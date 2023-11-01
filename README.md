# Camera-Calibration-using-Checkerboard

this repository contains the basic code for camera calibration using checkerboard image. In this version, I use python3 and OpenCV to calibrate my laptop's camera. 

# Requirements
Camera   
Python = 3.9.0                             
OpenCV = 3.4.18

# Idea
Camera Calibration is the process of determining the camera's intrinsic and extrinsic parameters. Intrinsic parameters include the focal length, center offset and skew. While, extrinsic parameters include the translation and rotation of the camera. 
The main idea behind camera calibration is to establish a relationship between the 3D world and the 2D image acquired by the camera. A good calibrated camera produces accruate 2d image, which produces better results in applications involving the camera. 

First, we capture a set of checkerboard images from different poses. The checkerboard can come in different sizes. In my case, I used a 7x5 checkerboard image.

An example image of the checkerboard may look like this. 

![checkerboard_13](https://github.com/Taarun-Srinivas/Camera-Calibration-using-Checkerboard/assets/52371207/f9e39517-4ba0-4173-abac-c3f89f260b87)

using OpenCV's cv2.findChessboardCorners(), cv2.drawChessboardCorners(), and cv2.calibrateCamera(), we calibrate our camera using a set of given checkerboard images. Once our camera is able to detect the corners of the checkerboard with great precision, we can say that our camera is calibrated. Using cv2.drawChessboardCorners(), we can visualize our checkerboard images. 

![corners_13](https://github.com/Taarun-Srinivas/Camera-Calibration-using-Checkerboard/assets/52371207/1b433f8a-d829-42be-be20-62223909a774)

Finally, the cv2.calibrateCamera() returns the translation vector, the rotation matrix, the intrinsic matrix and distortion coefficients. 

# Applications
Camera calibration is a very important and most crucial step of any computer vision project. Most of our applications depends on the camera's internal parameters. Some example appliactions include in 3D reconstruction, Projective Geometry, Estimating the fundamental matrix in Epipolar Geometry and so on. 

