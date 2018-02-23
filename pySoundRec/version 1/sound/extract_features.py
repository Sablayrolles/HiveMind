# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:06:12 2018

@author: louis
"""

from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np

from .constantes import *

def calculate_moy_max(data, samplerate):
    global DEBUG
    
    data_moy = []
    data_max = []
    for j in range(int(len(data)/samplerate)+1):
            if DEBUG:
                print("[Sound][Extract_Features][Calculate_Moy_Max()] Ressource Computing : ", int(j/(len(data)/samplerate)*100),"%")
            ptnmoy = []
            ptnmoy.append(int(np.mean(data[j*samplerate:(j+1)*samplerate,0])))
            ptnmoy.append(int(np.mean(data[j*samplerate:(j+1)*samplerate,1])))
            
            ptn_max = []
            ptn_max.append(int(max(data[j*samplerate:(j+1)*samplerate,0].tolist())))
            ptn_max.append(int(max(data[j*samplerate:(j+1)*samplerate,1].tolist())))
            
            data_moy.append(ptnmoy)
            data_max.append(ptn_max)
    data_moy = np.array(data_moy)
    data_max = np.array(data_max)
    times_moy = np.array(np.arange(len(data)/float(samplerate)))+1
    
    return times_moy, data_moy, data_max

def get_back_values(NUM_IT):
    global DEBUG
    
    if DEBUG:
        print("[Sound][Extract_Features][Get_Back_Values()] Extracting : ", 'data/test_'+str(NUM_IT)+'.wav')
    samplerate, data = wavfile.read('./data/test_'+str(NUM_IT)+'.wav')
    times = np.arange(len(data))/float(samplerate)
    
    times_moy, data_moy, data_max = calculate_moy_max(data, samplerate)
    
    return times, data, times_moy, data_moy, times_moy, data_max

def get_all_values():
    global TOTAL_RECORD
    global SECTION
    global DEBUG
    
    # Load the data and calculate the time of each sample
    data_concat = 0
    for i in range(int(TOTAL_RECORD/SECTION)):
        if DEBUG:
            print("[Sound][Extract_Features][Get_All_Values()] Ressource Loading : ", int(i/(TOTAL_RECORD/SECTION)*100),"%")
        samplerate, data = wavfile.read('./data/test_'+str(i)+'.wav') #samplerate nbdata / s
        if type(data_concat) == int:
            data_concat = data
        else:
            data_concat = np.concatenate((data_concat, data), axis=0)
    data = data_concat
    times = np.arange(len(data))/float(samplerate)
    
    times_moy, data_moy, data_max = calculate_moy_max(data, samplerate)
    
    return times, data, times_moy, data_moy, times_moy, data_max