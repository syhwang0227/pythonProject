from PIL import Image
import os
from pathlib import Path


def image_crop(save_path):
    img_path = 'C:/pythonProject/test_img/'
    img_list = os.listdir(img_path)

    for image in img_list:
        # print("image:", image)  # "image: img_01.tif"
        img = Image.open('%s%s'%(img_path, image))
        (img_h, img_w) = img.size
        # print(img.size)

        grid_w = 32
        grid_h = 32
        range_w = (int)(img_w/grid_w)
        range_h = (int)(img_h/grid_h)
        print(range_w, range_h)

        i = 0
        img_list_crop = []
        for w in range(range_w):
            for h in range(range_h):
                bbox = (h*grid_h, w*grid_w, (h+1)*(grid_h), (w+1)*(grid_w))
                print(h*grid_h, w*grid_w, (h+1)*(grid_h), (w+1)*(grid_w))

                img_list_crop = img.crop(bbox)
                # img_list_crop.append(img_crop)
                # print(img_list_crop)

                file_name = Path(img_path + image).stem
                fname = "{}_{}.jpg".format(file_name, "{0:03d}".format(i))
                savename = save_path + fname
                img_list_crop.save(savename)
                # print('save file ' + savename + '...')
                i += 1


if __name__ == '__main__':
    image_crop('save/')

