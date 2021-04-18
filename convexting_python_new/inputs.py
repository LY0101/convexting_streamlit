# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:21:24 2021

@author: yang
"""
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np



var_matrix_inputs_complete = pd.read_excel('source_variables.xls', sheet_name="Inputs")  
var_matrix_badges_complete = pd.read_excel('source_variables.xls', sheet_name="Badges")  
var_matrix_strategies_complete = pd.read_excel('source_variables.xls', sheet_name="Strategies")  


########################################################
### SECTION 3: Badges#####################
########################################################

# var_matrix_badges_mortgage = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Mortgage"].dropna()
# var_list_badges_mortgage_name_only_list = list(var_matrix_badges_mortgage['badge_name_full'])
# var_list_badges_mortgage_name_only_df=var_matrix_badges_mortgage['badge_name_full']


# Foundation
badge_df1 = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Foundation"].dropna()[['badge_variable', 'badge_name_full',  'url']]

# Resource
badge_df2 = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Resource"].dropna()[['badge_variable', 'badge_name_full',  'url']]

# Analysis
badge_df3 = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Analysis"].dropna()[['badge_variable', 'badge_name_full',  'url']]

# Buying
badge_df4 = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Buying"].dropna()[['badge_variable', 'badge_name_full',  'url']]

# Mortgage
badge_df5 = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Mortgage"].dropna()[['badge_variable', 'badge_name_full',  'url']]

# Tax
badge_df6 = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Tax"].dropna()[['badge_variable', 'badge_name_full',  'url']]

# Value-add
badge_df7 = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Value-add"].dropna()[['badge_variable', 'badge_name_full',  'url']]

# Property Management
badge_df8 = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Property Management"].dropna()[['badge_variable', 'badge_name_full',  'url']]

# Legal
badge_df9 = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Legal"].dropna()[['badge_variable', 'badge_name_full',  'url']]

# Selling
badge_df10 = var_matrix_badges_complete[var_matrix_badges_complete["budget_category"]=="Selling"].dropna()[['badge_variable', 'badge_name_full',  'url']]


########################################################
### SECTION 4: Strategies#####################
########################################################
# Foundation
stra_df1 = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Foundation"].dropna()[['strategy_variable', 'strategy_name_full',  'url']]

# Resource
stra_df2 = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Resource"].dropna()[['strategy_variable', 'strategy_name_full',  'url']]

# Analysis
stra_df3 = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Analysis"].dropna()[['strategy_variable', 'strategy_name_full',  'url']]

# Buying
stra_df4 = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Buying"].dropna()[['strategy_variable', 'strategy_name_full',  'url']]

# Mortgage
stra_df5 = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Mortgage"].dropna()[['strategy_variable', 'strategy_name_full',  'url']]

# Tax
stra_df6 = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Tax"].dropna()[['strategy_variable', 'strategy_name_full',  'url']]

# Value-add
stra_df7 = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Value-add"].dropna()[['strategy_variable', 'strategy_name_full',  'url']]

# Property Management
stra_df8 = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Property Management"].dropna()[['strategy_variable', 'strategy_name_full',  'url']]

# Legal
stra_df9 = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Legal"].dropna()[['strategy_variable', 'strategy_name_full',  'url']]

# Selling
stra_df10 = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Selling"].dropna()[['strategy_variable', 'strategy_name_full',  'url']]

# var_matrix_strategies_mortgage = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Mortgage"].dropna()
# var_matrix_strategies_mortgage_df = var_matrix_strategies_mortgage['strategy_name_full']
# var_matrix_strategies_mortgage_list = list(var_matrix_strategies_mortgage['strategy_name_full'])


# var_matrix_strategies_tax = var_matrix_strategies_complete[var_matrix_strategies_complete["strategy_category"]=="Tax"].dropna()
# var_matrix_strategies_tax_df = var_matrix_strategies_tax['strategy_name_full']
# var_list_strategies_tax_name_only = list(var_matrix_strategies_tax['strategy_name_full'])

