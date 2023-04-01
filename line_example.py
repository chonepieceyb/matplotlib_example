
# -*- coding: UTF-8 -*-
from common import * 
import numpy as np 

## data 
feature_nums = [128, 256 ,512 ,1024 , 2048 ,4096 ,8192]

FPGA = [7516.027295, 3954.56259, 2019.451581,1020.67682, 513.0857978, 257.2082224, 128.7697043]
HF = [63.41477575,31.47062354,15.87697861,8.020621869,3.994575238,1.547713653,0.562993826]
MC = [899.3550158,498.4939301,274.5322686,125.6873949,71.85447867,32.64608727,16.35486789]

speed_hf = [118.5217042,125.6588574,127.1936954,127.2565689,128.4456462,166.1859233,228.72312]
speed_mc = [8.357130569,7.933020561,7.355971635,8.120757222,7.140623761,7.878684521,7.873478721]
## data end 

styles = get_default_line_style_sheets()

labels = feature_nums
y_1 = FPGA
y_2 = MC
y_3 = HF
y_2_labels = ["%.2fx"%x for x in  speed_mc]
y_3_labels = ["%.2fx"%x for x in  speed_hf]

x_ticks = list(range(len(labels)))
markers = ['o', '*', '^']
linecolor = ["orange","green","blue","red"]

fig_config = {
    'ylabel' : 'K items/s',   #x轴标签名
    'xlabel' : 'Number of features' , #y轴标签名
    'spine_config' : {
        "left" : ("data", 0),
        "right" : ("data", len(labels) - 1)
    }
}

line_config1 = {
    'matplot_config' : {
        'color' : linecolor[0], 
        'linewidth' : 5, 
        'label' : 'FPGA',  
        'marker' : markers[0], 
        'markersize' : 20
    }
}

line_config2 = {
    'matplot_config' : {
        'color' : linecolor[1], 
        'linewidth' : 5, 
        'label' : 'MCA',  
        'marker' : markers[1], 
        'markersize' : 20
    },
    'annotate_text_config' : {
        "color" : linecolor[1],
        "fontsize" : 30,
        "fontweight" : "bold",
        'ha' : 'center',
        'textcoords' : 'offset pixels',
        'xytext' : (0, 12),
        'family' : "Calibri"
        #"rotation" : 45
    }
}

line_config3= {
    'matplot_config' : {
        'color' : linecolor[2], 
        'linewidth' : 5, 
        'label' : 'HF',  
        'marker' : markers[2], 
        'markersize' : 20
    },
    'annotate_text_config' : {
        "color" : linecolor[2],
        "fontsize" : 30,
        "fontweight" : "bold",
        'ha' : 'center',
        'textcoords' : 'offset pixels',
        'xytext' : (0, -26),
        'family' : "Calibri"
        #"rotation" : 45
    }
}

start_line = {
    'matplot_config' : {
        'color' : 'grey', 
        'linewidth' : 2, 
        'linestyle' : '--'
    }
}
def draw(): 
    with plt.style.context(styles): 
        fig, ax = plt.subplots()
        ax.plot(x_ticks, y_1, **line_config1["matplot_config"])
        ax.plot(x_ticks, y_2, **line_config2["matplot_config"])
        ax.plot(x_ticks, y_3, **line_config3["matplot_config"])

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(fig_config['ylabel'])
        ax.set_xlabel(fig_config['xlabel'])

        ax.set_xticks(x_ticks)
        ax.set_xlim(0, len(labels) -1)  #设置 x轴范围
        ax.set_xticklabels(labels)
        
        ax.set_ylim(0.1, 100000)
        ax.set_yscale('log', base = 10, subs = [10])

        #设置纵坐标轴
        #ax.spines['left'].set_position(fig_config["spine_config"]["left"])
        #ax.spines['right'].set_position(fig_config["spine_config"]["right"])
    
        #添加加速比(y_2)
        
        for x, y , l in zip(x_ticks, y_2, y_2_labels): 
            ax.annotate(l, (x, y), **line_config2["annotate_text_config"])
        
        for x, y , l in zip(x_ticks, y_3, y_3_labels): 
            ax.annotate(l, (x, y), **line_config3["annotate_text_config"])
        ax.legend()
        
        
        #ax.bar_label(rects1, padding=3)
        #ax.bar_label(rects2, padding=3)

        fig.tight_layout()
    
        save_figure('line_example')
        #plt.show()
    
if __name__ == '__main__': 
    draw()