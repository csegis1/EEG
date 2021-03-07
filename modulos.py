# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 01:18:19 2018

@author: ricra
"""

import numpy as np
from os import listdir
import itertools
def ls(ruta = '.'):
    return listdir(ruta)

def minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax


def normalizar(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

def pselect(picose):
    vmayor=0;
    #print(picose)
    for elemento in itertools.combinations(picose,5):
        #print(elemento)
        #varianza=stats.variance(elemento)
        varianza=np.var([elemento])
        if varianza>vmayor:
            picosel=elemento
            vmayor=varianza
    return picosel