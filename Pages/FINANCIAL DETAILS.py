import streamlit as st
import requests
import json
from others import calculations
from Finance import financial_calculations
import numpy as np

st.image("logo.svg", caption=None, width=200, use_column_width=50, clamp=False, channels="RGB", output_format="auto")
st.title('Others')

with open('financial_scores.json', 'r') as file:
    financial_scores = json.load(file)

# financial_scores = {key: 0 for key in financial_scores}

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

st.markdown(f"<h3><b> Others </b></h3>", unsafe_allow_html=True)

if 'form_data2' not in st.session_state:
    st.session_state.form_data2 = {
        'Ownership / Management': {},
        'Business / Activity': {},
        "Company's Credit Bureau Reports": {},
        'Support Factors': {},
        'Warning Signals': {}
    }

if 'submitted_forms' not in st.session_state:
    st.session_state.submitted_forms = set()

def create_form(form_name, fields):
    with st.expander(f"{form_name.capitalize()} {'✅' if form_name in st.session_state.submitted_forms else ''}"):
        with st.form(form_name):
            form_data2 = {}
            for field, options in fields.items():
                form_data2[field] = st.selectbox(field, options, key=f"{form_name}_{field}")
            
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.session_state.form_data2[form_name] = form_data2
                st.session_state.submitted_forms.add(form_name)
                st.success(f"{form_name.capitalize()} submitted successfully!")

# Define form fields with their dropdown options
# financial_scorecard = {

