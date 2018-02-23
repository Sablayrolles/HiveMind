# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:08:58 2018

@author: louis
"""
from sound.constantes import *
import sound.record
import sound.exporting_graph_features
import sound.almostRealTimeVisualisation

sound.record.start()
names = []
for i in range(int(TOTAL_RECORD/SECTION)):
    names.append(sound.record.record(SECTION, "./data/test_"+str(i)+".wav"))
sound.record.stop()

#sound.almostRealTimeVisualisation.aff()

sound.exporting_graph_features.exportPlot()
sound.exporting_graph_features.exportPlotMoy()
sound.exporting_graph_features.exportPlotMax()