# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:25:32 2021

@author: David
"""
import pandas as pd

from .constants import *

def guess_aliases(app_df, apps, custom_aliases={}):
    """
    merge_apps: dict of key applicant
    with value a list of applicants to be merged

    """
    AL_NAME = "Alias"
    NM_NAME = "Name"
    alias_sr = pd.Series(name=AL_NAME)
    alias_sr.index.name = NM_NAME
    
    for app in apps:
        joint_apps = app_df.loc[app, JPW_COL]
        joint_apps = joint_apps.split(SEP)

        # occurs anywhere inside?
        more_apps = find_extended_form_of_app(remove_common_terms(app),
                                              app_df.index)
        joint_apps += more_apps
        
        # check custom_alias:
        if app in custom_aliases.keys():
            custom_alias = custom_aliases[app]
            app_name = normal_case(custom_alias)
            more_apps = find_extended_form_of_app(custom_alias, app_df.index)
            joint_apps += more_apps
        else:
            app_name = normal_case(app)
        
        joint_apps = sorted(set(joint_apps))
        new_aliases = pd.Series(index=joint_apps, data=app_name,
                                name=AL_NAME)
        new_aliases.index.name = NM_NAME
        
        noverlap_ix = [ix for ix in new_aliases.index if ix not in alias_sr]
        new_aliases = new_aliases.loc[noverlap_ix]
        
        alias_sr = alias_sr.append(new_aliases)
        
    return alias_sr
        
        
def normal_case(s):
    words = s.split(" ")
    for ix, word in enumerate(words):
        if len(word) > 1:
            words[ix] = word[0].upper()+word[1:].lower()
        
    return " ".join(words)

def find_extended_form_of_app(app_to_find, apps):
    return [app for app in apps if app_to_find in app]

def remove_common_terms(app):
    COMMON_TERMS = ["CO", "LTD", "INC", "CORP", "LLC", "BV"]
    app_words = app.split(" ")
    for term in COMMON_TERMS:
        if term in app_words:
            app_words.remove(term)
    return " ".join(app_words)
    
        
        