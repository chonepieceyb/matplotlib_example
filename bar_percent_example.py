
# -*- coding: UTF-8 -*-
from common import * 
import numpy as np 

## data 

## data end 

styles = get_default_bar_style_sheets()

labels = ['#1', '#2', '#3', '#4', '#5']
y_1 = np.array([30, 40, 20, 30, 50])
y_2 = np.array([10, 20, 5, 20, 30])
y_3 = np.array([10, 15, 10, 25, 25])

#all_num = [y_1[i] + y_2[i] + y_3[i] for i in range(labels)]

datas = [y_1, y_2, y_3]
all_num = y_1 + y_2 + y_3

percent_list = [
    y_1 / all_num,
    y_2 / all_num,
    y_3 / all_num,
]

percent_label = [["%.1f%%"%(p*100) for p in  percent] for percent in percent_list]

barcolor = ["bisque","honeydew","lightskyblue","mistyrose"]
linecolor = ["orange","green","blue","red"]
hatch_style = ['x', '\\', '/']

markers = ['o', '*', '^']
linecolor = ["orange","green","blue","red"]

fig_config = {
    'xlabel' : '#CPU',   #x轴标签名
    'ylabel' : 'Time (us)' , #y轴标签名
    'bar_width' : 0.5, #每一根柱子的宽度
    'text_size' : 19
}

bar_config1 = {
    "matplot_config" : {
        #'color' : '#74A9D0', 
        'color' : barcolor[0], 
        'edgecolor' : linecolor[0],
        'linewidth' : 3, 
        'label' : 'Kernel',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : hatch_style[0]
    },
    "hatch_config" : {
        'color' : linecolor[0],
        'linewidth' : 2
    },
    "text_config" : {
        "fontsize" : fig_config["text_size"], 
        "color": linecolor[0],
    }
}

bar_config2 = {
    "matplot_config" : {
        #'color' : '#A1BA66', 
        'color' : barcolor[1],
        'edgecolor' : linecolor[1],
        'linewidth' : 3, 
        'label' : 'User',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : hatch_style[1]
    },
    "hatch_config" : {
        'color' : linecolor[1],
        'linewidth' : 2
    },
    "text_config" : {
        "fontsize" : fig_config["text_size"], 
        "color": linecolor[1],
    }
}

bar_config3 = {
    "matplot_config" : {
        #'color' : '#A1BA66', 
        'color' : barcolor[2],
        'edgecolor' : linecolor[2],
        'linewidth' : 3, 
        'label' : 'HW',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : hatch_style[2]
    },
    "hatch_config" : {
        'color' : linecolor[2],
        'linewidth' : 2
    },
    "text_config" : {
        "fontsize" : fig_config["text_size"], 
        "color": linecolor[2],
    }
}

configs = [bar_config1, bar_config2, bar_config3]

def draw(): 
    with plt.style.context(styles): 
        x = np.arange(len(labels))  # the label locations
        width = fig_config['bar_width']
        fig, ax = plt.subplots()
        
        bottom = np.zeros(len(labels))
        for i in range(len(datas)):
            y = datas[i]
            bar_config = configs[i]
            set_hatch(**bar_config["hatch_config"])
            bar =  ax.bar(x, y, width, **bar_config["matplot_config"], bottom=bottom)
            bottom += y
            
            #if you want to add text annotation within the bar
            #ax.bar_label(bar, percent_label[i], label_type='center',**bar_config["text_config"])
            #ax.bar_label(bar, y, label_type='center',**bar_config["text_config"])
        
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_ylabel(fig_config['ylabel'])
        ax.set_xlabel(fig_config['xlabel'])
        
        ax.legend()
        
        fig.tight_layout()

        
        fig.tight_layout()
    
        save_figure('bar_percent_example')
        plt.show()
    
if __name__ == '__main__': 
    draw()