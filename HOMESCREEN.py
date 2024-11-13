import streamlit as st
import json
import numpy as np
from Finance import financial_calculations
from others import calculations

st.set_page_config(
    page_title="Lendo Scorecard",
    page_icon="logo.svg",
)

def numeric_input(label, value, key):
    input_value = st.text_input(label, value, key=key)
    try:
        return float(input_value)
    except:
        return -33

st.markdown(
    """
    <style>
    .stApp {
        background-color: lightblue;  /* Background color using a name */
    }
    .main-title {
        color: navy;  /* Text color for the main title */
        font-size: 36px;
        text-align: center;
        font-weight: bold;
    }
    .sub-title {
        color: darkblue;  /* Text color for the subtitle */
        font-size: 24px;
        text-align: center;
        margin-bottom: 20px;
    }
    .text {
        color: black;  /* General text color */
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html = True
)

st.image("logo.svg", caption=None, width=200, use_column_width=50, clamp=False, channels="RGB", output_format="auto")

form_fields = {
    'Current Assets': ['Cash & Cash Equivalents', 'Marketable Securities', 'Trade Receivables - Gross', 'Provision', 
                       'Unbilled Revenues', 'Inventory - Gross', 'Slow-Moving assets provision', 'Due from shareholder(s)', 
                       'Due from Related Parties', 'Other Current Assets'],
    'Non Current Assets': ['Lands & properties', 'Equipment & machinaries', 'Vehicles, Equipment, machineries', 
                           'Furniture and others', 'Right of use assets', 'Depreciation', 'Capital work in progress', 
                           'Investment in Subsidiaries', 'Other Investments', 'Intangible Assets', 'Other Non-Current Assets','Total Fixed Assets'],
    'Current Liabilities': ["Short Term Loans - Banks", "Short Term Loans - NBFI", "CPTL (current portion of Term loans) - Banks", 
                            "CPTL (current portion of Term loans) - NBFI", "CPTL - Capital Lease Obligations", "Trade Payables", 
                            "Advances from Customers", "Due to shareholder(s) - Not subordinated", "Due to related parties", 
                            "Zakat Provision", "VAT", "Dividends payable to shareholders", "Accrued expense/Unearned Revenues", 
                            "Other Current Liabilities"],
    'Non Current Liabilities': ["TL - Banks", "TL - NBFI", "Capital Lease Obligations", "Bonds & other Term lending", 
                                "Due to shareholder(s) - Not subordinated", "Due to Related Parties", "Employees Benefits", 
                                "Other Non-Current Liabilities"],
    'Shareholders Equity': ["Paid in Capital", "Additional Capital", "Reserves", "Subordinated Debt", "Current Year Profit (Loss)", 
                            "Retained Profit (Loss)", "Non-controlling interest", "Unrealized Gains"],
    'PnL + Cash Flow': ['Revenues', 'COGS','Depreciation', 'G&A', 'Selling Expense', 'Depreciation/Amortizatoin', 
                        'Operating Expenses', 'Other Operating Income', 'Finance Cost (interest)',
                        'Income (loss) from Investments', 'Taxes/Zakat', 'Net Cash from Operating Activities', 
                        'Total loans as per SIMAH']
}

fields_already_filled = {
    'Current Assets': [],
    'Non Current Assets': [],
    'Current Liabilities': [],
    'Non Current Liabilities':[],
    'Shareholders Equity': [],
    'PnL + Cash Flow': []
}

fields_considered = {
    'Current Assets': ['Cash & Cash Equivalents', 'Marketable Securities', 'Trade Receivables - Gross', 'Provision', 
                       'Unbilled Revenues', 'Inventory - Gross', 'Slow-Moving assets provision', 'Due from shareholder(s)', 
                       'Due from Related Parties', 'Other Current Assets'],
    'Non Current Assets': ['Total Fixed Assets'],
    'Current Liabilities': ["Short Term Loans - Banks", "Short Term Loans - NBFI", "CPTL (current portion of Term loans) - Banks", 
                            "CPTL (current portion of Term loans) - NBFI", "CPTL - Capital Lease Obligations", "Trade Payables", 
                            "Advances from Customers", "Due to shareholder(s) - Not subordinated", "Due to related parties", 
                            "Zakat Provision", "VAT", "Dividends payable to shareholders", "Accrued expense/Unearned Revenues", 
                            "Other Current Liabilities"],
    'Non Current Liabilities': ["TL - Banks", "TL - NBFI", "Capital Lease Obligations", "Bonds & other Term lending", 
                                "Due to shareholder(s) - Not subordinated", "Due to Related Parties", "Employees Benefits", 
                                "Other Non-Current Liabilities"],
    'Shareholders Equity': ["Paid in Capital", "Additional Capital", "Reserves", "Subordinated Debt", "Current Year Profit (Loss)", 
                            "Retained Profit (Loss)", "Non-controlling interest", "Unrealized Gains"],
    'PnL + Cash Flow': ['Revenues', 'COGS','Depreciation', 'G&A', 'Selling Expense', 'Depreciation/Amortizatoin', 
                        'Operating Expenses', 'Other Operating Income', 'Finance Cost (interest)',
                        'Income (loss) from Investments', 'Taxes/Zakat', 'Net Cash from Operating Activities', 
                        'Total loans as per SIMAH']
}
# fields_considered = {
#     'Current Assets': ['Cash & Cash Equivalents', 'Trade Receivables - Gross', 'Provision','Unbilled Revenues', 'Inventory - Gross', 'Slow-Moving assets provision', 'Due from Related Parties','Other Current Assets'],
#     'Non Current Assets': ['Total Fixed Assets'],
#     'Current Liabilities': ["Short Term Loans - Banks", "Short Term Loans - NBFI", "CPTL - Capital Lease Obligations", "Trade Payables" ,"Due to related parties", "Zakat Provision","Other Current Liabilities"],
#     'Non Current Liabilities': ["TL - Banks", "TL - NBFI", "Capital Lease Obligations" ,"Due to Related Parties", "Employees Benefits", "Other Non-Current Liabilities"],
#     'Shareholders Equity': ["Paid in Capital", "Additional Capital", "Reserves","Subordinated Debt", "Current Year Profit (Loss)", 
#                             "Retained Profit (Loss)"],
#     'PnL + Cash Flow': ['Revenues', 'COGS', 'Operating Expenses','Other Operating Income', 'Finance Cost (interest)','Taxes/Zakat', 
#                         'Net Cash from Operating Activities', 
#                         'Total loans as per SIMAH']
# }

# Title of the app
st.title("Financials")

# Form section
with st.form("Financial_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(f"####  2024")

        input_data24 = {}

        for category, fields in form_fields.items():
            st.write(f"### {category}")
            input_data24[category] = {}
            
            for field in fields:
                if field in fields_considered[category]:
                    input_data24[category][field] = numeric_input(f"{field}:", value=0, key=f"{field}_{category}_24")
                elif field in fields_already_filled[category]:
                    st.markdown(f"**{field}**")
                    input_data24[category][field] =  numeric_input("", value=0, key=f"{field}_{category}_24")
                else:
                    input_data24[category][field] = 0

    with col2:
        st.write(f"####  2023")
        input_data23 = {}

        for category, fields in form_fields.items():
            st.write(f"### {category}")
            input_data23[category] = {}
            for field in fields:
                if field in fields_considered[category]:
                    input_data23[category][field] = numeric_input(f"{field}:", value=0, key=f"{field}_{category}_23")
                elif field in fields_already_filled[category]:
                    st.markdown(f"**{field}**")
                    input_data23[category][field] =  numeric_input(f"", value=int(np.array(list(input_data23['Current Assets'].values())).sum()), key=f"{field}_{category}_23")
                else:
                    input_data23[category][field] = 0

    with col3:
        st.write(f"####  2022")

        input_data22 = {}

        for category, fields in form_fields.items():
            st.write(f"### {category}")
            input_data22[category] = {}
            for field in fields:
                if field in fields_considered[category]:
                    input_data22[category][field] = numeric_input(f"{field}:", value=0, key=f"{field}_{category}_22")
                elif field in fields_already_filled[category]:
                    st.markdown(f"**{field}**")
                    input_data22[category][field] =  numeric_input(f"", value=int(np.array(list(input_data22['Current Assets'].values())).sum()), key=f"{field}_{category}_22")
                else:
                    input_data22[category][field] = 0

    if st.form_submit_button("Submit"):

        with open('input_data24.json', 'w') as file:
            json.dump(input_data24, file, indent=4)

        with open('input_data23.json', 'w') as file:
            json.dump(input_data23, file, indent=4)

        with open('input_data22.json', 'w') as file:
            json.dump(input_data22, file, indent=4)

        st.write("### Form Data Submitted")

        col1, col2, col3 = st.columns(3)

        with col1:
            current_assets = numeric_input(f"Current Assets", value=int(np.array(list(input_data24['Current Assets'].values())).sum()), key=99)
            non_current_assets = numeric_input(f"Non Current Assets", value=int(np.array(list(input_data24['Non Current Assets'].values())).sum()), key=199)
            total_assets = numeric_input(f"Total Assets", value=current_assets+non_current_assets, key=299)

            current_liabilities = numeric_input(f"Current Liabilities", value=int(np.array(list(input_data24['Current Liabilities'].values())).sum()), key=399)
            non_current_liabilities = numeric_input(f"Non Current Liabilities", value=int(np.array(list(input_data24['Non Current Liabilities'].values())).sum()), key=499)
            total_liabilities = numeric_input(f"Total Liabilities", value=current_liabilities+non_current_liabilities, key=599)

            total_shareholder_equity = numeric_input(f"Total Shareholder Equit", value=int(np.array(list(input_data24['Shareholders Equity'].values())).sum()), key=699)
            TE = numeric_input(f"Total Liabilities + Shareholders Equity", value=total_liabilities+total_shareholder_equity, key=697244)
            if(total_assets - total_liabilities - total_shareholder_equity < 10):
                st.markdown(f"<h1 style='color:green'>Balanced</h1>", unsafe_allow_html=True)
                
            else:
                st.markdown(f"<h1 style='color:red'>Not Balanced</h1>", unsafe_allow_html=True)

            st.markdown(f"<h1 style='color:purple'>_ _ _ _ _ _</h1>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:purple'></h3>", unsafe_allow_html=True)

            gross_profit = input_data24['PnL + Cash Flow']['Revenues'] - input_data24['PnL + Cash Flow']['COGS'] - input_data24['PnL + Cash Flow']['Depreciation']
            gross_profit = numeric_input(f"Total Shareholder Equit", value=gross_profit, key=69924)

            operating_profit = gross_profit + input_data24['PnL + Cash Flow']['Other Operating Income'] - input_data24['PnL + Cash Flow']['Operating Expenses'] - input_data24['PnL + Cash Flow']['G&A'] - input_data24['PnL + Cash Flow']['Selling Expense'] - input_data24['PnL + Cash Flow']['Depreciation/Amortizatoin']
            operating_profit = numeric_input(f"Operating Profit (loss)", value=operating_profit, key=69824)

            net_profit = gross_profit - input_data24['PnL + Cash Flow']['Finance Cost (interest)'] + input_data24['PnL + Cash Flow']['Income (loss) from Investments']  - input_data24['PnL + Cash Flow']['Taxes/Zakat']
            net_profit = numeric_input(f"Net Profit (loss)", value=net_profit, key=69724)

            

        with col2:
            current_assets = numeric_input(f"Current Assets", value=int(np.array(list(input_data23['Current Assets'].values())).sum()), key=93)
            non_current_assets = numeric_input(f"Non Current Assets", value=int(np.array(list(input_data23['Non Current Assets'].values())).sum()), key=193)
            total_assets = numeric_input(f"Total Assets", value=current_assets+non_current_assets, key=293)

            current_liabilities = numeric_input(f"Current Liabilities", value=int(np.array(list(input_data23['Current Liabilities'].values())).sum()), key=393)
            non_current_liabilities = numeric_input(f"Non Current Liabilities", value=int(np.array(list(input_data23['Non Current Liabilities'].values())).sum()), key=493)
            total_liabilities = numeric_input(f"Total Liabilities", value=current_liabilities+non_current_liabilities, key=593)

            total_shareholder_equity = numeric_input(f"Total Shareholder Equit", value=int(np.array(list(input_data23['Shareholders Equity'].values())).sum()), key=693)
            TE = numeric_input(f"Total Liabilities + Shareholders Equity", value=total_liabilities+total_shareholder_equity, key=697243)

            if(total_assets - total_liabilities - total_shareholder_equity < 10):
                st.markdown(f"<h1 style='color:green'>Balanced</h1>", unsafe_allow_html=True)
                
            else:
                st.markdown(f"<h1 style='color:red'>Not Balanced</h1>", unsafe_allow_html=True)

            st.markdown(f"<h1 style='color:purple'>Cash Flow</h1>", unsafe_allow_html=True)

            gross_profit = input_data23['PnL + Cash Flow']['Revenues'] - input_data23['PnL + Cash Flow']['COGS'] - input_data23['PnL + Cash Flow']['Depreciation']
            gross_profit = numeric_input(f"Total Shareholder Equit", value=gross_profit, key=69923)

            operating_profit = gross_profit + input_data23['PnL + Cash Flow']['Other Operating Income'] - input_data23['PnL + Cash Flow']['Operating Expenses'] - input_data23['PnL + Cash Flow']['G&A'] - input_data23['PnL + Cash Flow']['Selling Expense'] - input_data23['PnL + Cash Flow']['Depreciation/Amortizatoin']
            operating_profit = numeric_input(f"Operating Profit (loss)", value=operating_profit, key=69823)

            net_profit = gross_profit - input_data23['PnL + Cash Flow']['Finance Cost (interest)'] + input_data23['PnL + Cash Flow']['Income (loss) from Investments']  - input_data23['PnL + Cash Flow']['Taxes/Zakat']
            net_profit = numeric_input(f"Net Profit (loss)", value=operating_profit, key=69723)

            

        with col3:
            current_assets = numeric_input(f"Current Assets", value=int(np.array(list(input_data22['Current Assets'].values())).sum()), key=92)
            non_current_assets = numeric_input(f"Non Current Assets", value=int(np.array(list(input_data22['Non Current Assets'].values())).sum()), key=192)
            total_assets = numeric_input(f"Total Assets", value=current_assets+non_current_assets, key=292)

            current_liabilities = numeric_input(f"Current Liabilities", value=int(np.array(list(input_data22['Current Liabilities'].values())).sum()), key=392)
            non_current_liabilities = numeric_input(f"Non Current Liabilities", value=int(np.array(list(input_data22['Non Current Liabilities'].values())).sum()), key=492)
            total_liabilities = numeric_input(f"Total Liabilities", value=current_liabilities+non_current_liabilities, key=592)

            total_shareholder_equity = numeric_input(f"Total Shareholder Equity", value=int(np.array(list(input_data22['Shareholders Equity'].values())).sum()), key=692)
            TE = numeric_input(f"Total Liabilities + Shareholders Equity", value=total_liabilities+total_shareholder_equity, key=697242)
            if(total_assets - total_liabilities - total_shareholder_equity < 10):
                st.markdown(f"<h1 style='color:green'>Balanced</h1>", unsafe_allow_html=True)
                
            else:
                st.markdown(f"<h1 style='color:red'>Not Balanced</h1>", unsafe_allow_html=True)

            st.markdown(f"<h1 style='color:purple'>_ _ _ _ _ _</h1>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:purple'></h3>", unsafe_allow_html=True)

            gross_profit = input_data22['PnL + Cash Flow']['Revenues'] - input_data22['PnL + Cash Flow']['COGS'] - input_data22['PnL + Cash Flow']['Depreciation']
            gross_profit = numeric_input(f"Total Shareholder Equit", value=gross_profit, key=69922)

            operating_profit = gross_profit + input_data22['PnL + Cash Flow']['Other Operating Income'] - input_data22['PnL + Cash Flow']['Operating Expenses'] - input_data22['PnL + Cash Flow']['G&A'] - input_data22['PnL + Cash Flow']['Selling Expense'] - input_data22['PnL + Cash Flow']['Depreciation/Amortizatoin']
            operating_profit = numeric_input(f"Operating Profit (loss)", value=operating_profit, key=69822)

            net_profit = gross_profit - input_data22['PnL + Cash Flow']['Finance Cost (interest)'] + input_data22['PnL + Cash Flow']['Income (loss) from Investments']  - input_data22['PnL + Cash Flow']['Taxes/Zakat']
            net_profit = numeric_input(f"Net Profit (loss)", value=operating_profit, key=69722)

            


