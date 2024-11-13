import json
import streamlit as st

def net_profit_margin_score_calculate(f2):
    if f2 <= 0:
        return 0
    elif f2 < 0.08:
        return 1
    elif f2 < 0.15:
        return 3
    elif f2 < 0.25:
        return 5
    else:
        return 7

def gross_profit_margin_score_calcualte(d2):
    if d2 <= 0:
        return 0
    elif d2 < 0.08:
        return 1
    elif d2 < 0.15:
        return 3
    elif d2 < 0.25:
        return 5
    else:
        return 7

def cash_profit_margin_calcualte(h2):
    if h2 <= 0:
        return 0
    elif h2 < 0.05:
        return 1
    elif h2 < 0.1:
        return 3
    elif h2 < 0.2:
        return 5
    else:
        return 7

def debt_to_equity_calculate(j2):
        if j2 < 0:
            return 0
        elif j2 < 0.33:
            return 7
        elif j2 < 0.5:
            return 6
        elif j2 < 0.66:
            return 5
        elif j2 < 1:
            return 3
        elif j2 < 2:
            return 1
        else:
            return 0
        
def DSCR_Score_calculate(l2):
        if l2 < 0:
            return 0
        elif l2 < 1:
            return 1
        elif l2 < 1.5:
            return 2
        elif l2 < 2:
            return 4
        else:
            return 5

def current_ratio_score_calculate(n2):
    if n2==None:
        return 0
    
    if n2 < 0.6:
        return 0
    elif n2 < 0.9:
        return 2
    elif n2 < 1.2:
        return 4
    elif n2 < 1.5:
        return 5
    elif n2 < 2:
        return 7
    else:
        return 9

def working_capital_cycle_per_year_score_calculate(r2):
    if r2 < 0:
        return 8
    elif r2 < 2:
        return 1
    elif r2 < 4:
        return 3
    elif r2 < 6:
        return 6
    else:
        return 8
    
def long_term_debt_to_ebidta_score_calculate(t2):
    if t2 <= 0:
        return 0
    elif t2 < 2:
        return 7
    elif t2 < 4:
        return 5
    elif t2 < 7:
        return 3
    else:
        return 1

def CAGR_EBITDA_score_calculate(v2):
    if v2 <= 0:
        return 0
    elif v2 < 0.05:
        return 1
    elif v2 < 0.1:
        return 4
    elif v2 < 0.3:
        return 7
    else:
        return 9
    
def tol_to_adj_tangible_networth_score_calculate(x2):
    print(f"TOL_to_Adj_Tangible_Networth_Score ********{x2}")
    if x2 < 0:
        return 0
    elif x2 < 2:
        return 7
    elif x2 < 4:
        return 5
    elif x2 < 6:
        return 3
    else:
        return 1
    
def Altman_Z_Score_calculate(z2):
    if z2 < 0:
        return 0
    elif z2 < 1.1:
        return 1
    elif z2 < 2.6:
        return 4
    else:
        return 7
    
def ROCE_Score_calculate(ab2):

    if ab2==None:
        return 0
    if ab2 <= 0:
        return 0
    elif ab2 < 0.05:
        return 1
    elif ab2 < 0.12:
        return 3
    elif ab2 < 0.18:
        return 5
    else:
        return 7
    
def interest_coverage_score_calculate(ad2):

    if ad2==None:
        return 0
    if ad2 < 1:
        return 0
    elif ad2 < 2:
        return 2
    elif ad2 < 3:
        return 4
    else:
        return 7

def numeric_input(label, value,key):
    input_value = st.text_input(label, value,key=key)
    # Check if the entered value is a number
    if input_value.isnumeric():
        return int(input_value)
    elif input_value.replace('.', '', 1).isdigit() and input_value.count('.') < 2:
        return float(input_value)
    else:
        # st.warning("Please enter a valid number.")
        return None

st.title('Financial Ratios _R')

with open('input_data24.json', 'r') as file:
    data = json.load(file)
with open('input_data23.json', 'r') as file:
    dataP = json.load(file)

st.write("### Cash Flow")
col1, col2= st.columns(2)
with col1:
    
    total_investing_cash_flow = numeric_input('Total Investing Cash Flow', value=0, key=30)
with col2:
    total_financing_cash_flow = numeric_input('Total Financing Cash Flow', value=0, key=40)
    # net_income = numeric_input("Net Income",value=0,key=80)    

st.write("### Balance Sheet + PnL Cash Flow")
col1, col2 = st.columns(2)
with col1:
    inventory_days = numeric_input('Inventory Days',value=0,key=10)
    recievable_days = numeric_input('Recievable Days',value=0,key=60)
    intengible_fixed_assets = numeric_input('Intengible Fixed Assets', value=0,key=20)

