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

import hippos
import eye_accessories
import back_accessories
import colors

# gets path to be used in image creation mechanism, using os
# dirname = os.path.dirname(__file__)
dirname = '/Users/randyrollofson/happy-hippos'

# sets final image dimensions as 480x480 pixels
# the original 34x34 pixel image will be expanded to these dimensions
dimensions = 480, 480

def addAccessory(hippo_array, accessory_array):
        for idx1, val1 in enumerate(hippo_array):
            for idx2, val2 in enumerate(val1):
                    if(accessory_array[idx1][idx2][0] != colors.xx[0] and
                    accessory_array[idx1][idx2][1] != colors.xx[1] and
                    accessory_array[idx1][idx2][2] != colors.xx[2]):
                        hippo_array[idx1][idx2] = accessory_array[idx1][idx2]
        return hippo_array

hippos = [hippos.hippo_basic, hippos.hippo_two_teeth, hippos.hippo_six_teeth, hippos.hippo_smile, 
hippos.hippo_tongue_out, hippos.hippo_lick]

# tells how many times to iterate through the following mechanism
# which equals the number of hippos
# e.g. 
# for x in range(0-200) 
# would generate 201 hippos numbered 0-200
# for x in range(0, 1):
for idx, hippo in enumerate(hippos):


    # # using ETH block number as starting random number seed
    # b=11981207
    # seed(x+b)

    # #head color - randomly generate each number in an RGB color
    # hd = (randint(0, 256), randint(0, 256), randint(0, 256))
    # c=randint(0,500)
    # seed(c)

    # #throat color - same as head color
    # th = (randint(0, 256), randint(0, 256), randint(0, 256))
    # d = randint(0,1000)
    # seed(d)

    # #eye "white" color
    # # if random number between 1-1000 is 47 or less - Crazy Eyes!
    # if d > 47:
    #     # normal eyes are always the same color
    #     ew = (240,248,255)
    #     ey = (0, 0, 0)
    # else:
    #     # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
    #     ew = (randint(0, 256), randint(0, 256), randint(0, 256))
    #     ey = (154, 0, 0)
    # e = randint(0,1000)
    # seed(e)

    # # beak color
    # f = randint(0, 1000)
    # if f > 500:
    #     # if random number is 501-1000 >> grey beak
    #     bk = (152, 152, 152)
    # elif 500 >= f > 47:
    #     # 48-500 >> gold beak
    #     bk = (204, 172, 0)
    # elif 47 >= f > 7:
    #     # 8 >> 47 >> red beak
    #     bk = (204, 0, 0) 
    # else:
    #     # random number is 7 or less >> black beak
    #     bk = (0, 0, 0) 

    hippo_array = np.array(hippo, dtype=np.uint8)
    sunglasses_array = np.array(eye_accessories.sunglasses, dtype=np.uint8)
    bird_array = np.array(back_accessories.bird, dtype=np.uint8)

    hippo_array = addAccessory(hippo_array, sunglasses_array)
    hippo_array = addAccessory(hippo_array, bird_array)

    # for idx1, val1 in enumerate(hippo_array):
    #     for idx2, val2 in enumerate(val1):
    #         if (sunglasses_array[idx1][idx2] != xx[idx1][idx2]):
    #             hippo_array[idx1][idx2] = sunglasses_array[idx1][idx2]

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
    # array = np.array(basic_hippo, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(hippo_array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/hippo_images/' + (str(idx + 1)) + '.png'
    new_image.save(imgname)