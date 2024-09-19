# RED LIGHT VIOLATION LICENSE PLATE RECOGNITION SYSTEM
## 1. Introduction project
This is an applied research in the field of traffic security and road traffic management, assisting in capturing images and license plate information of vehicles that run red lights
### Subproblem 1: Tracking object
Detect whether there is a red light, during the appearance of the red light, and if any vehicle runs the red light. The red light detection problem requires using deep learning algorithms to solve it and tracking detected objects using tracking algorithms. The goal after solving this problem is to extract images containing red light violations from the video.

### Subproblem 2: Detect license plates
The input of this problem is the images extracted from the first problem. This problem aims to solve the extraction of images containing the license plates of violating vehicles using machine learning methods. After implementation, the output images of this problem will be the license plate images of vehicles running red lights.

### Subproblem 3: Text recognition
The input of this problem is the license plate images from the output of the second problem. The problem uses machine learning algorithms to detect characters in the input images. The goal of the problem, after implementation, is to obtain the license plate information of the vehicles that ran red lights.

## 2. Dataset
### 2.1. Light color classification
- Total images: 2047 images
- Labels: 3 label include: green(789 images), red(1016 images), yellow(242 images)

![image](https://github.com/user-attachments/assets/17f61aa2-68f4-418f-b78c-ab63085a7e2d)

### 2.2. Detect license plates
- Total images: 9031 images
- Label: only 1 label is plate

![image](https://github.com/user-attachments/assets/e164a37d-1bfc-4a25-92a7-a2ebff704b38)

### 2.3. Text recognition
- Total images: 3188 images
- Labels: 36 labels include: : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.

![image](https://github.com/user-attachments/assets/1c6962c6-fd86-4ed7-9e8e-dd53401d7ec3)

## 3. Algorithm
YOLO (You Only Look Once) is a popular object detection model known for its fast speed and high accuracy. This model was first introduced by Joseph Redmon and colleagues in 2016

YOLO proposes the use of an end-to-end neural network to simultaneously predict bounding boxes and the probability of objects. This differs from the approach of previous object detection algorithms, which reused classifiers to perform detection.

YOLO v7, a version released in 2022, has several improvements over previous versions. One of the main enhancements is the use of anchor boxes
Anchor boxes are a set of predefined boxes with different aspect ratios used to detect objects of various shapes. YOLO v7 uses nine anchor boxes, allowing it to detect a wider range of object shapes and sizes compared to previous versions, thereby reducing the number of false detections.

![image](https://github.com/user-attachments/assets/e4e04b6a-3431-4589-b7c3-0c8b04f578d0)

### Scenario and Evaluation methods
- Training with all dataset in 5 times
- Training process:
  
   	      Accuracy	  Precision	  Recall	  F1-Score

          85.00%	    92.70%	    91.10%	  91.89%
  
          86.68%	    92.52%	    91.21%	  91.86%
  
          83.33%	    90.70%	    92.27%	  91.47%
  
          84.00%	    91.15%	    90.02%	  90.58%
  
          90.00%	    91.20%	    89.60%	  90.39%
  
Averaged:	85.80%,	    91.65%,	    90.84%,	  91.24%


### Results
![image](https://github.com/user-attachments/assets/f36154ba-d857-424b-9912-5ad24a743f81)

![image](https://github.com/user-attachments/assets/be3e1068-c4cc-4fa0-9a0f-ed542190af66)

![image](https://github.com/user-attachments/assets/00e5ee72-b06d-438c-aa89-391f42c26eb8)

## 4. Client system design
* Interace layer: login.html, home.html
* Handle data layer:
  - Controller class:
     + detectionVideo.py: virtual class in intelligent server. This class need have detectVideo() function to handle video, return information of video, images and license plates detected in video. Client use API is provided by server to call this function.
     + main.py: saveVideo() function to save video, images and another information to database
   - Connect data class: DAO, UsserDAO, VideoDAO
* Entity layer: User, Video, ImageViolation, LicensePlate
  
![image](https://github.com/user-attachments/assets/a8112a70-19e9-4714-8e4e-4ab793d8d368)

### Application in web
- Home page:

![image](https://github.com/user-attachments/assets/5275d293-2551-42b7-9c4e-0372154128ec)

- Select video from computer or laptop

![image](https://github.com/user-attachments/assets/c773779a-b9c1-4595-96ad-debf041782e0)

- User click "Upload video", Clien will call API is served from intelligent serrver to handle video

![image](https://github.com/user-attachments/assets/d94a41f1-7881-4528-be56-dbe1f78b7d64)

- After handle, interface will show detected video, images and license plates detected in video
  
![image](https://github.com/user-attachments/assets/4a434146-6599-4635-b972-7303b94719c2)

- Usser can click “SAVE VIDEO AND IMAGE” if they want save data in database and website will be reloaded.



