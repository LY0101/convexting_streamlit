# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 12:00:24 2021

@author: yang
"""


import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

var_matrix_inputs_complete = pd.read_excel('source_variables.xls', sheet_name="Inputs")  
var_matrix_badges_complete = pd.read_excel('source_variables.xls', sheet_name="Badges")  
var_matrix_strategies_complete = pd.read_excel('source_variables.xls', sheet_name="Strategies")  


    
#badge_pull_from_input("mortgage_credit_morethan650")
