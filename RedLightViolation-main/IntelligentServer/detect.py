import cv2
import os
import sys
sys.path.insert(0, 'D:/IntelligentSystem/IntelligentServer/yolov7')
sys.path.insert(0, 'D:/IntelligentSystem/IntelligentServer/controller')

from  yolov7.hubconf import custom
import moviepy.editor as moviepy

from predict import *
from drawBox import *
from ModelDetectionDAO import *

def take_score(elem):
    return elem[4]

def non_max_suppression(boxes, threshold):
    order = boxes.copy()
    keep = []
    while order:
        i = order.pop(0)
        keep.append(i)
        for j in order:
            # Calculate the IoU between the two boxes
            box_i = i.copy()
            box_j = j.copy()
            intersection = max(0, min(box_i[2], box_j[2]) - max(box_i[0], box_j[0])) * \
                           max(0, min(box_i[3], box_j[3]) - max(box_i[1], box_j[1]))
            union = (box_i[2] - box_i[0]) * (box_i[3] - box_i[1]) + \
                    (box_j[2] - box_j[0]) * (box_j[3] - box_j[1]) - intersection
            iou = intersection / union

            # Remove boxes with IoU greater than the threshold
            if iou > threshold:
                order.remove(j)
    return keep

def detect(pathVideo):
    path_save = 'D:/IntelligentSystem/ClientServer/static/save'
    relative_path = "../static/save"

    os.makedirs(path_save, exist_ok= True)
    os.makedirs(os.path.join(path_save, 'video'), exist_ok= True)

    traffic_model_path = get_traffic_model().get_path() + get_traffic_model().get_name()
    plate_model_path = get_plate_model().get_path() + get_plate_model().get_name()
    model = custom(path_or_model=traffic_model_path)
    model1 = custom(path_or_model=plate_model_path)

    name_video = pathVideo.split('/')[-1]
    

    cap = cv2.VideoCapture(pathVideo)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video = cv2.VideoWriter(os.path.join(path_save, 'video', name_video.split('.')[0]+'.avi'), 
                        cv2.VideoWriter_fourcc(*'XVID'),
                        10, (width, height))
    
    plate_content_dict = {}
    list_images = []

    count = 0
    t = 0
    while cap.isOpened():
        count += 1
        if count%15 != 0:
            continue
        _, frame = cap.read()
        if frame is None:
            break

        results = predict_traffic(model, frame)
        results1 = predict_plate(model1, frame)

        if results is not None and results1 is not None :
            results = non_max_suppression(results, 0.45)

            if t == 0:
                lenTraffic = (results[0][3] - results[0][1])
                if lenTraffic <= height*0.15:
                    t = results[0][3] + lenTraffic*2
                else:
                    t = results[0][3] + lenTraffic*1.25
            
            # cv2.line(frame, (0,int(t)), (10000, int(t)), (255, 0, 0), thickness=1, lineType=8, shift=0)

            frame, labelTraffic = draw_box_traffic(frame, results)
            frame, plate_content_dict, list_images = draw_box_plate(frame, results1, labelTraffic, t, plate_content_dict,\
                                                        path_save, list_images, relative_path)

        video.write(frame)
        # cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        
    cap.release()
    video.release()

    os.remove(pathVideo)
    # print('Done, save video: {}'.format(os.path.join(path_save, source, name_video.split('.')[0]+'.avi')))
    path_video = '{}'.format(os.path.join(path_save, 'video', name_video.split('.')[0]+'.avi'))
    clip = moviepy.VideoFileClip(path_video)
    clip.write_videofile(pathVideo)
    os.remove(path_video)
    relative_path += "/video/" + name_video
    return list_images, relative_path

if __name__ == '__main__' :
    pathVideo = "D:/TraficRedLight/ClientServer/static/videos/abcd.mp4"
    path_save = "D:/TraficRedLight/ClientServer/static/save"
    detect(pathVideo, path_save)