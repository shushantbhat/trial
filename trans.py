import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\shush\Downloads\Sagittal-spinal-magnetic-resonance-imaging-MRI-Miliary-lesions-in-the-vertebral-bodies.png")


def rotate(img):
    rows, cols = img.shape[:2]
    img_rotation = cv2.warpAffine(img, cv2.getRotationMatrix2D((cols/2, rows/2),
                                                        30, 0.6),
                                 (cols, rows))
    cv2.imshow('img', img_rotation)
    cv2.imshow('img',img)
    cv2.waitKey()
    
    cv2.destroyAllWindows()


def Translate(img):
    rows, cols = img.shape[:2]
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def Affine_Transformation (img):
    rows, cols = img.shape[:2]  
    pts1 = np.float32([[50, 50],
                   [200, 50], 
                   [50, 200]])
 
    pts2 = np.float32([[10, 100],
                   [200, 50], 
                   [100, 250]])
 
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #abc
def Cropping (img):
    cropped_img = img[100:300, 100:300]
    cv2.imshow('cropped_out.jpg', cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def Shear (img):
    rows, cols = img.shape[:2] 
    M = np.float32([[1,   0, 0], [0.5, 1, 0], [0,   0, 1]])
    sheared_img = cv2.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
    cv2.imshow('sheared_y-axis_out.jpg', sheared_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
rotate(img)
Translate(img)
Affine_Transformation (img)
Shear(img)
Cropping (img)