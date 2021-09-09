# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# gets path to be used in image creation mechanism, using os
# dirname = os.path.dirname(__file__)
dirname = '/Users/randyrollofson/generate-bitbirds'

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 480, 480

# tells how many times to iterate through the following mechanism
# which equals the number of birds
# e.g. 
# for x in range(0-200) 
# would generate 201 birds numbered 0-200
for x in range(0, 1):

    # using ETH block number as starting random number seed
    b=11981207
    seed(x+b)

    #head color - randomly generate each number in an RGB color
    hd = (randint(0, 256), randint(0, 256), randint(0, 256))
    c=randint(0,500)
    seed(c)

    #throat color - same as head color
    th = (randint(0, 256), randint(0, 256), randint(0, 256))
    d = randint(0,1000)
    seed(d)

    #eye "white" color
    # if random number between 1-1000 is 47 or less - Crazy Eyes!
    if d > 47:
        # normal eyes are always the same color
        ew = (240,248,255)
        ey = (0, 0, 0)
    else:
        # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
        ew = (randint(0, 256), randint(0, 256), randint(0, 256))
        ey = (154, 0, 0)
    e = randint(0,1000)
    seed(e)

    # beak color
    f = randint(0, 1000)
    if f > 500:
        # if random number is 501-1000 >> grey beak
        bk = (152, 152, 152)
    elif 500 >= f > 47:
        # 48-500 >> gold beak
        bk = (204, 172, 0)
    elif 47 >= f > 7:
        # 8 >> 47 >> red beak
        bk = (204, 0, 0) 
    else:
        # random number is 7 or less >> black beak
        bk = (0, 0, 0) 

    # background color
    # bg = (238, 238, 238)
    bg = (0,255,255)
    # outline color
    ol = (0, 0, 0)
    # eyes
    ey = (255, 255, 255)
    
    # (1 = lightest, 5 = darkest)
    # color 1
    c1 = (159, 105, 52)
    # color 2
    c2 = (139, 93, 46)
    # color 3
    c3 = (120, 80, 39)
    # color 4
    c4 = (101, 67, 33)
    # color 5
    c5 = (82, 54, 27)

    basic_hippo = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, c4, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, ol, ol, ol, ol, ol, bg, ol, c3, ol, c4, c5, ol, ol, ol, ol, bg, ol, ol, ol, ol, c5, c4, ol, c3, ol, bg, bg, bg, bg, bg, bg, bg],
        [ol, ol, c2, c2, c2, c2, c2, ol, ol, c3, c3, c3, c3, c3, c2, c2, c3, ol, c5, c3, c2, c2, c2, c3, c3, c5, ol, bg, bg, bg, bg, bg, bg, bg],
        [c2, c2, c2, c2, c2, c2, c3, c3, c3, ol, c3, c3, c4, c3, ol, ol, c3, c3, c3, c3, ol, ol, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [c2, c2, c1, c2, c2, c1, c1, c2, c2, ol, c5, c3, c2, ol, ey, ey, ol, c4, c3, ol, ey, ey, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [c2, c1, c1, c1, c1, c1, c1, c1, c1, c3, ol, c4, c2, ol, ey, ol, ol, c4, c2, ol, ey, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [c1, c1, c1, c1, c1, c1, c1, c3, c1, c3, c3, ol, c5, ol, ol, ol, ol, c2, c2, ol, ol, ol, ol, c2, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [c1, c1, c1, c2, c1, c1, c1, c1, c1, c1, c3, c2, ol, c4, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c5, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [c1, c1, c1, c1, c2, c1, c1, c1, c1, c1, c2, c2, ol, c2, c2, c2, c1, c1, c1, c1, c1, c2, c2, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg],
        [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c2, ol, c4, c4, c3, c1, c1, c1, ol, ol, c1, c1, c1, c1, c1, c1, ol, ol, bg, bg, bg, bg, bg, bg],
        [c2, c2, c1, c1, c1, c1, c1, c1, c3, c3, ol, c4, c4, c3, c3, c1, c1, ol, c4, ol, c1, c1, c1, c1, c1, ol, c4, ol, ol, bg, bg, bg, bg, bg],
        [c2, c2, c2, c2, c1, c1, c1, c4, c3, ol, c5, c4, c2, c2, c1, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, ol, ol, ol, c5, ol, bg, bg, bg, bg],
        [c2, c4, c2, c2, c2, c1, c1, c4, c4, ol, c5, c4, c2, c2, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, c4, ol, bg, bg, bg, bg],
        [c3, c3, c3, c2, c2, c2, c2, c2, c4, ol, c4, c3, c3, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c4, ol, bg, bg, bg, bg],
        [c3, c3, c3, c4, c2, c2, c2, c2, c4, ol, c4, c4, c3, c2, c1, c1, ol, ol, ol, c1, c1, c1, c1, c1, c1, c1, ol, ol, c3, ol, bg, bg, bg, bg],
        [c4, c3, c4, c4, c4, c2, c2, c3, c3, ol, c5, c4, c3, c2, c1, c1, c1, c1, ol, ol, ol, ol, ol, ol, ol, ol, ol, c1, c2, ol, bg, bg, bg, bg],
        [c4, c4, c2, c2, c3, c4, c3, c3, c3, c3, ol, c4, c4, c3, c2, c2, c1, c1, ol, ey, ol, c1, c1, c1, ol, ey, ol, c1, ol, bg, bg, bg, bg, bg],
        [c3, c3, c4, c2, c4, c5, c3, c5, c3, c4, c5, ol, c3, c3, c3, c2, c1, c1, ol, ol, ol, c1, c1, c1, ol, ol, ol, c1, ol, bg, bg, bg, bg, bg],
        [c4, c3, c3, c3, c3, c3, c4, c4, c2, c4, c5, c5, ol, c5, c4, c4, c3, c1, c1, c1, c1, c1, c1, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg],
        [c4, c4, c4, c4, c4, c3, c3, c4, c1, c5, c4, c5, c5, ol, ol, ol, ol, c5, c4, c3, c2, c2, c2, c2, c2, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [c5, c5, c4, c4, c4, c4, c3, c1, c1, c4, c4, c5, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [c5, c5, c5, c5, c5, c4, c4, c1, c1, c3, c4, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [c5, c5, c5, c5, c5, c5, c4, c1, c1, c3, c4, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [c5, c5, c5, c5, c5, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [c5, c5, c5, ol, ol, ol, c5, c1, c1, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [ol, ol, ol, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, c5, c1, c1, c3, c3, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    # choose which bird image to use
    # seed(f)
    # g = randint(0,1000)
    # if g > 250:
    #     # if random number is 251 - 1000 >> basic bird
    #     pixels = basic_bird
    #     p = "basic"
    # elif 250 >= g > 100:
    #     # 101 - 250 >> jay
    #     pixels = jay
    #     p = "jay"
    # elif 100 >= g > 40:
    #     # 41 - 100 >> woodpecker
    #     pixels = woodpecker
    #     p = "pecker"
    # elif 40 >= g > 5:
    #     # 6 - 40 >> eagle
    #     pixels = eagle
    #     p = "eagle"
    # else:
    #     # if random number is 5 or less >> cockatoo!!
    #     pixels = cockatoo
    #     p = "cockatoo"

    # convert the pixels into an array using numpy
    array = np.array(basic_hippo, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/bird_images/' + (str(x)) + '.png'
    new_image.save(imgname)