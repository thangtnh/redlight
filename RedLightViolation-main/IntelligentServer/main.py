from flask import Flask, request, jsonify
from datetime import timedelta
from flask_cors import CORS
import sys
import os

from detect import *

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(seconds=86400)
app.secret_key = "intelligent"
CORS(app)

@app.route('/api/detect_video', methods=['POST'])
def detectVideo():
    video = request.files.get('video')
    if not video:
        return "No video file found in the request"
    video_path = 'D:/IntelligentSystem/ClientServer/static/save/video/' + video.filename
    video.save(video_path)
    list_images, pathVideo = detect(video_path)

    detection_results = {
        "images": list_images,
        "video": pathVideo
    }

    return jsonify(detection_results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)