# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:15:12 2021

@author: yang
"""
import streamlit as st
import pandas as pd
from operator import lt, le, eq, ne, ge, gt

#from inputs import var_list_badges_tax
#from inputs import var_list_badges_tax_df
from inputs import *

var_matrix_inputs_complete = pd.read_excel('source_variables.xls', sheet_name="Inputs")  
var_matrix_badges_complete = pd.read_excel('source_variables.xls', sheet_name="Badges")  
var_matrix_strategies_complete = pd.read_excel('source_variables.xls', sheet_name="Strategies")  


#Page Setup
st.set_page_config( layout='wide')
st.title('Convexting: Personalized Real Estate Investing Guide')
st.write("") # see *
st.write("") # see *


#font 
st.markdown("""
<style>
.instructions{
    font-size:14px !important;
}
</style>
""", unsafe_allow_html=True)


########################################################
### SECTION 1: Step 1, Infof Input #####################
########################################################
###Sidebar variables
st.sidebar.title("Step One: Input Info")
expander_sb = st.sidebar.beta_expander("Instructions")
expander_sb.markdown("<b>Three easy steps to generate personalized strategies!</b> ",unsafe_allow_html=True)
expander_sb.markdown('<p class="instructions"><b>1.Inputs:</b> punch in your personal stats to see which badges you qualify for!</p>', unsafe_allow_html=True)
expander_sb.markdown('<p class="instructions"><b>2.Badges:</b> collect badges (directly or through inputs) to unlock more strategies! </p>', unsafe_allow_html=True)
expander_sb.markdown('<p class="instructions"><b>3.Strategies:</b> based on your badges, these strategies likely suit you best!</p>', unsafe_allow_html=True)



col1_badges, col2_strategies = st.beta_columns((1,2))


### primary inputs
sidebar_expander_inputs_1 = st.sidebar.beta_expander("*Most Important Inputs!")
user_input_occupancy_type =         sidebar_expander_inputs_1.multiselect('1. Occupancy Type', ["Primary Residence","Investment Property","House Hacking","Repair and Renovation"])
user_input_income =                 sidebar_expander_inputs_1.slider('2. Income ($000, Annual Pre-tax Income)', min_value=0, max_value=500, value=100)
user_input_credit_score =           sidebar_expander_inputs_1.slider('3. Credit Score', min_value=500, max_value=850, value=700)
user_input_capital_for_down =       sidebar_expander_inputs_1.slider('4. Money for Down Payment ($000)', min_value=0, max_value=300, value=50)


sidebar_expander_inputs_5 = st.sidebar.beta_expander("Real Estate")
user_input_re_type =          sidebar_expander_inputs_5.multiselect('1. Which of the following  do you own?', ["Primary Residence","Second Home", "Investment Property","House Hacking Property","Value-add Property"])
user_input_re_num =           sidebar_expander_inputs_5.number_input('2. How many properties do you own?', value=0, step=1)
user_input_re_value =         sidebar_expander_inputs_5.number_input('3. Market value of all real estate assets?', value=0, step=10000)
user_input_re_mortgage =      sidebar_expander_inputs_5.number_input('4. Amount of mortgage debt outstanding?', value=0, step=10000)


sidebar_expander_inputs_2 = st.sidebar.beta_expander("Personal")
user_input_personal_zipcode =       sidebar_expander_inputs_2.number_input('1. Zip Code of Intended Purchase', value=90210)
user_input__personal_complexity =   sidebar_expander_inputs_2.slider('2. Complexity (e.g. 5 = can handle highly complex tasks)',min_value=1, max_value=5, value=3, step=1)
user_input__personal_effort =       sidebar_expander_inputs_2.slider('3. Effort (e.g. 5 = willing to put in a ton of effort)',min_value=1, max_value=5, value=3, step=1)


sidebar_expander_inputs_3 = st.sidebar.beta_expander("Income")
user_input_income_type =            sidebar_expander_inputs_3.selectbox('1. Main Income Type', ["W2","1099","Both", "To Be Determined"])
user_input_income_lvl=              sidebar_expander_inputs_3.slider('2. Relative Income Level (e.g. 5 = very high vs location)',min_value=1, max_value=5, value=3, step=1)
user_input_income_stability=        sidebar_expander_inputs_3.slider('3. Income Stability (e.g. 5 = very stable)',min_value=1, max_value=5, value=3, step=1)

sidebar_expander_inputs_4 = st.sidebar.beta_expander("Assets")
user_input_assets_cash =            sidebar_expander_inputs_4.number_input('1. Cash & Savings', value=0, step=1000)
user_input_assets_stocks_bonds =    sidebar_expander_inputs_4.number_input('2. Stocks & Bonds', value=0, step=1000)
user_input_assets_real_estate =     sidebar_expander_inputs_4.number_input('3. Real Estate Investments', value=0, step=1000)
user_input_assets_other =           sidebar_expander_inputs_4.number_input('4. Other Assets/Investments', value=0, step=1000)
user_input_assets_debts =           sidebar_expander_inputs_4.number_input('5. Total Debts', value=0, step=1000)


sidebar_expander_inputs_6 = st.sidebar.beta_expander("Tax")
user_input_tax_method =             sidebar_expander_inputs_6.text_input('1. State')
user_input_tax_method =             sidebar_expander_inputs_6.selectbox('1. Filing Method', ["Standard Deduction","Itemized Deduction", "To Be Determined"])
user_input_tax_status =             sidebar_expander_inputs_6.selectbox('2. Filing Status', ["Single","Married, Filing Jointly","Married, Filing Separately","Head of Household", "To Be Determined"])
user_input_tax_marginal_rate=       sidebar_expander_inputs_6.slider('3. Federal Marginal Tax Rate (%)',min_value=0, max_value=37, value=20, step=1)

show_only_qualified_flag = st.sidebar.checkbox('Show only badges and strategies that I qualify')







########################################################
### SECTION 2: Setting up  Columns for Badges ##########
########################################################

#Setup Columns in main page
#col1 is for badges and col2 is for strategies
badge_comp_dict = {">=": ge, ">": gt, "=": eq, "<": lt, "<=": le, "!=": ne}    

def badge_emoji(bool_var):
    if bool_var:
        return ":medal: "
    else:
        return ":white_circle: "

def badge_qualification_from_input(badge_variable):
    var_matrix_badges_complete_temp = var_matrix_badges_complete[var_matrix_badges_complete['badge_variable'] == badge_variable].dropna()
    #condition 1 check
    cond1_temp_variable = var_matrix_badges_complete_temp['condition1_variable'].iloc[0]
    cond1_user_temp_value = globals()[cond1_temp_variable]
    cond1_temp_direction = var_matrix_badges_complete_temp['condition1_direction'].iloc[0]
    cond1_temp_value = int(var_matrix_badges_complete_temp['condition1_value'].iloc[0])
    cond1_bool = badge_comp_dict[cond1_temp_direction](cond1_user_temp_value, cond1_temp_value)

    #condition 2 check
    cond2_temp_variable = var_matrix_badges_complete_temp['condition2_variable'].iloc[0]
    cond2_user_temp_value = globals()[cond2_temp_variable]
    cond2_temp_direction = var_matrix_badges_complete_temp['condition2_direction'].iloc[0]
    cond2_temp_value = int(var_matrix_badges_complete_temp['condition2_value'].iloc[0])
    cond2_bool = badge_comp_dict[cond2_temp_direction](cond2_user_temp_value, cond2_temp_value)
    
    #return true and false of the collection
    return cond1_bool & cond2_bool

col1_badges.header('Step Two: Collect Badges')


badges_title_dict = {
    '1. Foundation': badge_df1,
    '2. Resource': badge_df2,
    '3. Analysis': badge_df3,
    '4. Buying': badge_df4,
    '5. Mortgage': badge_df5,
    '6. Tax': badge_df6,
    '7. Value-add': badge_df7,
    '8. Property Management': badge_df8,
    '9. Legal': badge_df9,
    '10. Selling': badge_df10}

user_badge_dict = {}

for k, v in badges_title_dict.items():
    temp = col1_badges.beta_expander(k)
    for index, row in v.iterrows():
        user_badge_dict[row['badge_variable']] = badge_qualification_from_input(row['badge_variable'])
        if  not (show_only_qualified_flag and not(user_badge_dict[row['badge_variable']])):
            temp.markdown(badge_emoji(user_badge_dict[row['badge_variable']]) + "[{}]".format(row['badge_name_full']) + "({})".format(row['url']))


########################################################
### SECTION 4: Setting up  Columns for Strategy ##########
########################################################
def stra_emoji(bool_var):
    if bool_var:
        return ":heavy_check_mark: "
    else:
        return ":heavy_multiplication_x: "

def stra_qualification_from_badge(strategy_variable):
    var_matrix_strategy_complete_temp = var_matrix_strategies_complete[var_matrix_strategies_complete['strategy_variable'] == strategy_variable].dropna()
    #condition 1 check
    cond1_temp_variable = var_matrix_strategy_complete_temp['condition1_variable'].iloc[0]
    cond1_user_temp_value = user_badge_dict[cond1_temp_variable]
    cond1_temp_direction = var_matrix_strategy_complete_temp['condition1_direction'].iloc[0]
    cond1_temp_value = int(var_matrix_strategy_complete_temp['condition1_value'].iloc[0])
    cond1_bool = badge_comp_dict[cond1_temp_direction](cond1_user_temp_value, cond1_temp_value)

    #condition 2 check
    cond2_temp_variable = var_matrix_strategy_complete_temp['condition2_variable'].iloc[0]
    cond2_user_temp_value = user_badge_dict[cond2_temp_variable]
    cond2_temp_direction = var_matrix_strategy_complete_temp['condition2_direction'].iloc[0]
    cond2_temp_value = int(var_matrix_strategy_complete_temp['condition2_value'].iloc[0])
    cond2_bool = badge_comp_dict[cond2_temp_direction](cond2_user_temp_value, cond2_temp_value)
    
    #return true and false of the collection
    return cond1_bool & cond2_bool

stra_title_dict = {
    '1. Foundation': stra_df1,
    '2. Resource': stra_df2,
    '3. Analysis': stra_df3,
    '4. Buying': stra_df4,
    '5. Mortgage': stra_df5,
    '6. Tax': stra_df6,
    '7. Value-add': stra_df7,
    '8. Property Management': stra_df8,
    '9. Legal': stra_df9,
    '10. Selling': stra_df10}

col2_strategies.header('Step Three: View Personalized Strategies')

for k, v in stra_title_dict.items():
    temp = col2_strategies.beta_expander(k)
    for index, row in v.iterrows():
        user_badge_dict[row['strategy_variable']] = stra_qualification_from_badge(row['strategy_variable'])
        if  not (show_only_qualified_flag and not(user_badge_dict[row['strategy_variable']])):
            temp.markdown(stra_emoji(stra_qualification_from_badge(row['strategy_variable'])) + "[{}]".format(row['strategy_name_full']) + "({})".format(row['url']))


########################################################
### SECTION 3: Writing Functions########################
########################################################
















