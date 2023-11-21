
# -*- coding: UTF-8 -*-
from common import * 
import numpy as np 

## data 

## data end 

styles = get_style_sheet_upon_base("multigraph3.mplstyle")

labels = ['Switch', 'Router', 'Katran', 'BPF-iptables']
base_line1 = np.array([3, 4, 2, 3])
base_line2 = np.array([3, 4, 2, 3])
base_line3 = np.array([3, 4, 2, 3])
base_line4 = np.array([3, 4, 2, 3])
y_1 = np.array([4, 4.5, 3, 3.5])
y_2 = np.array([4, 4.5, 3, 3.5])
y_3 = np.array([4, 4.5, 3, 3.5])
y_4 = np.array([4, 4.5, 3, 3.5])

#all_num = [y_1[i] + y_2[i] + y_3[i] for i in range(labels)]

target_datas = [y_1, y_2, y_3]

#barcolor = ["bisque","honeydew","lightskyblue","mistyrose"]
hatch_style = ['x', '\\', '/']

linecolor = ["#DC625B", "#51B72D", "#DFDFDF"]

fig_config = {
    'xlabel' : '#CPU',   #x轴标签名
    'ylabel' : 'Avg Throughput (Mpps)' , #y轴标签名
    'bar_width' : 0.4, #每一根柱子的宽度
    'text_size' : 19,
    'bar_line_width' : 1,
    'gridspec_kw' : {
        "wspace" : 0
    },
    "xtick_label_conf": {
         "rotation" : 30,
         "ha" : "right",
    },
    "bar_interval" : 0.04,
    "bar_edge": 0.2,
    "legned_conf" : {
        "loc" : "upper left",
        "bbox_to_anchor" : (0.06, 0.93),
        "ncols" : 3,
    },
    "hatch_line_width" : 1
}
bar_config0 = {
    "matplot_config" : {
        #'color' : '#74A9D0', 
        'color' : "white", 
        'edgecolor' : linecolor[2],  #edgecolor will override hatch color 
        'linewidth' : fig_config['bar_line_width'], 
        'label' : 'Baseline',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : '\\\\\\\\\\',
    },
    "hatch_config" : {
        'color' :  linecolor[2],
        'linewidth' : fig_config["hatch_line_width"]
    }
}
bar_config1 = {
    "matplot_config" : {
        #'color' : '#74A9D0', 
        'color' : "white", 
        'edgecolor' : linecolor[0],
        'linewidth' : fig_config['bar_line_width'],
        'label' : 'Morpheus',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : 'xxx'
    },
    "hatch_config" : {
        'color' : linecolor[0],
        'linewidth' : fig_config["hatch_line_width"]
    }
}

bar_config2 = {
    "matplot_config" : {
        #'color' : '#74A9D0', 
        'color' : "white", 
        'edgecolor' : linecolor[1],
        'linewidth' : fig_config['bar_line_width'],
        'label' : 'ESwitch',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : '/////'
    },
    "hatch_config" : {
        'color' : linecolor[1],
        'linewidth' : fig_config["hatch_line_width"]
    }
}

def draw(): 
    with plt.style.context(styles): 
        width = fig_config['bar_width']
        x_tick, _, right_edge = cal_bar_xticks(fig_config["bar_edge"] + width / 2, \
            len(labels), width , interval=fig_config["bar_interval"])
        x = np.array(x_tick)
        fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, sharey=True, gridspec_kw = fig_config['gridspec_kw'])

        set_hatch(**bar_config0["hatch_config"])
        __barcontainer = ax1.bar(x, base_line1, width, **bar_config0["matplot_config"])
        set_bar_edgecolor_to_black(__barcontainer)
        increment = y_1 - base_line1
        set_hatch(**bar_config1["hatch_config"])
        __barcontainer = ax1.bar(x, increment, width, **bar_config1["matplot_config"], bottom = base_line1)
        set_bar_edgecolor_to_black(__barcontainer)
        
        set_hatch(**bar_config0["hatch_config"])
        __barcontainer = ax2.bar(x, base_line2, width, **bar_config0["matplot_config"])
        set_bar_edgecolor_to_black(__barcontainer)
        increment = y_2 - base_line2
        set_hatch(**bar_config1["hatch_config"])
        __barcontainer = ax2.bar(x, increment, width, **bar_config1["matplot_config"], bottom = base_line2)
        set_bar_edgecolor_to_black(__barcontainer)
        
        set_hatch(**bar_config0["hatch_config"])
        __barcontainer = ax3.bar(x, base_line3, width, **bar_config0["matplot_config"])
        set_bar_edgecolor_to_black(__barcontainer)
        increment = y_3 - base_line3
        set_hatch(**bar_config1["hatch_config"])
        __barcontainer = ax3.bar(x, increment, width, **bar_config1["matplot_config"], bottom = base_line3)
        set_bar_edgecolor_to_black(__barcontainer)
        
        set_hatch(**bar_config0["hatch_config"])
        __barcontainer = ax4.bar(x, base_line4, width, **bar_config0["matplot_config"])
        set_bar_edgecolor_to_black(__barcontainer)
        increment = y_3 - base_line4
        set_hatch(**bar_config2["hatch_config"])
        __barcontainer = ax4.bar(x, increment, width, **bar_config2["matplot_config"], bottom = base_line4)
        set_bar_edgecolor_to_black(__barcontainer)
        
        #label in the left edge
        #x_label_tick = x - width/2 
        x_label_tick = x
        
        ax1.set_xlim(0, right_edge + fig_config["bar_edge"])
        ax1.set_xticks(x_label_tick, labels, **fig_config["xtick_label_conf"])
        ax1.set_title("High Locality")
        
        ax2.set_xlim(0, right_edge + fig_config["bar_edge"])
        ax2.set_xticks(x_label_tick, labels, **fig_config["xtick_label_conf"])
        ax2.set_title("Low Locality")
        
        ax3.set_xlim(0, right_edge + fig_config["bar_edge"])
        ax3.set_xticks(x_label_tick, labels, **fig_config["xtick_label_conf"])
        ax3.set_title("No Locality")
        
        ax4.set_xlim(0, right_edge + fig_config["bar_edge"])
        ax4.set_xticks(x_label_tick, labels, **fig_config["xtick_label_conf"])
        ax4.set_title("ESwitch")
        
        bars, bar_labels = fig.axes[0].get_legend_handles_labels()
        __bars, __bar_labels = fig.axes[-1].get_legend_handles_labels()
        bars.append(__bars[-1])
        bar_labels.append(__bar_labels[-1])

        fig.legend(bars, bar_labels, **fig_config["legned_conf"]) # 图例的位置，bbox_to_anchor=(0.5, 0.92),

        ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
        ax1.set_ylabel(fig_config['ylabel'])
        ax1.set_ylim(0, 6)
         
        fig.tight_layout()
        save_figure('multi_bar_example')
        plt.show()
    
if __name__ == '__main__': 
    draw()