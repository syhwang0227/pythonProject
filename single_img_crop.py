from PIL import Image


def image_crop(infilename, save_path):
    img = Image.open(infilename)
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

            fname = "{}.jpg".format("{0:04d}".format(i))
            savename = save_path + fname
            crop_img.save(savename)
            print('save file ' + savename + '...')
            i += 1


if __name__ == '__main__':
    image_crop('test_img/img_01.tif', 'save/')

