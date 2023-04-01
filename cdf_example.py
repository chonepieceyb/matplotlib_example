
# -*- coding: UTF-8 -*-
from multiprocessing.connection import wait
from common import * 
import numpy as np 
import pandas as pd 
from data_common import * 
import math 
from functools import partial

FPGA_DATA_PATH = os.path.join(RAW_DATA_PATH, 'wait.csv')

LIN_BIN_NUMS = 10
LOG_BIN_NUMS = 10
LINTHRESH_BASE = 3
MAX_BASE = 6
#TAIL_THRESHOD = 2000


'''
#处理数据部分
#1.读取CSV 
#2.产生桶
#3.计算直方图
#4.计算频率
'''
def load_process_data():
    df  = pd.read_csv(FPGA_DATA_PATH, index_col = False, sep = ",").dropna() 
    wait_time = df["wait_time"].apply(lambda x : x /1e6).values
    #bins = np.linspace(0, math.pow(10, LINTHRESH_BASE), num = LIN_BIN_NUMS, endpoint=False).tolist()
    linbins = np.linspace(0, math.pow(10, LINTHRESH_BASE), num = LIN_BIN_NUMS + 1, endpoint=True).tolist()
    bins = linbins.copy()
    if (len(bins) > 1):
        bins.pop(-1)
    logbins = np.logspace(LINTHRESH_BASE, 6, num = LOG_BIN_NUMS + 1, endpoint=True, base=10.0).tolist()
    bins.extend(logbins)
    hist, bins = np.histogram(wait_time, bins=bins, density = False)
    hist = hist / hist.sum()
    
    return hist, bins, linbins, logbins 

def _gen_log_tick(value, *, start_exp, num_exp, start_index, num_index, base = 10): 
    if num_exp == 0 : 
        return None
    value_exp = math.log(value, base)

    #exp/exp_len = index / index_len
    #index = exp *index_len / exp_len 
    return  start_index + (value_exp - start_exp) * num_index / num_exp 

def _gen_lin_tick(value, *, start_value, end_value, start_index, num_index): 
    #value/value_interval = index / index_len
    #index = value * index_len / value_len
    #[start_value, end_value)
    interval = end_value - start_value 
    if (interval == 0):
        return None 
    return start_index + value * num_index / interval 
    

def _gen_ticks(selected_values, values): 
    #values 递增
    #x_values 递增
    ticks = []
    start = 0
    for v in selected_values: 
        for i in range(start, len(values)):
            if v == values[i]:
                ticks.append(i)
                start = i + 1
                break 
    return ticks 

def _gen_labels(ticks, values): 
    labels = []
    for i in ticks: 
        labels.append(values[i])
    return labels

styles = get_default_bar_style_sheets()
styles.append(os.path.join(STYLE_SHEET_DIR, 'two_cols.mplstyle'))

LIN_BINS = None 
LOG_BINS = None 
BINS = None 
HISTS = None

barcolor = ["orange","honeydew","lightskyblue","mistyrose"]
linecolor = ["#e68a00","green","blue","red"]

fig_config = {
    'ylabel' : 'Probability',   #x轴标签名
    'xlabel' : 'Processing time on FPGA (s)' , #y轴标签名
    'bar_width' : 0.8, #每一根柱子的宽度
}

bar_config1 = {
    "bar_config" : {
        #'color' : '#74A9D0', 
        'color' : barcolor[0], 
        'edgecolor' : linecolor[0],
        'linewidth' : 3, 
        #'label' : 'FPGA',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        #'hatch' : '/'
        'align' : 'edge'
    }
}

def draw(): 
    x_value = range(len(BINS)-1)
    #x_value= BINS.tolist()
    #x_value.pop(-1)

    
    lin_tick_gen = partial(_gen_lin_tick, start_value = LIN_BINS[0], end_value = LIN_BINS[-1], start_index = 0, num_index = len(LIN_BINS) - 1)
    log_tick_gen = partial(_gen_log_tick, start_exp = LINTHRESH_BASE, num_exp = MAX_BASE-LINTHRESH_BASE, start_index = len(LIN_BINS), num_index = len(LOG_BINS) - 1)
    

    xticks = [lin_tick_gen(0), lin_tick_gen(200), lin_tick_gen(500), log_tick_gen(1000), log_tick_gen(1e4), log_tick_gen(1e5), log_tick_gen(1e6)]
    xlabels = ['0','200','500', '1.0E3', '1.0E4','1.0E5', '1.0E6']

    with plt.style.context(styles): 
        fig, ax = plt.subplots()
        ax.bar(x_value, HISTS, fig_config["bar_width"], **bar_config1["bar_config"])
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(fig_config['ylabel'])
        ax.set_xlabel(fig_config['xlabel'])

        ax.set_xlim(0, x_value[-1] +1)
        ax.set_xticks(xticks)
        ax.set_xticklabels(xlabels)
        
        #ax.set_xscale('symlog', linthresh = 1000)
        #ax.xaxis.set_major_locator(mpl.ticker.SymmetricalLogLocator(linthresh = 1000, base = 10))
        fig.tight_layout()
        
        
        save_figure('cdf_example')
        #plt.show()
    
if __name__ == '__main__': 
    HISTS, BINS, LIN_BINS, LOG_BINS= load_process_data()
    draw()