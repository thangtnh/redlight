from ClientDAO import *
import sys

sys.path.insert(0, 'D:/TraficRedLight/ClientServer/models')
from Image import * 

def add_image(image):
    connection = connect_to_mysql()
    if connection:
        query = "INSERT INTO image(name, path, content, idVideo) VALUES (%s, %s, %s, %s)"
        try:
            cursor = connection.cursor()
            cursor.execute(query, (image.get_name(), image.get_path(), image.get_content(), image.get_video().get_idVideo()))
            connection.commit()

        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
    close_connection(connection)

def get_image_by_video(video):
    connection = connect_to_mysql()
    images = []
    if connection:
        query = "SELECT * FROM image WHERE idVideo = %s;"
        try:
            cursor = connection.cursor()
            cursor.execute(query, (str(video.get_idVideo()), ))

            results = cursor.fetchall()
            if results:
                for row in results:
                    image = Image()
                    image.set_idImage(row[0])
                    image.set_name(row[1])
                    image.set_path(row[2])
                    image.set_content(row[3])
                    image.set_video(video)
                    images.append(image)
            return images
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
    close_connection(connection)

def delete_image():
    pass
