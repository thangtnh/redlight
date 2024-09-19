from ClientDAO import *
import sys
import os

sys.path.insert(0, 'D:/TraficRedLight/ClientServer/models')
from Video import *
from UserDAO import *
from ImageDAO import *

def get_all_videos():
    connection = connect_to_mysql()
    videos = []
    if connection:
        query = "SELECT * FROM video;"
        try:
            cursor = connection.cursor()
            cursor.execute(query)

            results = cursor.fetchall()
            if results:
                for row in results:
                    video = Video()
                    video.set_idVideo(row[0])
                    video.set_name(row[1])
                    video.set_path(row[2])

                    date_raw = str(row[3])
                    arrDate = date_raw.split('-')
                    arrDate.reverse()
                    date = ""
                    for i in range(len(arrDate)):
                        date += arrDate[i]
                        if i != len(arrDate)-1:
                            date += "/"
                    print(date)
                    video.set_detectDate(row[3])
                    user = get_user_by_id(str(row[4]))
                    video.set_user(user)
                    videos.append(video)
            return videos
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
    close_connection(connection)


def get_video_detail(idVideo):
    connection = connect_to_mysql()
    if connection:
        video = Video()
        query = "SELECT * FROM video WHERE idvideo = %s;"
        try:
            cursor = connection.cursor()
            cursor.execute(query, (idVideo,))

            results = cursor.fetchall()
            if results:
                for row in results:
                    
                    video.set_idVideo(row[0])
                    video.set_name(row[1])
                    video.set_path(row[2])
                    video.set_detectDate(row[3])
                    user = get_user_by_id(str(row[4]))
                    video.set_user(user)
                    return video
                
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
    close_connection(connection)

def add_video(video):
    connection = connect_to_mysql()
    if connection:
        query = "INSERT INTO video(nameVideo, path, detectDate, idUser) VALUES (%s, %s, %s, %s)"
        try:
            cursor = connection.cursor()
            cursor.execute(query, (video.get_name(), video.get_path(), video.get_detectDate(), video.get_user().get_idUser()))
            connection.commit()

            video_id = cursor.lastrowid
            video.set_idVideo(video_id)

            return video
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
    close_connection(connection)

def delete_video_by_id(idVideo):
    connection = connect_to_mysql()
    if connection:
        query = "DELETE FROM video WHERE idvideo = %s"
        try:
            cursor = connection.cursor()
            cursor.execute(query, (idVideo, ))
            connection.commit()

        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
    close_connection(connection)

if __name__ == "__main__":
    # video = Video()
    # video.set_name("hello.mp4")
    # video.set_path("abcd")
    # user = "user01"
    # video.set_user(user)
    # add_video(video)
    # videos = []
    videos = get_all_videos()