# }
form_fields = {
    'Ownership / Management': {
        'Legal Structure': ['Sole Proprietorship / One Person Company (local / foreign investment)', 'Non-Saudi Company', r'''Foreign Investment (Saudi Company 100% owned by foreign)''', 'Mixed ownership (Local & Foreign)','''Company 100% owned by Locals (ultimately)''','Public Listed Company'],
        'Succession Risk': ['Sole Proprietorship with no second line involved in business', 'Sole Proprietorship / experienced second line involved in business', 'Compnay managed only by one of the partners', 'Complementary management by partners and/or experienced team'],
        '''Owners' experience''': ['No experience', 'Experience in different field of business (Total experience <5 years)', 'Experience in different field of business (Total experience >5 years)', 'Experience in same / related field of business ( <5 years)', 'Experience in same / related field of business ( >5 years)'],
        '''Management's experience''': ['Managed by Owner(s)', 'Managed by an experienced team (with Co. for less than 3 years)', 'Managed by an experienced team (with Co. for more than 3 years)'],
        '''Credit History (owners / Management)''': ['Irregular (Defaults, Past dues, Write off, Court cases)', 'No credit history with clean records (or report is not obtained)', 'O/s Financing with regular repayment and clean records (no histroy of full settlement)', 'At least 1 loan fully settled with regular repayment and clean records']
    },
    'Business / Activity': {
        'Years in Business (for the current business field)': ['Less than 3 years (Yet to break-even)', 'Less than 3 years (profitable)', '3 to <10 years', '>=10 years'],
        'Netaqat': ['Red', 'Yellow', 'Green', 'Platinum'],
        'Markets': [r'''>25% of sales for high-risk countries''', r'''>25% of sales for Other countries (excluding GCC)''', 'Local market (including GCC)'],
        'Industry': ['Water supply; sewerage, waste management', 'Construction', r'''Public administration and defense;compulsory social security''', 'Other service activities', 'Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use',
                      'Activities of extraterritorial organizations and bodies' ,  'Agriculture, Forestry and Fishing' ,  'Manufacturing' , 'Transportation and storage' , 'Real estate activities' , 'Human health and social work activities' , r'''Wholesale and retail trade; repair of motor vehicles and motorcycles''' , 'Mining and quarrying' ,
                      'Electricity, gas, steam and air conditioning supply' , 'Accommodation and food service activities', 'Financial and insurance activities' , 'Professional, scientific and technical activities' , 'Administrative and support service activities' , 'Education' , 'Information and Communication' , 'Arts, entertainment and recreation'],
        r'Type of customers (>=70% of sales/receivables to)': ['Consumers or unknown entities', 'Well-known Corporations (Public listed and/or closed)', 'Govt. and Semi Govt. Entities, and well-known Corporation', 'Govt. and Semi Govt. Entities'],
        r'Customers Concentration (80% of sales/receivables to)': ['<=5 Customers', '6 to <20 Customers', '20 Customers or more'],
        'Inventory liquidity/management': ['Inventory liquidity/management is concerning', 'N.A (Low inventory level or No inventory "Service industry")', 'Level of liquidity/management is uncertain', 'Majority is Ready for sale with proper management system'],
        'Access to additional Fund': ['No access (no support from owners/related parties or access to FI)', 'Proven access to FI', 'Proven support from owners/related parties']
    },
    "Company's Credit Bureau Reports": {
        'Repayment History': ['Defaults, or PD above 90 days', '30 days to 90 days PDs', 'PD below 30 days', 'No Funded facilities or relationship for <2 year with no PD', 'Funded facilities with No PD (relationship >2 year)'],
        'Returned Cheques': ['Unsettled bounced cheques with court cases', 'Unsettled bounced cheques (below 1 year) with no court cases', 'Unsettled bounced cheques (older than 1 years) with no court cases', 'No unsettled bounced cheques']
    },
    "Financials":{
    "Revenues Growth":[financial_scores['revenue_growth']],
    "Change in Gross Profit Margin (GPM)":[financial_scores['GPM_Change']],
    "Net Profit Margin (NPM)":[financial_scores['NPM']],
    "Change in NPM":[financial_scores['NPM_Change']],
    "Cash Flow from Operating Activities":[financial_scores['Cash_Flow']],
    "Current Ratio (CR)":[financial_scores['Current_Ratio']],
    "Leverage Ratio (Adjusted to Subordinated Debt)":[financial_scores['Leveraged_Ratio']],
    "Interest Coverage Ratio (EBIT / Interest Expense)":[financial_scores['Interest_Coverage_Ratio']],
    "DSCR (EBITDA / Debt Service)":[financial_scores['DSCR']],
    "Receivable Quality (Ageing Analysis)":[financial_scores['Recievable_Quality']],
    "Receivable Days":[financial_scores['Recievable_Days']],
    "Debt / Sales Ratio":[financial_scores['Debt_Sales_Ratio']],
    "Availability of Audited Financials":[financial_scores['Availibility_Audited_Financials']],
    "Quality of Internal Reports":[financial_scores['Quality_Internal_Report']]
    },
    'Support Factors': {
        'Control over cash flow': ['No Control', 'Partial control (could be cancelled by client)', 'Partial control (could be cancelled by Third Party)', 'Full Control (AACP, Noncancellable standing order, etc.)'],
        'Relationship with Lendo': ['No Relationship', 'Frequent PDs, Unsatisfactory relationship', 'Satisfactory relationship with some PDs', 'Satisfactory relationship with repayment in a timely manner']
    },
    'Warning Signals': {
        'Change in Ownership': ['Yes','No'],
        'Change in Management': ['Yes','No'],
        'Breach in financial covenants': ['Yes','No'],
        'Delayed AFS for >7 months from End of reporting period': ['Yes','No']
    }
}

# Create forms
for form_name, fields in form_fields.items():
    create_form(form_name, fields)

# Display submitted data
st.write("---")
# Streamlit form for user input
st.title("Client Information Form")

