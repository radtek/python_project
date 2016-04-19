'''
Created on 2016年4月7日

@author: THINK
'''

from PIL import Image,ImageFilter

im = Image.open('949.jpg')

# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')