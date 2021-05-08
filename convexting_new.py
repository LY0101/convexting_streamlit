# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:15:12 2021

@author: yang
"""
import streamlit as st
import pandas as pd
import numpy as np
from operator import lt, le, eq, ne, ge, gt

from inputs import *

# Page Setup
st.set_page_config(layout='wide')
st.title('Convexting: Personalized Real Estate Investing Guide')
st.write("")  # see *
st.write("")  # see *


# font
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
# Sidebar variables
st.sidebar.title("Instructions")
# expander_sb = st.sidebar.beta_expander("Instructions")
# expander_sb.markdown("<b>Three easy steps to generate personalized strategies!</b> ",unsafe_allow_html=True)
# expander_sb.markdown('<p class="instructions"><b>1.Inputs:</b> punch in your personal stats to see which badges you qualify for!</p>', unsafe_allow_html=True)
# expander_sb.markdown('<p class="instructions"><b>2.Badges:</b> collect badges (directly or through inputs) to unlock more strategies! </p>', unsafe_allow_html=True)
# expander_sb.markdown('<p class="instructions"><b>3.Strategies:</b> based on your badges, these strategies likely suit you best!</p>', unsafe_allow_html=True)
st.sidebar.markdown(
    '<p class="instructions"><b>1.Inputs:</b> punch in your own stats to see personalized recommendations!</p>', unsafe_allow_html=True)
st.sidebar.markdown(
    '<p class="instructions"><b>2.Guides:</b> Convexting&apos;s none-BS take on real estate investing education!</p>', unsafe_allow_html=True)
st.sidebar.markdown(
    '<p class="instructions"><b>3.Actionable Next Steps:</b> strategies that create direct monetary impact!</p>', unsafe_allow_html=True)

st.sidebar.title("Input Info")


# col1_badges, col2_guides, col3_actionitems = st.beta_columns((1,2,3))


# primary inputs


sidebar_expander_inputs_5 = st.sidebar.beta_expander("Real Estate")
user_input_re_renter = sidebar_expander_inputs_5.selectbox('1. I Am Currently...', [
                                                           "Renting and ready to buy!", "Renting but not ready to buy", "Living in Primary Residence", "Other"])
# user_input_re_occupancy_type = sidebar_expander_inputs_5.multiselect('2. I Want to Buy Property for...', [
#                                                                      "Primary Residence", "Second Home", "Investment Property", "House Hacking", "Value-add Property"])
user_input_re_ownership_type = sidebar_expander_inputs_5.multiselect('2. I Already Own...', [
                                                                     "Primary Residence", "Second Home", "Investment Property", "House Hacking Property", "Value-add Property"])
user_input_re_num = sidebar_expander_inputs_5.number_input(
    '3. How many properties do you own?', value=0, step=1)
sidebar_expander_inputs_5.write(
    "For property values and mortgages ,  see Assets & Liabilities section")

sidebar_expander_inputs_2 = st.sidebar.beta_expander("Personal")
user_input_credit_score = sidebar_expander_inputs_2.slider(
    '1. Credit Score', min_value=500, max_value=850, value=700)
user_input_personal_zipcode = sidebar_expander_inputs_2.number_input(
    '2. Zip Code of Intended Purchase', value=90210)
# user_input__personal_complexity = sidebar_expander_inputs_2.slider(
#     '3. Complexity (e.g. 5 = can handle highly complex tasks)', min_value=1, max_value=5, value=3, step=1)
# user_input__personal_effort = sidebar_expander_inputs_2.slider(
#     '4. Effort (e.g. 5 = willing to put in a ton of effort)', min_value=1, max_value=5, value=3, step=1)


sidebar_expander_inputs_3 = st.sidebar.beta_expander("Income")
user_input_income_amount = sidebar_expander_inputs_3.number_input(
    '1. Total Income (Annual Pretax)', value=50000, step=10000)
user_input_income_type = sidebar_expander_inputs_3.selectbox(
    '2. Main Income Type', ["W2", "1099", "Both", "To Be Determined"])
user_input_income_lvl = sidebar_expander_inputs_3.slider(
    '3. Relative Income (5 = very high vs location)', min_value=1, max_value=5, value=3, step=1)
user_input_income_stability = sidebar_expander_inputs_3.slider(
    '4. Income Stability (5 = very stable)', min_value=1, max_value=5, value=3, step=1)

sidebar_expander_inputs_4 = st.sidebar.beta_expander("Assets & Liabilities")
user_input_assets_down = sidebar_expander_inputs_4.number_input(
    '1. Asset: Money for Down Payment', value=10000, step=10000)
user_input_assets_cash = sidebar_expander_inputs_4.number_input(
    '2. Asset: Cash & Liquid Savings', value=10000, step=10000)
user_input_assets_stocks_bonds = sidebar_expander_inputs_4.number_input(
    '3. Asset: Stocks & Bonds', value=50000, step=10000)
user_input_assets_re_pr = sidebar_expander_inputs_4.number_input(
    '4. Asset: Real Estate Primary Residence', value=0, step=10000)
user_input_assets_re_ip = sidebar_expander_inputs_4.number_input(
    '5. Asset: Real Estate Investment Property', value=0, step=10000)
user_input_assets_other = sidebar_expander_inputs_4.number_input(
    '6. Asset: Other Assets/Investments', value=0, step=10000)
user_input_liabilties_mort_pr = sidebar_expander_inputs_4.number_input(
    '7. Liability: Mortgage on Primary Residence', value=0, step=10000)
user_input_liabilties_mort_ip = sidebar_expander_inputs_4.number_input(
    '8. Liability: Mortgages on Investment Prop', value=0, step=10000)
user_input_assets_consumer_debt = sidebar_expander_inputs_4.number_input(
    '9. Liability: Consumer & Student Loans', value=0, step=10000)

sidebar_expander_inputs_6 = st.sidebar.beta_expander("Tax")
user_input_tax_method = sidebar_expander_inputs_6.text_input('1. State')
user_input_tax_method = sidebar_expander_inputs_6.selectbox(
    '2. Filing Method', ["Standard Deduction", "Itemized Deduction", "To Be Determined"])
user_input_tax_status = sidebar_expander_inputs_6.selectbox('2. Filing Status', [
                                                            "Single", "Married, Filing Jointly", "Married, Filing Separately", "Head of Household", "To Be Determined"])
user_input_tax_marginal_rate = sidebar_expander_inputs_6.slider(
    '4. Federal Marginal Tax Rate (%)', min_value=0, max_value=37, value=20, step=1)

# show_only_qualified_flag = st.sidebar.checkbox('Show only badges and strategies that I qualify')


########################################################
### SECTION 2: Setting up  Columns for Badges ##########
########################################################

# Setup Columns in main page
# col1 is for badges and col2 is for strategies
badge_comp_dict = {">=": ge, ">": gt, "=": eq, "<": lt, "<=": le, "!=": ne}


def badge_emoji(bool_var):
    if bool_var:
        return ":medal: "
    else:
        return ":white_circle: "


def badge_qualification_from_input(badge_variable):
    var_matrix_badges_complete_temp = var_matrix_badges_complete[
        var_matrix_badges_complete['badge_variable'] == badge_variable].dropna()
    # condition 1 check
    cond1_temp_variable = var_matrix_badges_complete_temp['condition1_variable'].iloc[0]
    cond1_user_temp_value = globals()[cond1_temp_variable]
    cond1_temp_direction = var_matrix_badges_complete_temp['condition1_direction'].iloc[0]
    cond1_temp_value = int(
        var_matrix_badges_complete_temp['condition1_value'].iloc[0])
    cond1_bool = badge_comp_dict[cond1_temp_direction](
        cond1_user_temp_value, cond1_temp_value)

    # condition 2 check
    cond2_temp_variable = var_matrix_badges_complete_temp['condition2_variable'].iloc[0]
    cond2_user_temp_value = globals()[cond2_temp_variable]
    cond2_temp_direction = var_matrix_badges_complete_temp['condition2_direction'].iloc[0]
    cond2_temp_value = int(
        var_matrix_badges_complete_temp['condition2_value'].iloc[0])
    cond2_bool = badge_comp_dict[cond2_temp_direction](
        cond2_user_temp_value, cond2_temp_value)

    # return true and false of the collection
    return cond1_bool & cond2_bool


# Stats Summary Drop Down Menu

#st.header('Summary of Your Current Stats')

stats_summary_expander = st.beta_expander(
    "Summary of Your Stats: You have completed [5] of [25] inputs")
summary_col1, summary_col2, summary_col3, summary_col4, summary_col5 = stats_summary_expander.beta_columns(
    (1, 1, 1, 1, 1))
summary_col1.subheader('Real Estate')
summary_col1.write("number of properties owned")
summary_col1.write(user_input_re_num)

summary_col2.subheader('Personal')
summary_col3.subheader('Income')
summary_col4.subheader('Assets')
summary_col5.subheader('Tax')
st.write("")

# Stats Summary Drop Down Menu

additional_filter_expander = st.beta_expander(
    "Additional Filters to Optimize Viewing")
filter_col1, filter_col2, filter_col3, filter_col4, filter_col5 = additional_filter_expander.beta_columns(
    (1, 1, 1, 1, 1))
st.write("")
st.write("")

filter_col1.subheader('I Want to Buy Property for...')
user_input_re_occupancy_type = filter_col1.multiselect('Select ownership type', [
                                                                     "Primary Residence", "Second Home", "Investment Property", "House Hacking", "Value-add Property"])
filter_col2.subheader('Buying 1st Property')
filter_1st_home = filter_col2.checkbox('Buying 1st Property?', value=False)

filter_col3.subheader('Difficulty Level')
filter_level = filter_col3.selectbox("Filter for Difficult Level of Guides and Strategies", [
    "Beginner", "Intermediate", "Advanced", "Professional"], index=1)

filter_col4.subheader('Complexity Level')
user_input__personal_complexity = filter_col4.slider(
    'e.g. 5 = willing to tackle complex challenges', min_value=1, max_value=5, value=3, step=1)

filter_col5.subheader('Effort Level')
user_input__personal_effort = filter_col5.slider(
    'e.g. 5 = willing to put in a ton of effort', min_value=1, max_value=5, value=3, step=1)



st.write("")
st.write("")
st.write("")

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
    # temp = col1_badges.beta_expander(k)
    # st.write(k)
    for index, row in v.iterrows():
        user_badge_dict[row['badge_variable']] = badge_qualification_from_input(
            row['badge_variable'])
        # if  not (show_only_qualified_flag and not(user_badge_dict[row['badge_variable']])):
        # st.markdown(badge_emoji(user_badge_dict[row['badge_variable']]) + "[{}]".format(row['badge_name_full']) + "({})".format(row['url']))


########################################################
### SECTION 4: Setting up  Columns for Strategy ##########
########################################################
def stra_emoji(bool_var):
    if bool_var:
        return ":heavy_check_mark: "
    else:
        return ":heavy_multiplication_x: "


def stra_qualification_from_badge(strategy_variable):
    var_matrix_strategy_complete_temp = var_matrix_strategies_complete[
        var_matrix_strategies_complete['strategy_variable'] == strategy_variable]  # .dropna()
    # condition 1 check
    # try:
    cond1_temp_variable = var_matrix_strategy_complete_temp['condition1_variable'].iloc[0]
    if cond1_temp_variable is np.nan:
        return True
    cond1_user_temp_value = user_badge_dict[cond1_temp_variable]
    cond1_temp_direction = var_matrix_strategy_complete_temp['condition1_direction'].iloc[0]
    cond1_temp_value = int(
        var_matrix_strategy_complete_temp['condition1_value'].iloc[0])
    cond1_bool = badge_comp_dict[cond1_temp_direction](
        cond1_user_temp_value, cond1_temp_value)

    # condition 2 check
    cond2_temp_variable = var_matrix_strategy_complete_temp['condition2_variable'].iloc[0]
    cond2_user_temp_value = user_badge_dict[cond2_temp_variable]
    cond2_temp_direction = var_matrix_strategy_complete_temp['condition2_direction'].iloc[0]
    cond2_temp_value = int(
        var_matrix_strategy_complete_temp['condition2_value'].iloc[0])
    cond2_bool = badge_comp_dict[cond2_temp_direction](
        cond2_user_temp_value, cond2_temp_value)

    # return true and false of the collection
    return cond1_bool & cond2_bool
    # except:
    #     return False


col2_guides, col3_actionitems = st.beta_columns((1, 2))

col2_guides.header('Personalized Guides')
guide_top3_qualified_flag = False
guide_show_all = False
guide_flag = col2_guides.selectbox(
    '', ['Show Top 3 Impactful Guides', 'Show All Qualified Guides', 'Show All Available Guides'], index=0, key=None)
if guide_flag == 'Show Top 3 Impactful Guides':
    guide_top3_qualified_flag = True
elif guide_flag == 'Show All Available Guides':
    guide_show_all = True
# guide_top3_qualified_flag = col2_guides.checkbox('Show top three impactful guides', value=True)
# guide_show_all = col2_guides.checkbox('Show all guides available', value=False)

# Foundation
stra_df1 = stra_df("Foundation", flag_first_time=filter_1st_home,
                   difficulty_level=filter_level)

# Resource
stra_df2 = stra_df("Resource", flag_first_time=filter_1st_home,
                   difficulty_level=filter_level)

# Analysis
stra_df3 = stra_df("Analysis", flag_first_time=filter_1st_home,
                   difficulty_level=filter_level)

# Buying
stra_df4 = stra_df("Buying", flag_first_time=filter_1st_home,
                   difficulty_level=filter_level)

# Mortgage
stra_df5 = stra_df("Mortgage", flag_first_time=filter_1st_home,
                   difficulty_level=filter_level)

# Tax
stra_df6 = stra_df("Tax", flag_first_time=filter_1st_home,
                   difficulty_level=filter_level)

# Value-add
stra_df7 = stra_df("Value-add", flag_first_time=filter_1st_home,
                   difficulty_level=filter_level)

# Property Management
stra_df8 = stra_df("Property Management",
                   flag_first_time=filter_1st_home, difficulty_level=filter_level)

# Legal
stra_df9 = stra_df("Legal", flag_first_time=filter_1st_home,
                   difficulty_level=filter_level)

# Selling
stra_df10 = stra_df("Selling", flag_first_time=filter_1st_home,
                    difficulty_level=filter_level)

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

for k, v in stra_title_dict.items():
    temp = col2_guides.beta_expander(k)
    # print(v.apply(
    #     lambda x: stra_qualification_from_badge(x['strategy_variable']), axis=1))
    try:
        v['qualified_flag'] = v.apply(
            lambda x: stra_qualification_from_badge(x['strategy_variable']), axis=1)
    except:
        v['qualified_flag'] = False
    v = v[v['Type'] == 'Guide']
    if guide_top3_qualified_flag:
        v = v[v['qualified_flag'] == True]
        v = v.sort_values(by=['impact', 'strategy_num2'],
                          ascending=[False, True]).head(3)
    if guide_show_all is False:
        v = v[v['qualified_flag'] == True]
    for index, row in v.iterrows():
        display_str = stra_emoji(row['qualified_flag']) + "[{}]".format(
            row['strategy_name_full']) + "({})".format(row['url'])
        if guide_top3_qualified_flag == True:
            display_str += " (Impact Level: {})".format(row['impact'])
        temp.markdown(display_str)

col3_actionitems.header('Actionable Next Steps with Monetary Impact')
action_top3_qualified_flag = False
action_show_all = False
action_flag = col3_actionitems.selectbox(
    '', ['Show Top 3 Impactful Next Steps', 'Show All Qualified Next Steps', 'Show All Available Next Steps'], index=0, key=None)
if action_flag == 'Show Top 3 Impactful Next Steps':
    action_top3_qualified_flag = True
elif action_flag == 'Show All Available Next Steps':
    action_show_all = True

for k, v in stra_title_dict.items():
    temp = col3_actionitems.beta_expander(k)
    try:
        v['qualified_flag'] = v.apply(
            lambda x: stra_qualification_from_badge(x['strategy_variable']), axis=1)
    except:
        v['qualified_flag'] = False
    v = v[v['Type'] == 'Actionable']
    if action_top3_qualified_flag:
        v = v[v['qualified_flag'] == True]
        v = v.sort_values(by=['impact', 'strategy_num2'],
                          ascending=[False, True]).head(3)
    if action_show_all is False:
        v = v[v['qualified_flag'] == True]
    for index, row in v.iterrows():
        display_str = stra_emoji(row['qualified_flag']) + "[{}]".format(
            row['strategy_name_full']) + "({})".format(row['url'])
        if guide_top3_qualified_flag == True:
            display_str += " (Impact Level: {})".format(row['impact'])
        temp.markdown(display_str)

########################################################
### SECTION 3: Writing Functions########################
########################################################
