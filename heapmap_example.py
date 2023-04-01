# -*- coding: UTF-8 -*-
import os 
from common import * 
from data_common import * 
import numpy as np 
import pandas as pd
import matplotlib.cm as cm 

from data_common import PROCESS_DATA_PATH

ops = ["kendall"]

def read_process_data(path): 
    df = pd.read_csv(path, index_col = 0, sep = ",")
    assert isinstance(df, pd.DataFrame)
    label = df.columns.values.tolist()
    return label, df.values

def draw(data, labelx, labely, output): 
    with plt.style.context(get_default_heapmap_style_sheets()): 
        plt.tight_layout()
        fig = plt.figure()
        ax = fig.add_subplot(1 ,1 ,1)  #divide the whole figure into 1row, 1col(意味着只有一张子图) and ax index is 1 
        assert isinstance(ax, axes.Axes)

        ax.set_xlabel("id", fontsize=20)
        ax.set_xticks(range(len(labelx)))
        #ax.set_xticklabels(labelx, rotation=45)    #detail https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html
        ax.set_xticklabels(labelx, rotation=60)
        ax.set_ylabel("id", fontsize=20)
        ax.set_yticks(range(len(labely)))
        ax.set_yticklabels(labely)

        im = ax.imshow(data, cmap=plt.cm.RdYlBu, vmin=-1, vmax=1)
        #增加右侧的颜色刻度条
        plt.colorbar(im)
        save_figure(output)


if __name__ == '__main__':
    
    op = "kendall"
    exp = "raw"
    path = os.path.join(PROCESS_DATA_PATH,"%s_%s_%s.csv"%("heamap",exp, op))
    label, data =  read_process_data(path)
    label_x = label_y = ["%d"%x for x in range(len(label))]
    draw(data, label_x, label_y, "heapmap_example")
        
    