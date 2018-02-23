# -*- coding: utf-8 -*-

# Load the required libraries:
#   * scipy
#   * numpy
#   * matplotlib

from matplotlib import pyplot as plt

from .constantes import *
from . import extract_features

times, data, times_moy, data_moy, tmp, data_max = 0, 0, 0, 0, 0, 0

def exportPlot():
    global times
    global data
    global times_moy
    global data_moy
    global tmp
    global data_max
    global DEBUG
    
    times, data, times_moy, data_moy, tmp, data_max = extract_features.get_all_values()

    if DEBUG:
        print("[Sound][Exporting_Graph_Features][exportPlot()] Exporting plot")
    # Make the plot
    # You can tweak the figsize (width, height) in inches
    plt.figure(figsize=(30, 4))
    plt.fill_between(times, data[:,0], data[:,1], color='k') 
    plt.xlim(times[0], times[-1])
    plt.xlabel('time (s)')
    plt.ylabel('amplitude')
    # You can set the format by changing the extension
    # like .pdf, .svg, .eps
    plt.savefig('./data/plot.png', dpi=100)

def exportPlotMoy():
    global times
    global data
    global times_moy
    global data_moy
    global tmp
    global data_max
    
    times, data, times_moy, data_moy, tmp, data_max = extract_features.get_all_values()
    
    if DEBUG:
        print("[Sound][Exporting_Graph_Features][exportPlotMoy()] Exporting plot moy")
    # Make the plot
    # You can tweak the figsize (width, height) in inches
    plt.figure(figsize=(30, 4))
    plt.fill_between(times_moy, data_moy[:,0], data_moy[:,1], color='r')
    plt.xlim(times[0], times[-1])
    plt.xlabel('time (s)')
    plt.ylabel('amplitude')
    # You can set the format by changing the extension
    # like .pdf, .svg, .eps
    plt.savefig('./data/plot_moy.png', dpi=100)

def exportPlotMax():
    global times
    global data
    global times_moy
    global data_moy
    global tmp
    global data_max
    
    times, data, times_moy, data_moy, tmp, data_max = extract_features.get_all_values()
    
    if DEBUG:
        print("[Sound][Exporting_Graph_Features][exportPlotMax()] Exporting plot max")
    # Make the plot
    # You can tweak the figsize (width, height) in inches
    plt.figure(figsize=(30, 4))
    plt.fill_between(times_moy, data_max[:,0], data_max[:,1], color='b') 
    plt.xlim(times[0], times[-1])
    plt.xlabel('time (s)')
    plt.ylabel('amplitude')
    # You can set the format by changing the extension
    # like .pdf, .svg, .eps
    plt.savefig('./data/plot_max.png', dpi=100)