with col2:
    total_inventory_cash_flow = numeric_input('Total Inventory Cash Flow',value=0,key=50)
    days_payable = numeric_input('Days Payable',value=0,key=70)

short_term_debt = data['Current Liabilities']['Short Term Loans - Banks'] + data['Current Liabilities']['Short Term Loans - NBFI']
long_term_debt = data['Non Current Liabilities']['TL - Banks'] + data['Non Current Liabilities']['TL - NBFI']
total_debt = short_term_debt + long_term_debt

gross_profit_margin = (data['PnL + Cash Flow']['Revenues'] - data['PnL + Cash Flow']['COGS']) / data['PnL + Cash Flow']['Revenues']
net_profit_margin = data['PnL + Cash Flow']['Net Profit'] / data['PnL + Cash Flow']['Revenues']
cash_profit_margin = data['PnL + Cash Flow']['Net Cash from Operating Activities'] / data['PnL + Cash Flow']['Revenues']
debt_to_equity = total_debt / (data['Shareholders Equity']['Total Shareholders Equity'] + 0.0001) 
dscr = data['PnL + Cash Flow']['EBITDA'] / (data['PnL + Cash Flow']['Finance Cost (interest)'] + total_debt + 0.000001)
current_ratio = data['Current Assets']['Total Current Assets'] / data['Current Liabilities']['Total Current Liabilities'] if data['Current Liabilities']['Total Current Liabilities']!=0 else -1
annual_turnover_growth_rate = (data['PnL + Cash Flow']['Revenues'] - dataP['PnL + Cash Flow']['Revenues']) / dataP['PnL + Cash Flow']['Revenues'] if dataP['PnL + Cash Flow']['Revenues']!=0 else -1
working_capital_cycle_per_year = 365 / (inventory_days + recievable_days - days_payable + 0.0001)
long_term_debt_by_ebitda = long_term_debt / (data['PnL + Cash Flow']['EBITDA'] + 0.0001)
cagr_ebitda = (data['PnL + Cash Flow']['EBITDA'] - dataP['PnL + Cash Flow']['EBITDA']) / (dataP['PnL + Cash Flow']['EBITDA']) if dataP['PnL + Cash Flow']['EBITDA'] !=0 else -1
tol_to_adj_tangible_networth = (data['Current Liabilities']['Total Current Liabilities'] + data['Non Current Liabilities']['Total Non Current Liabilities']) / (data['Current Assets']['Total Current Assets'] + data['Non Current Assets']['Total Fixed Assets'] - data['Current Liabilities']['Total Current Liabilities'] - data['Non Current Liabilities']['Total Non Current Liabilities'] - intengible_fixed_assets)
total_assets = (data['Current Assets']['Total Current Assets'] + data['Non Current Assets']['Total Fixed Assets'])
total_liabilities = data['Current Liabilities']['Total Current Liabilities'] + data['Non Current Liabilities']['Total Non Current Liabilities']
working_capital_total_assets = (data['Current Assets']['Total Current Assets'] - data['Current Liabilities']['Total Current Liabilities'])/total_assets
Altman_Z = 1.2 * (working_capital_total_assets) + 1.4*(data['Shareholders Equity']['Retained Profit (Loss)']/total_assets) + 3.3*(data['PnL + Cash Flow']['EBIT']/total_assets) + 0.6*(data['Shareholders Equity']['Total Shareholders Equity']/total_liabilities) + (data['PnL + Cash Flow']['Revenues']/total_assets)

ROCE = data['PnL + Cash Flow']['EBIT'] / (data['Non Current Liabilities']['Total Non Current Liabilities'] + data['Shareholders Equity']['Total Shareholders Equity']) if (data['Non Current Liabilities']['Total Non Current Liabilities'] + data['Shareholders Equity']['Total Shareholders Equity']) !=0 else -1
interest_coverage_ratio = data['PnL + Cash Flow']['EBIT'] / data['PnL + Cash Flow']['Finance Cost (interest)'] if data['PnL + Cash Flow']['Finance Cost (interest)']!=0 else -1


