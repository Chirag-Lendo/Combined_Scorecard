import json
import numpy as np

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
        'Industry': ['Water supply; sewerage, waste management', 'Construction', r'''Public administration and defense; compulsory social security''', 'Other service activities', 'Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use',
                      'Activities of extraterritorial organizations and bodies' ,  'Agriculture, Forestry and Fishing' ,  'Manufacturing' , 'Transportation and storage' , 'Real estate activities' , 'Human health and social work activities' , r'''Wholesale and retail trade; repair of motor vehicles and motorcycles''' , 'Mining and quarrying',
                      'Electricity, gas, steam and air conditioning supply' , 'Accommodation and food service activities', 'Financial and insurance activities' , 'Professional, scientific and technical activities' , 'Administrative and support service activities' , 'Education' , 'Information and Communication' , 'Arts, entertainment and recreation'],
        r'Type of customers (>=70% of sales/receivables to)': ['Consumers or unknown entities', 'Well-known Corporations (Public listed and/or closed)', 'Govt. and Semi Govt. Entities, and well-known Corporation', 'Govt. and Semi Govt. Entities'],
        r'Customers Concentration (80% of sales/receivables to)': ['<=5 Customers', '6 to <20 Customers', '20 Customers or more'],
        'Inventory liquidity/management' : ['Inventory liquidity/management is concerning', 'N.A (Low inventory level or No inventory "Service industry")', 'Level of liquidity/management is uncertain', 'Majority is Ready for sale with proper management system'],
        'Access to additional Fund' : ['No access (no support from owners/related parties or access to FI)', 'Proven access to FI', 'Proven support from owners/related parties']
    },
    "Company's Credit Bureau Reports": {
        'Repayment History': ['Defaults, or PD above 90 days', '30 days to 90 days PDs', 'PD below 30 days', 'No Funded facilities or relationship for <2 year with no PD', 'Funded facilities with No PD (relationship >2 year)'],
        'Returned Cheques': ['Unsettled bounced cheques with court cases', 'Unsettled bounced cheques (below 1 year) with no court cases', 'Unsettled bounced cheques (older than 1 years) with no court cases', 'No unsettled bounced cheques']
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

form_values = {
    'Ownership / Management': {
        'Legal Structure': [-1.5, -1.5 , 0 , 3 , 4.5 , 6],
        'Succession Risk': [-1.25, 1.25 , 2.5 , 5],
        '''Owners' experience''': [-1.25 , 1.25 , 2.5 , 3.75 , 5],
        '''Management's experience''': [3 , 1.5 , 3],
        '''Credit History (owners / Management)''': [-3, 0, 4.5, 6]
    },
    'Business / Activity': {
        'Years in Business (for the current business field)': [-1, 1.4, 3, 4],
        'Netaqat': [-4, -2, 0, 2],
        'Markets': [-1.5, 1.5, 3],
        'Industry': [2.31, 2.31, 2.31, 2.31, 2.31, 2.31, 3.5, 3.5, 3.5, 3.5, 3.5, 4.69, 5.81, 5.81, 5.81, 5.81, 5.81, 5.81, 5.81, 7, 7],
        r'''Type of customers (>=70% of sales/receivables to)''': [2, 3, 3.6, 4],
        r'''Customers Concentration (80% of sales/receivables to)''': [1.25, 3.75, 5],
        'Inventory liquidity/management': [-3, 3, 1.5, 3],
        'Access to additional Fund': [0, 1, 2]
    },
    "Company's Credit Bureau Reports": {
        'Repayment History': [-35, -14, -7, 0, 7],
        'Returned Cheques': [-3, -1.5, -0.75, 3]
    },
    'Support Factors': {
        'Control over cash flow': [1, 1.01, 1.05, 1.25],
        'Relationship with Lendo': [1, 0.75, 1.05, 1.15]
    },
    'Warning Signals': {
        'Change in Ownership': [0.9, 1],
        'Change in Management': [ 0.95, 1],
        'Breach in financial covenants': [0.9, 1],
        'Delayed AFS for >7 months from End of reporting period': [0.85, 1]
    }
}

field_names = ['Ownership / Management', 'Business / Activity', "Company's Credit Bureau Reports", 'Support Factors', 'Warning Signals']

other_values = {
    'Ownership / Management':0,
    'Business / Activity':0,
    "Company's Credit Bureau Reports":0,
    'Support Factors':0,
    'Warning Signals':0,
    'final rating':0,
}

output_values = {
    'Ownership / Management': {
        'Legal Structure': 0,
        'Succession Risk': 0,
        '''Owners' experience''': 0,
        '''Management's experience''': 0,
        '''Credit History (owners / Management)''': 0
    },
    'Business / Activity': {
        'Years in Business (for the current business field)': 0,
        'Netaqat': 0,
        'Markets': 0,
        'Industry': 0,
        r'Type of customers (>=70% of sales/receivables to)': 0,
        r'Customers Concentration (80% of sales/receivables to)': 0,
        'Inventory liquidity/management': 0,
        'Access to additional Fund': 0
    },
    "Company's Credit Bureau Reports": {
        'Repayment History': 0,
        'Returned Cheques': 0
    },
    'Support Factors': {
        'Control over cash flow': 0,
        'Relationship with Lendo':0
    },
    'Warning Signals': {
        'Change in Ownership': 0,
        'Change in Management': 0,
        'Breach in financial covenants': 0,
        'Delayed AFS for >7 months from End of reporting period': 0
    }
}

from Finance import financial_calculations

class calculations:

    def __init__(self):
        pass

    def other_calculation(self , x):

        data = json.loads(x)

        financial = 20

        for i in range(len(field_names)):

            list_names = list(form_fields[field_names[i]].keys())
            score  = 0

            for j in range(len(list_names)):

                ind = form_fields[field_names[i]][list_names[j]].index(data[field_names[i]][list_names[j]])
                
                # if (i == 0 and j == 3):
                output_values[field_names[i]][list_names[j]] = form_values[field_names[i]][list_names[j]][ind] #output_values['Ownership / Management']['''Management's experience''']
                    # print(ind , field_names[i] , list_names[j])
                    # print(form_values[field_names[i]][list_names[j]])
                # else:
                #     output_values[field_names[i]][list_names[j]] = form_values[field_names[i]][list_names[j]][ind]

                score += output_values[field_names[i]][list_names[j]]

            if i<3:
                other_values[field_names[i]] = score
            else:
                other_values[field_names[i]] = score #-len(form_fields[field_names[i]])

        # print(output_values)
        SRR = other_values['Ownership / Management'] + other_values['Business / Activity'] + other_values["Company's Credit Bureau Reports"] + financial

        if SRR > 0:
            other_values['final rating'] = (1+other_values['Support Factors'] + other_values['Warning Signals'])* SRR
        else:
            other_values['final rating'] = ((other_values['Support Factors'] + other_values['Warning Signals'])* (-SRR))+SRR

        return json.dumps(other_values)