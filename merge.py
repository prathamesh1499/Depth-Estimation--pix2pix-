import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
"""for i in range(8,15):"""
path1= r'C:\Users\prathu\Desktop\dataset\o4_\shift_scale_rotate\o4_scr_'+str(6)+'.png'
path2= r'C:\Users\prathu\Desktop\dataset\o4_\shift_scale_rotate\d4_scr_'+str(6)+'.png'
img1=Image.open(path1).convert('RGB')
img2=Image.open(path2).convert('RGB')
#resizing
img1 = img1.resize((256,256), Image.ANTIALIAS)
img2 = img2.resize((256,256), Image.ANTIALIAS)
new_image=Image.new(color='white',size=(512,256),mode='RGBA')
area1=(0,0)#upper left corner
new_image.paste(img1,area1)
area2=(256,0)
new_image.paste(img2,area2)
image=np.asarray(new_image)
cv2.imwrite(r"C:\Users\prathu\Desktop\dataset\o4_\merg"+str(6)+".png",cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
#print('Image saved...')