with st.form("my_form1"):
    st.header("Financial Scorecard")
    gross_profit_margin = numeric_input('Gross Profit Margin', value=gross_profit_margin,key=11)
    gross_profit_margin_score = numeric_input('Gross Profit Margin Score', value=gross_profit_margin_score_calcualte(gross_profit_margin),key=12)
    net_profit_margin = numeric_input('Net Profit Margin', value=net_profit_margin,key=13)
    net_profit_margin_score = numeric_input('Net Profit Margin Score', value=net_profit_margin_score_calculate(net_profit_margin),key=14)
    cash_profit_margin = numeric_input('Cash Profit Margin', value=cash_profit_margin,key=15)
    cash_profit_margin_score = numeric_input('Cash Profit Margin Score', value=cash_profit_margin_calcualte(cash_profit_margin),key=155)
    debt_to_equity_wf = numeric_input('Debt to Equity_WF', value=debt_to_equity,key=16)
    debt_to_equity_score = numeric_input('Debt to Equity Score', value=debt_to_equity_calculate(debt_to_equity),key=17)
    debt_service_coverage_wf = numeric_input('Debt Service Coverage_WF', value=dscr,key=18)
    DSCR_Score = numeric_input('DSCR Score', value=DSCR_Score_calculate(dscr),key=19)
    current_ratio = numeric_input('Current Ratio', value=current_ratio,key=101)
    current_ratio_score = numeric_input('Current Ratio Score', value=current_ratio_score_calculate(current_ratio),key=111)
    annual_turover_growth_rate = numeric_input('Annual Turnover Growth Rate', value=annual_turnover_growth_rate,key=122)
    annual_turover_growth_rate_score = numeric_input('Annual Turnover Growth Rate Score', value=1,key=133)
    working_capital_cycle_per_year = numeric_input('Working Capital Cycle per Year', value=working_capital_cycle_per_year,key=144)
    working_capital_cycle_per_year_score = numeric_input('Working Capital Cycle per Year Score', value=working_capital_cycle_per_year_score_calculate(working_capital_cycle_per_year),key=1555)
    long_term_debt_to_ebidta = numeric_input('Long Term Debt to EBITDA', value=long_term_debt_by_ebitda,key=166)
    long_term_debt_to_ebidta_score = numeric_input('Long Term Debt to EBITDA Score', value=long_term_debt_to_ebidta_score_calculate(long_term_debt_by_ebitda),key=177)
    CAGR_EBITDA = numeric_input('CAGR EBITDA', value=cagr_ebitda,key=188)
    CAGR_EBITDA_score = numeric_input('CAGR EBITDA Score',value=CAGR_EBITDA_score_calculate(CAGR_EBITDA),key=199)

    # total_liability_to_adj_tangible_networth = numeric_input('Total Liability to Adj Tangible Networth',value=-1,key=100)
    # total_liability_to_adj_tangible_networth_score = numeric_input('Total Liability to Adj Tangible Networth Score',value=-1,key=100)

    Tol_to_adj_tangible_networth = numeric_input('TOL_to_Adj_Tangible_Networth',value=tol_to_adj_tangible_networth,key=1111)
    tol_to_adj_tangible_networth_score = numeric_input('TOL_to_Adj_Tangible_Networth_Score',value=tol_to_adj_tangible_networth_score_calculate(tol_to_adj_tangible_networth),key=112)
    
    Altman_Z = numeric_input('Altman Z',value=Altman_Z,key=113)
    Altman_Z_Score = numeric_input('Altman Z Score',value=Altman_Z_Score_calculate(Altman_Z),key=114)
    ROCE = numeric_input('ROCE',value=ROCE,key=115)
    ROCE_Score = numeric_input('ROCE Score',value=ROCE_Score_calculate(ROCE),key=116)
    interest_coverage = numeric_input('Interest Coverage',value=interest_coverage_ratio,key=117)
    interest_coverage_score = numeric_input('Interest Coverage Score',value=interest_coverage_score_calculate(interest_coverage),key=118)

    if st.form_submit_button('Submit'):
        st.session_state.PnL = {
            "Gross Profit Margin" : gross_profit_margin,
            "Gross Profit Margin Score" : gross_profit_margin_score,
            "Net Profit Margin" : net_profit_margin,
            "Net Profit Margin Score" : net_profit_margin_score,
            "Cash Profit Margin" : cash_profit_margin,
            "CAGR_EBITDA" : CAGR_EBITDA,
            "CAGR_EBITDA_score" : CAGR_EBITDA_score
        }
        st.success(f"Final Score:{gross_profit_margin_score+net_profit_margin_score+cash_profit_margin_score+debt_to_equity_score+DSCR_Score+current_ratio_score+annual_turover_growth_rate_score+working_capital_cycle_per_year_score+long_term_debt_to_ebidta_score+CAGR_EBITDA_score+Altman_Z_Score+ROCE_Score+interest_coverage_score}")
        print("HI")
    