# Create form using Streamlit form functionality
with st.form(key="client_form"):

    client_name = st.text_input("Client Name", value="Client_Name")
    reporting_year = st.number_input("Reporting Period",value=2024)

    col1, col2, col3 = st.columns(3)

    with col1:
        year_2023 = st.number_input("Year  ", value=2024)
        month_2023 = st.selectbox("Month  ", options=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], index=11)
        type_fs_2023 = st.selectbox("Type of FS  ", options=["Audited", "Draft", "In house", "Projections"], index=0)
        months_2023 = st.number_input("# of months  ", min_value=1, max_value=12, value=12)
        quality_2023 = st.selectbox("Quality of Internal Reports  ", options=["No Concerns/Moderate", "Unsatisfying", "Professional"])

    with col2:
        year_2022 = st.number_input("Year", value=2023)
        month_2022 = st.selectbox("Month", options=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], index=11)
        type_fs_2022 = st.selectbox("Type of FS", options=["Audited", "Draft", "In house", "Projections"], index=0)
        months_2022 = st.number_input("# of months", min_value=1, max_value=12, value=12)
        quality_2022 = st.selectbox("Quality of Internal Reports", options=["No Concerns/Moderate", "Unsatisfying", "Professional"])

    with col3:
        year_2021 = st.number_input("Year ", value=2022)
        month_2021 = st.selectbox("Month ", options=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], index=11)
        type_fs_2021 = st.selectbox("Type of FS ", options=["Audited", "Draft", "In house", "Projections"], index=0)
        months_2021 = st.number_input("# of months ", min_value=1, max_value=12, value=12)
        quality_2021 = st.selectbox("Quality of Internal Reports ", options=["No Concerns/Moderate", "Unsatisfying", "Professional"])

    # If the form is submitted, show the data
    if st.form_submit_button(label="Submit"):

        st.subheader("Client Information Submitted")
        st.session_state.client_info = {
            2024: {
                "Year": year_2023,
                "Month": month_2023,
                "Type of FS": type_fs_2023,
                "# of months": months_2023,
                "Quality of Internal Reports": quality_2023
            },
            2023: {
                "Year": year_2022,
                "Month": month_2022,
                "Type of FS": type_fs_2022,
                "# of months": months_2022,
                "Quality of Internal Reports": quality_2022
            },
            2022: {
                "Year": year_2021,
                "Month": month_2021,
                "Type of FS": type_fs_2021,
                "# of months": months_2021,
                "Quality of Internal Reports": quality_2021
            }
        }

        others = st.session_state.form_data2
        calc = calculations()
        # print(others)
        results = json.loads(calc.other_calculation(json.dumps(others)))
        # print(results)

        with open('input_data22.json', 'r') as file:
            input_data22 = json.load(file)
        with open('input_data23.json', 'r') as file:
            input_data23 = json.load(file)
        with open('input_data24.json', 'r') as file:
            input_data24 = json.load(file)

        fin = financial_calculations()
        Financial_score = fin.calculate_score(st.session_state.client_info, reporting_year, input_data22, input_data23, input_data24)

        col1, col2  = st.columns(2)
        with col1:
            srr = results["Ownership / Management"] + results["Business / Activity"] + results["Company's Credit Bureau Reports"] + Financial_score
            a = (results["Support Factors"] - 2)
            b = (results["Warning Signals"] - 4)
            print(srr,a,b)
            st.success(f"Ownership / Management (25) : {results["Ownership / Management"]}")
            st.success(f"Business / Activity (30) : {results["Business / Activity"]}")
            st.success(f"Company's Credit Bureau Reports (10) : {results["Company's Credit Bureau Reports"]}")
            st.success(f"Support Factor : {a}")
            st.success(f"Warning Signals : {b}")
            st.success(f"Financials (35) : {Financial_score}")

        with col2:
            NUMBER = abs(((a+b)*abs(srr) + srr))
            def get_grade(score):
                if 90 <= score <= 100:
                    return 0
                elif 70 <= score < 90:
                    return 1
                elif 60 <= score < 70:
                    return 2
                elif 50 <= score < 60:
                    return 3
                elif 40 <= score < 50:
                    return 4
                elif 0 <= score < 40:
                    return 5
                else:
                    return 6

            # Display submitted data
            st.title(f"Final Risk Rating: {np.round(NUMBER,2)}")
            
            bands = ['A+', 'A', 'B', 'C', 'D', 'R','Something Went Wrong']
            colors = ['black', 'blue', 'green', 'yellow', 'pink', 'red','red']
            index = get_grade(NUMBER)

            selected_band = bands[index]
            selected_color = colors[index]

            st.markdown(f"<h1 style='color:{selected_color}'>{selected_band}</h1>", unsafe_allow_html=True)

        print(st.session_state.client_info)