import random
import cv2
import numpy as np
import math
from PIL import Image
import matplotlib.pyplot as plt

class ShiftScaleRotate:
    def __init__(self, shift_limit=0.0625, scale_limit=0.25, rotate_limit=50, prob=1):
        self.shift_limit = shift_limit
        self.scale_limit = scale_limit
        self.rotate_limit = rotate_limit
        self.prob = prob

    def __call__(self, img, mask=None):
        if random.random() < self.prob:
            height, width, channel = img.shape

            angle = random.uniform(-self.rotate_limit, self.rotate_limit)
            scale = random.uniform(1-self.scale_limit, 1+self.scale_limit)
            dx = round(random.uniform(-self.shift_limit, self.shift_limit)) * width
            dy = round(random.uniform(-self.shift_limit, self.shift_limit)) * height

            cc = math.cos(angle/180*math.pi) * scale
            ss = math.sin(angle/180*math.pi) * scale
            rotate_matrix = np.array([[cc, -ss], [ss, cc]])

            box0 = np.array([[0, 0], [width, 0],  [width, height], [0, height], ])
            box1 = box0 - np.array([width/2, height/2])
            box1 = np.dot(box1, rotate_matrix.T) + np.array([width/2+dx, height/2+dy])

            box0 = box0.astype(np.float32)
            box1 = box1.astype(np.float32)
            mat = cv2.getPerspectiveTransform(box0, box1)
            img = cv2.warpPerspective(img, mat, (width, height),
                                      flags=cv2.INTER_LINEAR,
                                      borderMode=cv2.BORDER_REFLECT_101)
            if mask is not None:
                mask = cv2.warpPerspective(mask, mat, (width, height),
                                           flags=cv2.INTER_LINEAR,
                                           borderMode=cv2.BORDER_REFLECT_101)

        return img, mask


img1 = Image.open(r'C:\Users\prathu\Desktop\dataset\o2_\o2.png').convert('RGB').resize((2048,2048))
img1_arr = np.asarray(img1)
img1_arr.shape

img2 = Image.open(r'C:\Users\prathu\Desktop\dataset\o2_\d2.png').convert('RGB')
img2_arr = np.asarray(img2)
img2_arr.shape
for i in range(15):
    scr = ShiftScaleRotate( shift_limit=0.0625, scale_limit=0.3, rotate_limit=0, prob=1)
    new_img1,new_img2 = scr.__call__(img1_arr,img2_arr)
    im1 = Image.fromarray(new_img1).convert('RGB')
    im1.save(r'C:\Users\prathu\Desktop\dataset\o2_\shift_scale_rotate\o2_scr_'+str(i)+'.png')
    im2 = Image.fromarray(new_img2).convert('RGB')
    im2.save(r'C:\Users\prathu\Desktop\dataset\o2_\shift_scale_rotate\d2_scr_'+str(i)+'.png')
