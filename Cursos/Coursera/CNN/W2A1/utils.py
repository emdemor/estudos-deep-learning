import numpy as np
from PIL import Image


def center_crop(imagem, basewidth=64):

    img = np.array(imagem)

    width = img.shape[1]

    height = img.shape[0]

    new_width = min(width, height)

    new_height = min(width, height)

    left = int(np.ceil((width - new_width) / 2))

    right = width - int(np.floor((width - new_width) / 2))

    top = int(np.ceil((height - new_height) / 2))

    bottom = height - int(np.floor((height - new_height) / 2))

    if len(img.shape) == 2:
        center_cropped_img = img[top:bottom, left:right]
    else:
        center_cropped_img = img[top:bottom, left:right, ...]

    img = Image.fromarray(center_cropped_img)

    wpercent = basewidth / float(img.size[0])

    hsize = int((float(img.size[1]) * float(wpercent)))

    img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    return img