# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:47:00 2021

@author: David

Calculate statistics from Applicant data.
"""
from collections import OrderedDict

from .constants import *

def get_amounts_per_year(app_df):
    year_cols = [col for col in app_df if \
                 (all([c in '1234567890' for c in col[:4]]) and \
                  FRAC_EXT in col)]
    amounts = app_df.sum()[year_cols]
    amounts.index = [int(ix[:4]) for ix in amounts.index]
    amounts.name = "Patent Families "+FRAC_EXT
    return amounts

def get_top_amounts(app_df, count_frac=True):
    if count_frac:
        top_pats = app_df[TOPP_FRAC_COL]
    else:
        top_pats = app_df[TOP_PAT_COL]
    top_amounts = top_pats.sum()
    return top_amounts


def split_by_funcs(app_df, by:OrderedDict,
             no_overlap=True):
    """
    Split an applicant dataframe by a number of functions

    'by' is an OrderedDict with keys the label for the split sub-group
    and value the function that returns a True or False per row.
    
    if no_overlap = True each row will only be assigned to a single
    split sub-group, and the order of the 'by' keys matters.
    """
    app_df_dict = {}
    for label in by.keys():
        split_func = by[label]
        mask = app_df.apply(split_func, axis=1)
        
        app_df_sub = app_df.loc[mask]
        app_df_dict[label] = app_df_sub
        
        if no_overlap:
            app_df = app_df.loc[~mask]
    
    return app_df_dict

def split_by_func(app_df, split_func):
    """
    Split an applicant dataframe by a single function
    
    'by' should be a function which returns a string per row.
    """
    labels = app_df.apply(split_func, axis=1)

    return {label:app_df.loc[labels == label] for label in labels.unique()}

        


