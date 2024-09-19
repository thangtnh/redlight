from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from flask_cors import CORS
from datetime import timedelta
import sys
import os
import datetime
sys.path.insert(0, 'D:/IntelligentSystem/ClientServer/controller')
sys.path.insert(0, 'D:/IntelligentSystem/ClientServer/models')

from Video import *
from Image import *
import moviepy.editor as moviepy

from UserDAO import *
from VideoDAO import *
from ImageDAO import *
from PlateDAO import *

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(seconds=86400)
app.secret_key = "intelligent"
CORS(app)

@app.route("/login", methods = ["GET", "POST"])
def login():
    msg=''
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        session.permanent = True
        username = request.form["username"]
        password = request.form["password"]
        user = checkLogin(username, password)
        if user is not None:
            session["login"] = True
            session["fullname"] = user.get_fullname()
            session["user"] = user.__dict__
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username / password !'
            
    return render_template('login.html', msg = msg)

@app.route("/", methods = ["GET", "POST"])
def home():
    tmp = "novideo"
    image_files = "noImage"
    if "fullname" in session:
        fullname = session["fullname"]
        return render_template("index.html", video_name = tmp, image_files=image_files, fullname = fullname)
    
    return redirect(url_for('login'))

@app.route("/api/upload", methods = ["GET","POST"])
def upload():
    data = request.get_json()
    image_paths = data.get('images')
    video_path = data.get('video')
    # print(video_path)
    # for i in image_paths:
    #     print(i)

    video_db_save = Video()
    nameVideo = video_path.split('/')[-1]

    lastIndexVideo = video_path.rfind('/')
    videoPath = video_path[:lastIndexVideo+1]

    user_data = session.get('user')
    user = User(**user_data)

    video_db_save.set_name(nameVideo)
    video_db_save.set_path(videoPath)
    video_db_save.set_detectDate(datetime.date.today())
    video_db_save.set_user(user)

    video_db = add_video(video_db_save)
    for image in image_paths:
        image_db_save = Image()

        nameImage = image.split('/')[-1]
        content = nameImage.split('.')[0]
        lastIndexImage = image.rfind('/')
        pathImage = image[:lastIndexImage+1]

        print(nameImage)
        print(content)
        print(lastIndexImage)
        print(pathImage)

        image_db_save.set_name(nameImage)
        image_db_save.set_path(pathImage)
        image_db_save.set_content(content)
        image_db_save.set_video(video_db)
        print(image_db_save.get_content())
        print(video_db_save.get_name())
        add_image(image_db_save)

    response_data = {'status': 'success', 'message': 'Data received successfully'}
    return jsonify(response_data)

@app.route("/logout", methods = ["GET"])
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/getallvideos", methods = ["GET", "POST"])
def get_videos():
    if "fullname" in session:
        fullname = session["fullname"]

        videos = get_all_videos()
        return render_template('listVideos.html', fullname=fullname, videos = videos)
    return redirect(url_for('login'))

@app.route("/video/<int:idVideo>", methods = ["GET", "POST"])
def get_video(idVideo):
    if "fullname" in session:
        fullname = session["fullname"]
        video = get_video_detail(idVideo)
        images = get_image_by_video(video)
        results = []
        for image in images:
            results.append([image.get_name(), image.get_content()])

        # video_name = video.get_name()

        return render_template('video.html', fullname=fullname, video = video, results = results)
    return redirect(url_for('login'))

@app.route("/deleteVideo/<int:idVideo>", methods = ["GET", "POST"])
def delete_video(idVideo):
    if "fullname" in session:
        delete_video_by_id(idVideo)
        return redirect(url_for('get_videos'))
    
    return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)