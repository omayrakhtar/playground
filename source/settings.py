# -*- coding: utf-8 -*-
'''
Author         : Umair
Contact        : omayr.akhtar@gmail.com
Copyright      : None
Created        : 25.06.2018
Latest Version : 25.06.2018
Description    : settings and configurations
'''

from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Umair'

from os.path import join
from os.path import abspath
from os.path import dirname
from os import pardir




class Config(object):

    CURRENT_DIR = abspath(dirname(__file__))  # Up to source/
    ROOT_DIR = abspath(join(CURRENT_DIR, pardir))  # Up to cancer-ai/
    DATA_DIR = abspath(join(ROOT_DIR, "data"))  # Up to data/
    MODELS_DIR = abspath(join(ROOT_DIR, "models"))  # Up to models/
    LOGS_DIR = abspath(join(ROOT_DIR, "logs"))  # Up to logs/
