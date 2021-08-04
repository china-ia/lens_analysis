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
import pandas as pd
from .constants import *
from .utilities import contains_word, ends_on_word, contains_string
import os

DAT_DIR = os.path.join(os.path.dirname(__file__),"res/applicant_types/")
COMP_TERMS = pd.read_excel(DAT_DIR+"company_types.xlsx", squeeze=True, header=None)
ACAD_TERMS = pd.Series(["UNIV", "CAS", "CAEP", "CN ACAD", "CHINESE ACAD", "CHINA ACAD",
                        "CNRS", "UNIVERSITY", "INST TECHNOLOGY", "INST TECH"])
ACAD_TERMS_NO_SPACES = pd.Series(["大学", "学院", "中科院"])
COMP_TERMS_ANYWHERE = pd.Series(["CO", "LTD", "COMP", "COMPANY", "LIMITED","CORP",
                                 "CORPORATION", "GMBH", "BV", "NV", "SARL", "SRL",])
COMP_TERMS_NO_SPACES = pd.Series(["公司","会社"])

INV_TYPE = "Individual"
COMP_TYPE = "Company"
ACAD_TYPE = "Academia"
UNK_TYPE = "Other / Unknown"

def classify_by_type(row):
    if is_individual(row):
        return INV_TYPE
    if is_company(row):
        return COMP_TYPE
    if is_academia(row):
        return ACAD_TYPE
    else:
        return UNK_TYPE
    
def is_company(row):
    app = row.name
    if not isinstance(app, str):
        return False
    if ends_on_word(app, COMP_TERMS):
        return True
    if contains_word(app, COMP_TERMS_ANYWHERE):
        return True
    if contains_string(app, COMP_TERMS_NO_SPACES):
        return True
    
    return False
    

def is_academia(row):
    app = row.name
    if not isinstance(app, str):
        return False
    if contains_word(app, ACAD_TERMS):
        return True
    if contains_string(app, ACAD_TERMS_NO_SPACES):
        return True
    
    return False
    
def is_individual(row):
    return row[ISINV_COL]
    

    


    
    
    
    