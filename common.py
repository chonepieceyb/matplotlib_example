# -*- coding: UTF-8 -*-
import os 
from matplotlib import pyplot as plt
import matplotlib as mpl
from matplotlib import axes

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
STYLE_SHEET_DIR = os.path.join(ROOT_DIR, 'styles')
DEFAULT_SAVE_DIR = os.path.join(ROOT_DIR, 'images')

DEFAULT_BASE_STYLE = os.path.join(STYLE_SHEET_DIR, 'base.mplstyle')
DEFAULT_HEAP_MAP_STYLE = os.path.join(STYLE_SHEET_DIR, 'heapmap.mplstyle')
DEFAULT_BAR_STYLE = os.path.join(STYLE_SHEET_DIR, 'bargraph.mplstyle')
DEFAULT_LINE_STYLE = os.path.join(STYLE_SHEET_DIR, 'linegraph.mplstyle')

def get_default_heapmap_style_sheets():
    return [DEFAULT_BASE_STYLE, DEFAULT_HEAP_MAP_STYLE]

def get_default_bar_style_sheets():
    return [DEFAULT_BASE_STYLE, DEFAULT_BAR_STYLE]

def get_default_line_style_sheets():
    return [DEFAULT_BASE_STYLE, DEFAULT_LINE_STYLE]

def get_style_sheet_upon_base(style):
    return [DEFAULT_BASE_STYLE, os.path.join(STYLE_SHEET_DIR, style)]


def cal_bar_offset(index, num, width, align_mode = "center"): 
    '''
        calculate offset to x of groub bars
        @param: 
            index: index of the bar start with 0
            num: the number of bars in group 
            width: witdth of each bar(should be the same)
        @return: 
            return offset 
    '''
    assert align_mode in ['center'] and "unsupported align mode %s"%align_mode 
    return (2*index + 1 - num)*width / 2

def save_figure(name):
    if not os.path.exists(DEFAULT_SAVE_DIR):
        os.mkdir(DEFAULT_SAVE_DIR)
    plt.savefig(os.path.join(DEFAULT_SAVE_DIR, name))
    
def set_hatch(*, color, linewidth): 
    plt.rcParams["hatch.color"] = color
    plt.rcParams["hatch.linewidth"] = linewidth