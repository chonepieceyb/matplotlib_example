
# -*- coding: UTF-8 -*-
from common import * 
import numpy as np 

## data 
feature_lens = [256 ,512 ,1024 , 2048 ,4096 ,8192]

FPGA = [66289, 1167180, 4087332, 10869780, 16307037, 30144267]
HF = [8329800, 2.03e8, 525000000, 1241470400, 2710000000, 4900000000]
MC = [525872, 28290300, 29186100, 33850900, 48000000, 75000000]

speed_hf = [125.6588574, 174.1685087, 128.4456462, 114.21302, 166.1859233, 162.5516388]
speed_mc = [7.933020561, 24.23816378, 7.140623761, 3.114221263, 3, 2.5]
## data end 

styles = get_default_bar_style_sheets()

labels = feature_lens
y_1 = FPGA
y_2 = MC
y_3 = HF

l_1 = speed_mc 
l_2 = speed_hf

barcolor = ["bisque","honeydew","lightskyblue","mistyrose"]
linecolor = ["orange","green","blue","red"]
hatch_style = ['x', '+', '/']

markers = ['o', '*', '^']
linecolor = ["orange","green","blue","red"]

fig_config = {
    'xlabel' : 'Feature length',   #x轴标签名
    'ylabel' : 'Latency (us)' , #y轴标签名
    'ylabel2' : 'Speedup',
    'bar_width' : 0.24, #每一根柱子的宽度
}

bar_config1 = {
    "matplot_config" : {
        #'color' : '#74A9D0', 
        'color' : barcolor[0], 
        'edgecolor' : linecolor[0],
        'linewidth' : 3, 
        'label' : 'FPGA',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : '/'
    },
    "hatch_config" : {
        'color' : linecolor[0],
        'linewidth' : 2
    }
}

bar_config2 = {
    "matplot_config" : {
        #'color' : '#A1BA66', 
        'color' : barcolor[1],
        'edgecolor' : linecolor[1],
        'linewidth' : 3, 
        'label' : 'MCA',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : 'x'
    },
    "hatch_config" : {
        'color' : linecolor[1],
        'linewidth' : 2
    }
}

bar_config3 = {
    "matplot_config" : {
        #'color' : '#A1BA66', 
        'color' : barcolor[2],
        'edgecolor' : linecolor[2],
        'linewidth' : 3, 
        'label' : 'HF',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : 'x'
    },
    "hatch_config" : {
        'color' : linecolor[2],
        'linewidth' : 2
    }
}

line_config1 = {
    'matplot_config' : {
        'color' : linecolor[1], 
        'linewidth' : 3, 
        'label' : 'Speedup over MCA',  
        'marker' : markers[0], 
        'markersize' : 15,
        'linestyle' : '-'
    }
}

line_config2 = {
    'matplot_config' : {
        'color' : linecolor[2], 
        'linewidth' : 3, 
        'label' : 'Speedup over HF',  
        'marker' : markers[1], 
        'markersize' : 15,
        'linestyle' : '-'
    }
}


def draw(): 
    with plt.style.context(styles): 
        x = np.arange(len(labels))  # the label locations
        width = fig_config['bar_width']
        
        fig, ax = plt.subplots()
        
        set_hatch(**bar_config1["hatch_config"])
        bar1 = ax.bar(x + cal_bar_offset(0, 3, width), y_1, width, **bar_config1["matplot_config"])
        set_hatch(**bar_config2["hatch_config"])
        bar2 = ax.bar(x + cal_bar_offset(1, 3, width), y_2, width, **bar_config2["matplot_config"])
        set_hatch(**bar_config3["hatch_config"])
        bar3 = ax.bar(x + cal_bar_offset(2, 3, width), y_3, width, **bar_config3["matplot_config"])
        
        # Add some text for labels, title and custom x-axis tick labels, etc.
        #ax.set_ylim(1, 1e12)
        ax.set_yscale('log', base = 10, subs = [10])
        ax.set_ylabel(fig_config['ylabel'])
        ax.set_xlabel(fig_config['xlabel'])
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
    
        


        ax2 = ax.twinx()
        line1 = ax2.plot(x + cal_bar_offset(1, 3, width), l_1, **line_config1["matplot_config"])
        line2 = ax2.plot(x + cal_bar_offset(2, 3, width), l_2, **line_config2["matplot_config"])
        
        ax2.set_ylim(1, 1000)
        ax2.set_yscale('log', base = 10, subs = [10])
        ax2.set_ylabel(fig_config['ylabel2'])

        ax2.grid(False)
        
        lines = line1 + line2
        bars = [bar1, bar2, bar3]
        
        
        #在一个图层上展示 图例
        #分开zhanshi 
        
        l1 = plt.legend(bars, [b.get_label() for b in bars], loc = "upper left", framealpha = 0.6)
        l2 = plt.legend(lines, [l.get_label() for l in lines],loc = "upper right", framealpha = 0.6)
        plt.gca().add_artist(l1)
        
        fig.tight_layout()

        save_figure('bar_line_example')
    
if __name__ == '__main__': 
    draw()