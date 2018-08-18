
# -*- coding: utf-8 -*-
"""
Author         : Umair Akhtar
Contact        : omayr.akhtar@gmail.com 
Copyright      : na
Created        : 18.08.2018
Latest Version : 18.08.2018
Description    : Exploratory analysis and visualization of signals
"""

import numpy as np
from matplotlib import pyplot as plt

def read_signals():
	
	with open('data.dat','r') as d:
		signal = d.readlines()

	signal = np.array(signal)

	plt.plot(signal[0:1000])
	plt.show()

	return None

read_signals()