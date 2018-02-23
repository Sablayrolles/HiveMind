# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 09:19:42 2018

@author: louis
"""

#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from matplotlib import style
import matplotlib.animation as animation
import threading
import time

from . import extract_features
from .constantes import *

NUM_IT = 0
ax1 = 0
ax2 = 0
ax3 = 0
 
def update_graph(dt):
    global NUM_IT
    global ax1
    global ax2
    global ax3
    global DEBUG
        
    if DEBUG:
        print("[Sound][AlmostRealTimeVisualisation][update_graph()] Iteration : ", NUM_IT)
    
    x1, y1, x2, y2, x3, y3 = extract_features.get_back_values(NUM_IT)
    ax1.clear()
    ax2.clear()
    ax3.clear()
    #ax1.set_ylim(0, 10, auto=False)
    #ax2.set_ylim(0, 10, auto=False)
    ax3.set_xlabel('Temps')
    ax1.set_ylabel('amplitude', color='g')
    ax2.set_ylabel('amplitude moyenne', color='r')
    ax3.set_ylabel('amplitude maximum', color='b')
    ax1.plot(x1, y1, 'g-o')
    ax2.plot(x2, y2, 'r-o')
    ax3.plot(x3, y3, 'b-o')
    
    NUM_IT += 1
            
def aff():
    global ax1
    global ax2
    global ax3
    
    app = tk.Tk()
    app.wm_title("Graphe Matplotlib dans Tkinter")
     
    style.use("ggplot")
    fig = Figure(figsize=(12, 9), dpi=112)
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312, sharex=ax1)
    ax3 = fig.add_subplot(313, sharex=ax1)
    ax3.set_xlabel('Temps')
    ax1.set_ylabel('amplitude', color='g')
    ax2.set_ylabel('amplitude moyenne', color='r')
    ax3.set_ylabel('amplitude maximum', color='b')
    fig.tight_layout()
     
    graph = FigureCanvasTkAgg(fig, master=app)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=0)

    time.sleep(SECTION)
    ani = animation.FuncAnimation(fig, update_graph, interval=int(TOTAL_RECORD/SECTION)*1000)
    app.mainloop()

if __name__ == "__main__":
    aff()