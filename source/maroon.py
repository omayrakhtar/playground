#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author         : Umair
Contact        : omayr.akhtar@gmail.com
Copyright      : None
Created        : 25.06.2018
Latest Version : 25.06.2018
Description    : Python script file for experimenting and learning

"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Umair'

from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime
import openslide
from os.path import join
from os.path import abspath
import sys
from settings import Config as cf

from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from skimage.feature import hog
from skimage.feature import local_binary_pattern as lbp
from skimage.feature import ORB
import cv2 as cv
from skimage.feature import BRIEF
from skimage.feature import corner_peaks
from skimage.feature import corner_harris


def read_tiff():


    '''
    A simple method that reads a tiff file

    :return: None

    '''

    sample_image = openslide.open_slide(abspath(join(cf.DATA_DIR,'test_128.tif')))
    print(sample_image.associated_images)
    #for i in range(len(sample_image.level_dimensions)):
    #    print("DS level:%s Res:%s"% (sample_image.level_downsamples[i], sample_image.level_dimensions[i]))

def string_manipulation(my_str):

    my_str = 'I have changed the string'
    
    return None

def test_func():

    test_str = 'This is a test string'
    print(test_str)
    string_manipulation(test_str)
    print(test_str)

test_func()