# with st.form("my_form2"):

#     st.header("Balance Sheet")
#     cash_equivalent = st.number_input('Cash & Cash Equivalents')
#     inventory = st.number_input('Inventory')
#     inventory_days = st.number_input('Inventory Days')
#     receivable = st.number_input('Receivables')
#     receivable_days = st.number_input('Receivable Days')
#     current_assets = st.number_input('Current Assets')
#     long_term_assets = st.number_input('Long-Term Assets')
#     intangible_assets = st.number_input('Intangible Fixed Assets')
#     total_assets = st.number_input('Total Assets')
#     working_capital = st.number_input('Working Capital')
#     short_term_debt = st.number_input('Short Term Debt')
#     days_payable = st.number_input('Days Payable')
#     current_liabilities = st.number_input('Current Liabilities')
#     long_term_debt = st.number_input('Long-Term Debt')
#     total_debt = st.number_input('Total Debt')
#     long_term_liabilities = st.number_input('Long-Term Liabilities')
#     total_liabilities = st.number_input('Total Liabilities')
#     shareholder_equity = st.number_input('Shareholder Equity')

#     if st.form_submit_button('Submit'):

#         st.session_state.balance_sheet = {
#             "Cash Equivalent" : cash_equivalent,
#             "Inventory" : inventory,
#             "Inventory Days" : inventory_days,
#             "Receivable" : receivable,
#             "Receivable Days" : receivable_days,
#             "Current Assets" : current_assets,
#             "Long Term Assets" : long_term_assets,
#             "Intangible Assets" : intangible_assets,
#             "Total Assets" : total_assets,
#             "Working Capital" : working_capital,
#             "Short Term Debt": short_term_debt,
#             "Days Payable" : days_payable,
#             "Current Liabilities" : current_liabilities,
#             "Long Term Debt" : long_term_debt,
#             "Total Debt" : total_debt,
#             "Long Term Liabilities" : long_term_liabilities,
#             "Total Liabilities" : total_liabilities,
#             "Shareholder Equity" : shareholder_equity
#         }
#         print("HI2")
    

# with st.form("my_form3"):

#     st.header("Cash Flow Details")
#     operation_cash_flow = st.number_input('Total Operation Cash Flow')
#     investing_cash_flow = st.number_input('Total Investing Cash Flow')
#     financing_cash_flow = st.number_input('Total Financing Cash Flow')

#     if st.form_submit_button('Submit'):
#         st.session_state.cash_flow = {
#             "Total Operation Cash Flow" : operation_cash_flow,
#             "Total Investing Cash Flow" : investing_cash_flow,
#             "Total Financing Cash Flow" : financing_cash_flow
#         }
#         print("HI3")


# with st.form("my_form4"):

#     st.header("Change In / Curremt Assets / Current Liabilities / Turnover / EBITDA")
#     previous_year_assets = st.number_input('Previous Year Total Assets')
#     current_year_assets = st.number_input('Current Year Total Assets')
#     previous_year_current_assets = st.number_input('Previous Year Current Assets')
#     current_year_current_assets = st.number_input('Current Year Current Assets')
#     previous_year_current_liabilities = st.number_input('Previous Year Current Liabilities')
#     current_year_current_liabilities = st.number_input('Current Year Current Liabilities')
#     previous_year_liabilities = st.number_input('Previous Year Total Liabilities')
#     current_year_liabilities = st.number_input('Current Year Total Liabilities')
#     previous_year_turnover = st.number_input('Previous Year Turnover')
#     current_year_turnover = st.number_input('Current Year Turnover')
#     previous_year_ebitda = st.number_input('Previous Year EBITDA')
#     current_year_ebitda = st.number_input('Current Year EBITDA')

#     if st.form_submit_button('Submit'):
#         st.session_state.delta = {
#             "Previous Year Total Assets" : previous_year_assets,
#             "Current Year Total Assets" : current_year_assets,
#             "Previous Year Current Assets" : previous_year_current_assets,
#             "Current Year Current Assets" : current_year_current_assets,
#             "Previous Year Current Liabilities" : previous_year_current_liabilities,
#             "Current Year Current Liabilities" : current_year_current_liabilities,
#             "Previous Year Total Liabilities" : previous_year_liabilities,
#             "Current Year Total Liabilities" : current_year_liabilities,
#             "Previous Year Turnover" : previous_year_turnover,
#             "Current Year Turnover" : current_year_turnover,
#             "Previous Year EBITDA" : previous_year_ebitda,
#             "Current Year EBITDA" : current_year_ebitda
#         }
#         print("HI4")