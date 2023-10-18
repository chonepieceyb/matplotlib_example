
# -*- coding: UTF-8 -*-
from common import * 
import numpy as np 

## data 

## data end 

styles = get_style_sheet_upon_base("multigraph3.mplstyle")

labels = ['#1', '#2', '#3', '#4']
base_line1 = np.array([30, 40, 20, 30])
base_line2 = np.array([30, 40, 20, 30])
base_line3 = np.array([30, 40, 20, 30])
y_1 = np.array([40, 45, 30, 35])
y_2 = np.array([50, 55, 40, 40])
y_3 = np.array([55, 60, 50, 45])

#all_num = [y_1[i] + y_2[i] + y_3[i] for i in range(labels)]

target_datas = [y_1, y_2, y_3]

barcolor = ["bisque","honeydew","lightskyblue","mistyrose"]
linecolor = ["orange","green","blue","red"]
hatch_style = ['x', '\\', '/']

markers = ['o', '*', '^']
linecolor = ["orange","green","blue","red"]

fig_config = {
    'xlabel' : '#CPU',   #x轴标签名
    'ylabel' : 'Time (us)' , #y轴标签名
    'bar_width' : 0.4, #每一根柱子的宽度
    'text_size' : 19,
    'bar_line_width' : 1,
    'gridspec_kw' : {
        "wspace" : 0
    }
}
bar_config0 = {
    "matplot_config" : {
        #'color' : '#74A9D0', 
        'color' : "white", 
        'edgecolor' : "grey",
        'linewidth' : fig_config['bar_line_width'], 
        'label' : 'Base',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : '/////'
    },
    "hatch_config" : {
        'color' :  "grey",
        'linewidth' : 0.5
    },
    "text_config" : {
        "fontsize" : fig_config["text_size"], 
        "color": linecolor[0],
    }
}
bar_config1 = {
    "matplot_config" : {
        #'color' : '#74A9D0', 
        'color' : barcolor[0], 
        'edgecolor' : linecolor[0],
        'linewidth' : fig_config['bar_line_width'],
        'label' : 'Ours',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : 'xxxxx'
    },
    "hatch_config" : {
        'color' : linecolor[0],
        'linewidth' : 0.5
    },
    "text_config" : {
        "fontsize" : fig_config["text_size"], 
        "color": linecolor[0],
    }
}

def draw(): 
    with plt.style.context(styles): 
        x = np.array([1, 1.5, 2, 2.5])  # the label locations
        width = fig_config['bar_width']
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, gridspec_kw = fig_config['gridspec_kw'])
        
        set_hatch(**bar_config0["hatch_config"])
        ax1.bar(x, base_line1, width, **bar_config0["matplot_config"])
        increment = y_1 - base_line1
        set_hatch(**bar_config1["hatch_config"])
        ax1.bar(x, increment, width, **bar_config1["matplot_config"], bottom = base_line1)
        
        set_hatch(**bar_config0["hatch_config"])
        ax2.bar(x, base_line2, width, **bar_config0["matplot_config"])
        increment = y_2 - base_line2
        set_hatch(**bar_config1["hatch_config"])
        ax2.bar(x, increment, width, **bar_config1["matplot_config"], bottom = base_line2)
        
        set_hatch(**bar_config0["hatch_config"])
        ax3.bar(x, base_line3, width, **bar_config0["matplot_config"])
        increment = y_3 - base_line3
        set_hatch(**bar_config1["hatch_config"])
        ax3.bar(x, increment, width, **bar_config1["matplot_config"], bottom = base_line3)
        
        ax1.set_xticks(x)
        ax1.set_xlim(0.5,3)
        ax1.set_xticklabels(labels)
        ax1.set_title("No Locality")
        
        ax2.set_xlim(0.5,3)
        ax2.set_xticks(x)
        ax2.set_xticklabels(labels)
        ax2.set_title("Low Locality")
        
        ax3.set_xlim(0.5,3)
        ax3.set_xticks(x)
        ax3.set_xticklabels(labels)
        ax3.set_title("High Locality")
        
        bars, bar_labels = fig.axes[-1].get_legend_handles_labels()
        fig.legend(bars, bar_labels, loc = 'upper right') # 图例的位置，bbox_to_anchor=(0.5, 0.92),

        fig.tight_layout()
        save_figure('multi_bar_example')
        plt.show()
    
if __name__ == '__main__': 
    draw()