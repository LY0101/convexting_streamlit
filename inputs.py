# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:21:24 2021

@author: yang
"""
import streamlit as st
import pandas as pd



var_matrix_inputs_complete = pd.read_excel('source_variables.xls', sheet_name="Inputs")  
var_matrix_badges_complete = pd.read_excel('source_variables.xls', sheet_name="Badges")  
var_matrix_strategies_complete = pd.read_excel('source_variables.xls', sheet_name="Strategies")  


########################################################
### SECTION 3: Badges#####################
########################################################

# var_matrix_badges_mortgage = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Mortgage"].dropna()
# var_list_badges_mortgage_name_only_list = list(var_matrix_badges_mortgage['badge_name_full'])
# var_list_badges_mortgage_name_only_df=var_matrix_badges_mortgage['badge_name_full']

def badge_df(cat, sort_by_impact=False):
    temp_df = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]==cat].dropna()[['badge_variable', 'badge_name_full',  'url', 'impact']]
    if sort_by_impact is False:
        return temp_df
    else:
        return temp_df.sort_values(by='impact', ascending=False)
# Foundation
badge_df1 = badge_df("Foundation")

# Resource
badge_df2 = badge_df("Resource")

# Analysis
badge_df3 = badge_df("Analysis")

# Buying
badge_df4 = badge_df("Buying")

# Mortgage
badge_df5 = badge_df("Mortgage")

# Tax
badge_df6 = badge_df("Tax")

# Value-add
badge_df7 = badge_df("Value-add")

# Property Management
badge_df8 = badge_df("Property Management")

# Legal
badge_df9 = badge_df("Legal")

# Selling
badge_df10 = badge_df("Selling")


########################################################
### SECTION 4: Strategies#####################
########################################################
def stra_df(cat, sort_by_impact=False):
    temp_df = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]==cat].dropna()[['strategy_variable', 'strategy_name_full',  'url', 'Type', 'impact']]
    if sort_by_impact is False:
        return temp_df
    else:
        return temp_df.sort_values(by='impact', ascending=False)


# var_matrix_strategies_mortgage = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Mortgage"].dropna()
# var_matrix_strategies_mortgage_df = var_matrix_strategies_mortgage['strategy_name_full']
# var_matrix_strategies_mortgage_list = list(var_matrix_strategies_mortgage['strategy_name_full'])


# var_matrix_strategies_tax = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Tax"].dropna()
# var_matrix_strategies_tax_df = var_matrix_strategies_tax['strategy_name_full']
# var_list_strategies_tax_name_only = list(var_matrix_strategies_tax['strategy_name_full'])

