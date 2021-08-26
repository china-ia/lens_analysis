# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:46:57 2021
Constants used in the rest of the modules
@author: David
"""
import os
import pandas as pd

# separators
SEPARATOR = ";;"
BIG_SEPARATOR = ";,;,"

# export column names:
POUND_COL = "#"
JURISDICTION_COL = "Jurisdiction"
KIND_COL = "Kind"
PUBLICATION_NUMBER_COL = "Display Key"
LENS_ID_COL = "Lens ID"
PUBLICATION_DATE_COL = "Publication Date"
PUBLICATION_YEAR_COL = "Publication Year"
APPLICATION_NUMBER_COL = "Application Number"
APPLICATION_DATE_COL = "Application Date"
PRIORITY_NUMBERS_COL = "Priority Numbers"
EARLIEST_PRIORITY_DATE_COL = "Earliest Priority Date"
TITLE_COL = "Title"
ABSTRACT_COL = "Abstract"
APPLICANTS_COL = "Applicants"
INVENTORS_COL = "Inventors"
OWNERS_COL = "Owners"
URL_COL = "URL"
DOCUMENT_TYPE_COL = "Document Type"
HAS_FULL_TEXT_COL = "Has Full Text"
CITES_PATENT_COUNT_COL = "Cites Patent Count"
CITED_PATENT_COUNT_COL = "Cited by Patent Count"
SIMPLE_FAMILY_SIZE_COL = "Simple Family Size"
EXTENDED_FAMILY_SIZE_COL = "Extended Family Size"
SEQUENCE_COUNT_COL = "Sequence Count"
CPC_CLASSIFICATIONS_COL = "CPC Classifications"
IPCR_CLASSIFICATIONS_COL = "IPCR Classifications"
US_CLASSIFICATIONS_COL = "US Classifications"
CITED_NPL_COUNT_COL = "NPL Citation Count"
RESOLVED_CITED_NPL_COUNT_COL = "NPL Resolved Citation Count"
RESOLVED_CITED_NPL_LENS_IDS_COL = "NPL Resolved Lens ID(s)"
RESOLVED_CITED_NPL_EXTERNAL_IDS_COL = "NPL Resolved External ID(s)"
NPL_CITATIONS_COL = "NPL Citations"

# fixed export entries
GRANTED_PATENT_ENTRY = "Granted Patent"
WO_JURISDICTION = "WO"
US_JURISDICTION = "US"
NL_JURISDICTION = "NL"
CN_JURISDICTION = "CN"
EU_JURISDICTIONS = \
    ["AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "EP", "ES", "EU", "FI", 
    "FR", "GR", "HR", "HU", "IE", "IT", "LT", "LU", "LV", "MT", "NL", 
    "PL", "PT", "RO", "SE", "SI", "SK", "EU"]
REST_OF_WORLD_JURISDICTIONS = \
    ["AD", "AE", "AF", "AG", "AL", "AM", "AO", "AP", "AR", "AU",
    "AZ", "BA", "BB", "BD", "BF", "BH", "BI", "BJ", "BN", "BO", 
    "BR", "BS", "BT", "BW", "BY" "BZ", "CA", "CD", "CF", "CG", 
    "CH", "CI", "CK", "CL", "CM", "CO", "CR", "CU", "CV", "DJ", 
    "DM", "DO", "DZ", "EC", "EG", "ER", "ET", "FI", "FM", "GA", 
    "GB", "GD", "GE", "GH", "GM", "GN", "GQ", "GT", "GW", "GY", 
    "HK", "HN", "HT", "ID", "IL", "IN", "IQ", "IR", "IS", "JM", 
    "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", 
    "KW", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS",
    "LY","MA","MC","MD","ME","MG","MH","ML","MM","MN","MO","MR",
    "MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NO","NP",
    "NR","NZ","OA","OM","PA","PE","PG","PH","PK","PW","PY","QA",
    "RS","RU","RW","SA","SB","SC","SD","SG","SL","SM","SN","SO",
    "SR","ST","SV","SY","SZ","TD","TG","TH","TJ","TL","TM","TN",
    "TO","TP","TR","TT","TV","TZ","UA","UG","UY","UZ","VA","VC",
    "VE","VN","VU","WS","YE","ZA","ZM","ZW"]



# families self-defined column names
JURISDICTIONS_COL = "Jurisdictions"
KINDS_COL = "Kinds"
GRANTED_JURISDICTIONS_COL = "Granted Jurisdictions"
PUBLICATION_NUMBERS_COL = "Publication Numbers"
LENS_IDS_COL = "Lens IDs"
EARLIEST_PUBLICATION_DATE_COL = "Earliest Publication Date"
EARLIEST_PUBLICATION_YEAR_COL = "Earliest Publication Year"
APPLICATION_NUMBERS_COL = "Application Numbers"
EARLIEST_APPLICATION_DATE_COL = "Earliest Application Date"
SORTED_PRIORITY_NUMBERS_COL = "Sorted Priority Numbers"
EARLIEST_PRIORITY_YEAR_COL = "Earliest Priority Year"
TITLES_COL = "Titles"
FIRST_ABSTRACT_COL = "First Abstract"
URLS_COL = "URLs"
DOCUMENT_TYPES_COL = "Document Types"
IS_GRANTED_COL = "Has Granted Family Member"
FAMILY_CITES_PATENT_COUNT_COL = "Total Cites Patent Count of Family"
FAMILY_CITED_PATENT_COUNT_COL = "Total Cited by Patent Count of Family"
INCLUDED_SIMPLE_FAMILY_SIZE_COL = "Simple Family Size in Original Lens Export"
WEIGHT_PER_APPLICANT_COL = "Weight per Applicant"
MARKET_COVERAGE_COL = "Market Coverage"
PATENT_POWER_COL = "Patent Power"
IS_TOP_PATENT_COL = "Is Top Patent"
PRIORITY_JURISDICTIONS_COL = "Priority Jurisdictions"
CITATION_SCORE_COL = "Citation Score"
APPLICANT_IN_INVENTORS_COL = "Applicant in Inventors"

# applicant self-defined column names
FRACTIONAL_COL_EXTENSION = " (Fractionally Counted)"
APPLICANT_COL = "Applicant"
ALIASED_APPLICANT_COL = "Standardized Applicant Name"
FAMILIES_COUNT_COL = "Number of Simple Patent Families"
FRACTIONAL_FAMILIES_COUNT_COL = FAMILIES_COUNT_COL+FRACTIONAL_COL_EXTENSION
MAIN_JURISDICTION_COL = "Main Jurisdiction"
MAIN_PRIORITY_JURISDICTION_COL = "Main Priority Jurisdiction"
MEAN_CITATION_SCORE_COL = "Mean Citation Score"
MEAN_MARKET_COVERAGE_COL = "Mean Market Coverage"
MEAN_PATENT_POWER_COL = "Mean Patent Power"
TOP_PATENTS_COL = "Top Patents"
FRACTIONAL_TOP_PATENTS_COL = TOP_PATENTS_COL+FRACTIONAL_COL_EXTENSION
HAS_CITATION_SCORE_NUMBER_COL = "Number of Patents with Citation Score"
FRACTIONAL_HAS_CITATION_SCORE_NUMBER_COL = HAS_CITATION_SCORE_NUMBER_COL+FRACTIONAL_COL_EXTENSION
IS_INVENTOR_COL = "Is Inventor"
JOINT_PATENTS_WITH_COL = "Joint Patents With"

# data to determine country of origin / company types
COMPANY_TYPES_DIR = os.path.join(os.path.dirname(__file__),"res/company_types/")
AMERICAN_ACADEMIA_FILENAME = COMPANY_TYPES_DIR+"american-academia.xlsx"
AMERICAN_COMPANIES_FILENAME = COMPANY_TYPES_DIR+"american-companies.xlsx"
AMERICAN_GEOGRAPHICAL_TERMS_FILENAME = COMPANY_TYPES_DIR+"american-geographical-terms.xlsx"
CHINESE_ACADEMIA_FILENAME = COMPANY_TYPES_DIR+"chinese-academia.xlsx"
CHINESE_COMPANIES_FILENAME = COMPANY_TYPES_DIR+"chinese-companies.xlsx"
CHINESE_GEOGRAPHICAL_TERMS_FILENAME = COMPANY_TYPES_DIR+"chinese-geographical-terms.xlsx"
CHINESE_CITIES_FILENAME = COMPANY_TYPES_DIR+"chinese-cities.xlsx"
CHINESE_PROVINCES_FILENAME = COMPANY_TYPES_DIR+"chinese-provinces.xlsx"
EU_ACADEMIA_FILENAME = COMPANY_TYPES_DIR+"european-academia.xlsx"
EU_COMPANIES_FILENAME = COMPANY_TYPES_DIR+"european-companies.xlsx"
EU_CITIES_FILENAME = COMPANY_TYPES_DIR+"european-cities.xlsx"
EU_COUNTRY_NAMES_FILENAME = COMPANY_TYPES_DIR+"european-country-names.xlsx"
EU_COMPANY_FORMS_FILENAME = COMPANY_TYPES_DIR+"european-company-forms.xlsx"
NETHERLANDS_APPLICANTS_FILENAME = COMPANY_TYPES_DIR+"netherlands-applicants.xlsx"
NETHERLANDS_TAX_EVADERS_FILENAME = COMPANY_TYPES_DIR+"netherlands-tax-evaders.xlsx"
NETHERLANDS_TERMS_FILENAME = COMPANY_TYPES_DIR+"netherlands-terms.xlsx"
REST_OF_WORLD_ACADEMIA_FILENAME = COMPANY_TYPES_DIR+"rest-of-world-academia.xlsx"
REST_OF_WORLD_COMPANIES_FILENAME = COMPANY_TYPES_DIR+"rest-of-world-companies.xlsx"
REST_OF_WORLD_COMPANY_FORMS_FILENAME = COMPANY_TYPES_DIR+"rest-of-world-company-forms.xlsx"
ALL_COMPANY_FORMS_FILENAME = COMPANY_TYPES_DIR+"all-company-forms.xlsx"
ALL_ACADEMIA_TERMS_FILENAME = COMPANY_TYPES_DIR+"all-academia-terms.xlsx"
CHINESE_GEOGRAPHICAL_FILENAMES = [CHINESE_CITIES_FILENAME, CHINESE_GEOGRAPHICAL_TERMS_FILENAME, CHINESE_PROVINCES_FILENAME]
EU_GEOGRAPHICAL_FILENAMES = [EU_CITIES_FILENAME, EU_COUNTRY_NAMES_FILENAME]

# applicant types
COUNTRY_OF_ORIGIN_COL = "Country of Origin"
LEGAL_TYPE_COL = "Applicant Legal Type"
APPLICANT_LABEL_COL = "Applicant Type"

ACADEMIA_LABEL = "Academia"
COMPANY_LABEL = "Company"
INDIVIDUAL_LABEL = "Individual"
UNKNOWN_LABEL = "Unknown"
CHINESE_LABEL = "Chinese"
AMERICAN_LABEL = "American"
EU_LABEL = "EU-27"
NETHERLANDS_LABEL = "Dutch"
REST_OF_WORLD_LABEL = "Rest of World"



