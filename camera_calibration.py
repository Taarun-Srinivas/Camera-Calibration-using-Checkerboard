import cv2
import numpy as np

image_dir = [f"checkerboard/checkerboard_{i}.jpg" for i in range(1,23)]

def calibrate_camera(width, height, square_size, image_dir):
    obj_points = []
    img_points = []
    image_files = image_dir

    checkerboard_size = (width, height)
    square_size = square_size
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    points_3d = np.zeros((checkerboard_size[0] * checkerboard_size[1], 3), np.float32)
    ind = 0
    for i in range(checkerboard_size[0]):
        for j in range(checkerboard_size[1]):
            points_3d[ind][0] = i * square_size
            points_3d[ind][1] = j * square_size
            ind += 1

    for x,image in enumerate(image_files):
        # print(i)

        img = cv2.imread(image)
        image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(image, checkerboard_size, cv2.CALIB_CB_ADAPTIVE_THRESH +
                                                                           cv2.CALIB_CB_NORMALIZE_IMAGE)

        if ret == True:
            obj_points.append(points_3d)
            corners2 = cv2.cornerSubPix(gray, corners, (3, 3), (-1, -1), criteria)
            img_points.append(corners2)

            img = cv2.drawChessboardCorners(image, checkerboard_size, corners2, ret)
            cv2.imwrite(f"drawCorners/corners_{x+1}.png", img)

    ret, mtx, dist_coeff, R_vecs, T_vecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None,
                                                                   None)

    return mtx, dist_coeff

K_mat, dist_coeff = calibrate_camera(7,5,23,image_dir)
print("Intrinsic Matrix: \n", K_mat)
print("Distortion Coefficient: \n", dist_coeff)

# K = [[680, 0, 529],
#      [0, 1641, 511],
#      [0, 0, 1]]
