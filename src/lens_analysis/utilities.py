# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:24:43 2021
Utility functions for other modules

There are a few join functions that
are options for collapsing columns into a single value

join_cols is the basic function for collapsing a dataframe into
a series that is used to collapse Lens exports to family dataframes
or family dataframes to applicant dataframes.

@author: David
"""
import pandas as pd
from itertools import chain
from collections import Counter
from .constants import *

def _mode(sample):
     c = Counter(sample)
     return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
 
def join(col):
    return BIG_SEP.join(col.astype(str))

def join_set(col):
    all_vals = col.astype(str).str.split(SEP)
    return SEP.join(set(chain(*all_vals)))

def join_max(col):
    return col.max()

def join_sum(col):
    return col.sum()

def join_mean(col):
    return col.mean()

def join_earliest(col):
    return col.sort_values().iloc[0]

def join_size(col):
    return len(col)

def join_most(col):
    """ 
    Will return value that occurs most often    
    """
    all_vals = col.astype(str).str.split(SEP)
    all_vals = [val for val in chain(*all_vals)]
    mode = _mode(all_vals)
    return SEP.join(mode)

def join_cols(df, func_d):
    """ 
    Compresses a df of a family to a series of the family
    func_d: dictionary of length 2 tuples, first string, second function
        mapping of columns through function to other column
    std_func: function to use when column not in func_d
        will automatically map to same column name
    
    """
    sr = pd.Series()
    for col in df.columns:
        if col in func_d:
            col_out = func_d[col][0]
            func = func_d[col][1]
        else: 
            continue
        sr[col_out] = func(df[col])
    return sr

def contains_word(string, series_of_words):
    """
    Fast method to check if any of a series of words is contained
    exactly in a string
    That is: series_of_words=[ai], string=air pressure will return False, 
    but series_of_words=[ai], str_sr=responsible ai, will return True
    """
    string = " "+string+" "
    series_of_words = " "+series_of_words+" "
    return series_of_words.apply(lambda x: x in string).any()

def contains_string(string, series_of_strings):
    """
    is any of the strings in series of strings contained in string
    """
    return series_of_strings.apply(lambda x: x in string).any()

def ends_on_word(string, series_of_words):
    """
    Fast method to check if a string ends with any in a series of words
    """
    string = " "+string
    series_of_words = " "+series_of_words
    return series_of_words.apply(lambda x: \
                                 x == string[-min(len(string), len(x)):]).any()

    