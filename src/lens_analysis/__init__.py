# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:17:35 2021

@author: David
"""

from .applicants import merge_to_applicants, alias_apps
from .families import merge_to_family
from .countries import is_cn, is_nl, CN_CTY, CN_PRV, CN_APPS, CN_ACAD, CN_TERMS
from .citations import calc_mncs
from .market_cov import calc_mark_cov
from .countries import is_eu, is_nl, is_cn, is_us, is_not_cn, app_in_list
from .countries import classify_by_country
from .applicant_type import classify_by_type
from .applicant_type import is_company, is_individual, is_academia
from .statistics import split_by_funcs, split_by_func
from .statistics import get_amounts_per_year, get_top_amounts
from .applicant_disambiguation import guess_aliases