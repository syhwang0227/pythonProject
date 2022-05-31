from PIL import Image
import os
import numpy as np

img_path = 'C:/pythonProject/test_img/'
sv_path = 'C:/pythonProject/save_img/'

img_list = os.listdir(img_path)  # 디렉토리 내 모든 파일 불러오기
print("img_list: {}".format(img_list))

img_crop = []

for i in img_list:
    img = Image.open('%s%s'%(img_path, i))
    (img_h, img_w) = img.size
    print(img.size)

    grid_w = 32
    grid_h = 32
    range_w = (int)(img_w/grid_w)
    range_h = (int)(img_h/grid_h)
    print(range_w, range_h)

    i = 0
    for w in range(range_w):
        for h in range(range_h):
            bbox = (h*grid_h, w*grid_w, (h+1)*(grid_h), (w+1)*(grid_w))
            print(h*grid_h, w*grid_w, (h+1)*(grid_h), (w+1)*(grid_w))

            crop_img = img.crop(bbox)

            fname = "{}.jpg".format("{0:03d}".format(i))
            savename = sv_path + fname
            crop_img.save(savename)
            i += 1

