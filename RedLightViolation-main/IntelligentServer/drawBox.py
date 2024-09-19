import argparse
import cv2
import random
import os
import sys

from deep_sort_realtime.deepsort_tracker import DeepSort
from predict import *
from  yolov7.hubconf import custom
from ModelDetectionDAO import *

tracker = DeepSort()
char_model_path = get_char_model().get_path() + get_char_model().get_name()
char_model = custom(path_or_model=char_model_path)


def get_label_traffic(label):
    if str(label) == '0':
        return 'green'
    if str(label) == '1' or str(label) == '2':
        return 'red'
    
def draw_box_traffic(image, boxs) :
    reLabel = 1
    for i, (left, top, right, bottom, score, label) in enumerate(boxs) :
        if label==2: 
            label==1
        reLabel = label
        c1, c2 = (left, top), ( right, bottom)
        if str(label) == '1' or str(label) == '2':
            cv2.rectangle(image, c1, c2, color= (0,0,255), thickness= 2) # vex hcn
            cv2.putText(image, "{}".format(get_label_traffic(label)) + " {:.2f}".format(score), (c1[0], c1[1] - 2), 0, fontScale= 0.5, color = (0,0,255), thickness= 1, lineType= cv2.LINE_AA)
        
        else:
            cv2.rectangle(image, c1, c2, color= (0,0,255), thickness= 2) # vex hcn
            cv2.putText(image, "{}".format(get_label_traffic(label)) + " {:.2f}".format(score), (c1[0], c1[1] - 2), 0, fontScale= 0.5, color = (0,0,255), thickness= 1, lineType= cv2.LINE_AA)
        
    return image, reLabel

def draw_box_plate(image, boxs, labelTraffic, positionLine, plate_content_dict, path_save, list_images, relative_path) :
    os.makedirs(path_save, exist_ok= True)
    os.makedirs(os.path.join(path_save, 'images'), exist_ok= True)
    
    tracks = tracker.update_tracks(boxs, frame=image)
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        ltrb = track.to_ltrb()

        bbox = ltrb

        if track_id not in plate_content_dict:
            plate = image[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
            plate_content = predict_character(char_model, plate)
            plate_content_dict[track_id] = plate_content
        
        
        if labelTraffic == 1 and (int(bbox[3]) + (int(bbox[3]) - int(bbox[1]))) <= positionLine:
            cv2.rectangle(image, (int(bbox[0]),int(bbox[1])),(int(bbox[2]),int(bbox[3])),(0,0,255),2)
            cv2.putText(image, "#" + str(plate_content_dict[track_id]), (int(bbox[0]),int(bbox[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

            image_filename = os.path.join(path_save, 'images', f"{plate_content_dict[track_id]}.jpg")

            if os.path.isfile(image_filename):
                continue
            elif plate_content_dict[track_id] != "":
                captured_image = image[:int(positionLine)+20, :]
                cv2.imwrite(image_filename, captured_image)
                pathImage = relative_path + '/images/' + f"{plate_content_dict[track_id]}.jpg"
                list_images.append([pathImage, plate_content_dict[track_id]])
            
        elif (int(bbox[3]) + (int(bbox[3]) - int(bbox[1]))) <= positionLine:
           cv2.rectangle(image, (int(bbox[0]),int(bbox[1])),(int(bbox[2]),int(bbox[3])),(0,0,255),2)
           cv2.putText(image, str(plate_content_dict[track_id]), (int(bbox[0]),int(bbox[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
   
    return image, plate_content_dict, list_images