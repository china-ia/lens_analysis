# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:24:43 2021

Functionality for retrieving the country of origin of an applicant.
This only works for China and the Netherlands

Main functions:
    - is_cn() takes a row from a applicant dataframe
    and returns True if most likely belongs to a Chinese applicant.
    Works on the basis of placenames, known applicants and other identifiers,
    as well as main priority jurisdiction
    - is_nl() does the same for Dutch applicants
    Note that a number of companies have been removed
    that are only classified as Dutch by the Epodoc classification 
    since they are registered in NL for tax evasion purposes, 
    but don't actually do their main R&D there, such as
    Schlumberger, Nike, Sabic.
    - is_eu() works on the basis of placenames, main priority jurisdiction
    - is_us() works on the basis of main priority jurisdiction

@author: David
"""
import os
from collections import OrderedDict

import pandas as pd

from .constants import *
from .utilities import contains_word, ends_on_word


DAT_DIR = os.path.join(os.path.dirname(__file__),"res/countries/")
CN_CTY = pd.read_excel(DAT_DIR+"cn-cities.xlsx", squeeze=True, header=None)
CN_PRV = pd.read_excel(DAT_DIR+"cn-provinces.xlsx", squeeze=True, header=None)
CN_APPS = pd.read_excel(DAT_DIR+"cn-apps.xlsx", squeeze=True, header=None)
CN_ACAD = pd.read_excel(DAT_DIR+"cn-acads.xlsx", squeeze=True, header=None)
CN_TERMS = pd.read_excel(DAT_DIR+"cn-terms.xlsx", squeeze=True, header=None)

NL_APPS = pd.read_excel(DAT_DIR+"nl-apps.xlsx", squeeze=True, header=None)
NL_TERMS = pd.read_excel(DAT_DIR+"nl-terms.xlsx", squeeze=True, header=None)
NL_TAX_EVADERS = pd.read_excel(DAT_DIR+"nl-tax-evaders.xlsx", squeeze=True, header=None)

EU_JURS = ["AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "ES", "EU", "FI", 
           "FR", "GR", "HR", "HU", "IE", "IT", "LT", "LU", "LV", "MT", "NL", 
           "PL", "PT", "RO", "SE", "SI", "SK"]

EU_TERMS = pd.read_excel(DAT_DIR+"eu-terms.xlsx", squeeze=True, header=None)
EU_COMPS = pd.read_excel(DAT_DIR+"eu-companies.xlsx", squeeze=True, header=None)
EU_COMP_TERMS = pd.read_excel(DAT_DIR+"eu-company-forms.xlsx", squeeze=True, 
                              header=None)


EU_NAME = "EU-27"
CN_NAME = "China"
NL_NAME = "Netherlands"
US_NAME = "US"
ROW_NAME = "Rest of World"
UNK_NAME = "Unknown"

def app_in_list(row, l=[]):
    app = row.name
    if not isinstance(app, str):
        return False
    
    return app in l

def is_cn(row):
    app = row.name
    
    if not isinstance(app, str):
        return False
    if app in CN_APPS.values:
        return True
    if app in CN_ACAD.values:
        return True  
    if contains_word(app, CN_PRV):
        return True
    if contains_word(app, CN_CTY):
        return True
    if contains_word(app, CN_TERMS):
        return True
    
    if not isinstance(row[MJUR_COL],str):
        return False
    if "CN" == row[MJUR_COL]:
        return True
    if "CN" in row[MJUR_COL] and "WO" in row[MJUR_COL] \
        and row[MJUR_COL].count(SEP) <= 1:
        return True
    
    return False

def is_not_cn(row):
    return not is_cn(row)
    
def is_nl(row):
    app = row.name
    if not isinstance(app, str):
        return False
    if app in NL_TAX_EVADERS.values:
        return False
    if app in NL_APPS.values:
        return True
    if contains_word(app, NL_TERMS):
        return True

    if not isinstance(row[MJUR_COL],str):
        return False
    if "NL" in row[MJUR_COL]:
        return True
    
    return False
    
def is_eu(row):
    app = row.name
    
    if not isinstance(app, str):
        return False
    if contains_word(app, EU_TERMS):
        return True
    if contains_word(app, EU_COMPS):
        return True 
    if ends_on_word(app, EU_COMP_TERMS):
        return True
    
    if not isinstance(row[MJUR_COL],str):
        return False
    for eu_jur in EU_JURS:
        if eu_jur in row[MJUR_COL]:
            return True
    
    return False
        
def is_us(row):
    app = row.name
    if not isinstance(app, str):
        return False
    
    if not isinstance(row[MJUR_COL],str):
        return False
    if "US" == row[MJUR_COL]:
        return True
    if "US" in row[MJUR_COL] and "WO" in row[MJUR_COL] \
        and row[MJUR_COL].count(SEP) <= 1:
        return True

    return False

def classify_by_country(row,
                        by=OrderedDict([(EU_NAME,is_eu),
                                        (CN_NAME,is_cn),
                                        (US_NAME,is_us)]),
                        unk_name=UNK_NAME):
    """
    Classifies a row to a single country of origin with
    order specified by OrderedDict 'by'
    """
    for country in by.keys():
        is_country = by[country]
        if is_country(row):
            return country
    # else
    return unk_name
    


    
    
    
    