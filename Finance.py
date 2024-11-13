import json
import numpy as np
import pandas as pd        

#  https://gitlab.swifty.ltd/

class financial_calculations:

    def __init__(self):
        pass

    def financial_calculations(self, data22, data23, data24):

        data22 = {key + "  ": value for key, value in data22.items()}
        # data23 = {key + "": value for key, value in data23.items()}
        data24 = {key + " ": value for key, value in data24.items()}

        

        data22['Current Assets  ']['Trade Receivables - Net'] = data22['Current Assets  ']['Trade Receivables - Gross'] - data22['Current Assets  ']['Provision']
        data22['Current Assets  ']['Inventory - Net'] = data22['Current Assets  ']['Inventory - Gross'] - data22['Current Assets  ']['Slow-Moving assets provision']
        data22['Current Assets  ']['Total Current Assets'] = int(np.array(list(data22['Current Assets  '].values())).sum()) - data22['Current Assets  ']['Trade Receivables - Gross'] - data22['Current Assets  ']['Provision'] - data22['Current Assets  ']['Inventory - Gross'] - data22['Current Assets  ']['Slow-Moving assets provision']

        data23['Current Assets']['Trade Receivables - Net'] = data23['Current Assets']['Trade Receivables - Gross'] - data23['Current Assets']['Provision']
        data23['Current Assets']['Inventory - Net'] = data23['Current Assets']['Inventory - Gross'] - data23['Current Assets']['Slow-Moving assets provision']
        data23['Current Assets']['Total Current Assets'] = int(np.array(list(data23['Current Assets'].values())).sum()) - data23['Current Assets']['Trade Receivables - Gross'] - data23['Current Assets']['Provision'] - data23['Current Assets']['Inventory - Gross'] - data23['Current Assets']['Slow-Moving assets provision']

        data24['Current Assets ']['Trade Receivables - Net'] = data24['Current Assets ']['Trade Receivables - Gross'] - data24['Current Assets ']['Provision']
        data24['Current Assets ']['Inventory - Net'] = data24['Current Assets ']['Inventory - Gross'] - data24['Current Assets ']['Slow-Moving assets provision']
        data24['Current Assets ']['Total Current Assets'] = int(np.array(list(data24['Current Assets '].values())).sum()) - data24['Current Assets ']['Trade Receivables - Gross'] - data24['Current Assets ']['Provision'] - data24['Current Assets ']['Inventory - Gross'] - data24['Current Assets ']['Slow-Moving assets provision']
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # data22['Non Current Assets  ']['Net Fixed assets'] = int(np.array(list(data22['Non Current Assets  '].values()))[:5].sum()) - data22['Non Current Assets  ']['Depreciation']
        # data23['Non Current Assets']['Net Fixed assets'] = int(np.array(list(data23['Non Current Assets'].values()))[:5].sum()) - data23['Non Current Assets']['Depreciation']
        # data24['Non Current Assets ']['Net Fixed assets'] = int(np.array(list(data24['Non Current Assets '].values()))[:5].sum()) - data24['Non Current Assets ']['Depreciation']

        # data22['Non Current Assets  ']['Total Fixed Assets'] = data22['Non Current Assets  ']['Net Fixed assets'] + data22['Non Current Assets  ']['Capital work in progress'] + data22['Non Current Assets  ']['Investment in Subsidiaries'] + data22['Non Current Assets  ']['Other Investments'] + data22['Non Current Assets  ']['Intangible Assets'] + data22['Non Current Assets  ']['Other Non-Current Assets']
        # data23['Non Current Assets']['Total Fixed Assets'] = data23['Non Current Assets']['Net Fixed assets'] + data23['Non Current Assets']['Capital work in progress'] + data23['Non Current Assets']['Investment in Subsidiaries'] + data23['Non Current Assets']['Other Investments'] + data23['Non Current Assets']['Intangible Assets'] + data23['Non Current Assets']['Other Non-Current Assets']
        # data24['Non Current Assets ']['Total Fixed Assets'] = data24['Non Current Assets ']['Net Fixed assets'] + data24['Non Current Assets ']['Capital work in progress'] + data24['Non Current Assets ']['Investment in Subsidiaries'] + data24['Non Current Assets ']['Other Investments'] + data24['Non Current Assets ']['Intangible Assets'] + data24['Non Current Assets ']['Other Non-Current Assets']
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        total_assets22 = data22['Current Assets  ']['Total Current Assets'] + data22['Non Current Assets  ']['Total Fixed Assets']
        total_assets23 = data23['Current Assets']['Total Current Assets'] + data23['Non Current Assets']['Total Fixed Assets']
        total_assets24 = data24['Current Assets ']['Total Current Assets'] + data24['Non Current Assets ']['Total Fixed Assets']
#--------------------------------------------------------------------------------------------------------------------------------------------------
        data22['Current Liabilities  ']['Total Current Liabilities'] = int(np.array(list(data22['Current Liabilities  '].values())).sum())
        data23['Current Liabilities']['Total Current Liabilities'] = int(np.array(list(data23['Current Liabilities'].values())).sum())
        data24['Current Liabilities ']['Total Current Liabilities'] = int(np.array(list(data24['Current Liabilities '].values())).sum())

        data22['Non Current Liabilities  ']['Total Non Current Liabilities'] = int(np.array(list(data22['Non Current Liabilities  '].values())).sum())
        data23['Non Current Liabilities']['Total Non Current Liabilities'] = int(np.array(list(data23['Non Current Liabilities'].values())).sum())
        data24['Non Current Liabilities ']['Total Non Current Liabilities'] = int(np.array(list(data24['Non Current Liabilities '].values())).sum())
#--------------------------------------------------------------------------------------------------------------------------------------------------
        total_liabilities22 = data22['Current Liabilities  ']['Total Current Liabilities'] + data22['Non Current Liabilities  ']['Total Non Current Liabilities']
        total_liabilities23 = data23['Current Liabilities']['Total Current Liabilities'] + data23['Non Current Liabilities']['Total Non Current Liabilities']
        total_liabilities24 = data24['Current Liabilities ']['Total Current Liabilities'] + data24['Non Current Liabilities ']['Total Non Current Liabilities']
#--------------------------------------------------------------------------------------------------------------------------------------------------
        data22['Shareholders Equity  ']['Total Shareholders Equity'] = int(np.array(list(data22['Shareholders Equity  '].values())).sum())
        data23['Shareholders Equity']['Total Shareholders Equity'] = int(np.array(list(data23['Shareholders Equity'].values())).sum())
        data24['Shareholders Equity ']['Total Shareholders Equity'] = int(np.array(list(data24['Shareholders Equity '].values())).sum())

        total_equity_liabilities22 = data22['Shareholders Equity  ']['Total Shareholders Equity']+ total_liabilities22
        total_equity_liabilities23 = data23['Shareholders Equity']['Total Shareholders Equity'] + total_liabilities23
        total_equity_liabilities24 = data24['Shareholders Equity ']['Total Shareholders Equity'] + total_liabilities24
#--------------------------------------------------------------------------------------------------------------------------------------------------

        balance_sheet = {2022:{}, 2023:{}, 2024:{}}

        balance_sheet[2022]['Current Assets  '] = [data22['Current Assets  '], {key : value*100 / total_assets22 if total_assets22!=0 else -1 for key, value in data22['Current Assets  '].items()}, {key:-1 for key,value in data22['Current Assets  '].items()}]
        balance_sheet[2023]['Current Assets'] = [data23['Current Assets'], {key : value*100 / total_assets23 if total_assets23!=0 else -1 for key, value in data23['Current Assets'].items()}, {key: 100*(value - data22['Current Assets  '][key])/data22['Current Assets  '][key] if data22['Current Assets  '][key]!=0 else -1 for key,value in data23['Current Assets'].items()}]
        balance_sheet[2024]['Current Assets '] = [data24['Current Assets '], {key : value*100 / total_assets24 if total_assets24!=0 else -1 for key, value in data24['Current Assets '].items()}, {key: 100*(value - data23['Current Assets'][key])/data23['Current Assets'][key] if data23['Current Assets'][key]!=0 else -1 for key,value in data24['Current Assets '].items()}]

        balance_sheet[2022]['Non Current Assets  '] = [data22['Non Current Assets  '], {key : value*100 / total_assets22 if total_assets22!=0 else -1 for key, value in data22['Non Current Assets  '].items()}, {key:-1 for key,value in data22['Current Assets  '].items()}]
        balance_sheet[2023]['Non Current Assets'] = [data23['Non Current Assets'], {key : value*100 / total_assets23 if total_assets23!=0 else -1 for key, value in data23['Non Current Assets'].items()}, {key: 100*(value - data22['Non Current Assets  '][key])/data22['Non Current Assets  '][key] if data22['Non Current Assets  '][key]!=0 else -1 for key,value in data23['Non Current Assets'].items()}]
        balance_sheet[2024]['Non Current Assets '] = [data24['Non Current Assets '], {key : value*100 / total_assets24 if total_assets24!=0 else -1 for key, value in data24['Non Current Assets '].items()}, {key: 100*(value - data23['Non Current Assets'][key])/data23['Non Current Assets'][key] if data23['Non Current Assets'][key]!=0 else -1 for key,value in data24['Non Current Assets '].items()}]

        balance_sheet[2022]['Current Liabilities  '] = [data22['Current Liabilities  '], {key : value*100 / total_liabilities22 if total_liabilities22!=0 else -1 for key, value in data22['Current Liabilities  '].items()}, {key:-1 for key,value in data22['Current Assets  '].items()}]
        balance_sheet[2023]['Current Liabilities'] = [data23['Current Liabilities'], {key : value*100 / total_liabilities23 if total_liabilities23!=0 else -1 for key, value in data23['Current Liabilities'].items()}, {key: 100*(value - data22['Current Liabilities  '][key])/data22['Current Liabilities  '][key] if data22['Current Liabilities  '][key]!=0 else -1 for key,value in data23['Current Liabilities'].items()}]
        balance_sheet[2024]['Current Liabilities '] = [data24['Current Liabilities '], {key : value*100 / total_liabilities24 if total_liabilities24!=0 else -1 for key, value in data24['Current Liabilities '].items()}, {key: 100*(value - data23['Current Liabilities'][key])/data23['Current Liabilities'][key] if data23['Current Liabilities'][key]!=0 else -1 for key,value in data24['Current Liabilities '].items()}]

        balance_sheet[2022]['Non Current Liabilities  '] = [data22['Non Current Liabilities  '], {key : value*100 / total_liabilities22 if total_liabilities22!=0 else -1 for key, value in data22['Non Current Liabilities  '].items()},{-1 for key,value in data22['Current Assets  '].items()}]
        balance_sheet[2023]['Non Current Liabilities'] = [data23['Non Current Liabilities'], {key : value*100 / total_liabilities23 if total_liabilities23!=0 else -1 for key, value in data23['Non Current Liabilities'].items()},{key: 100*(value - data22['Non Current Liabilities  '][key])/data22['Non Current Liabilities  '][key] if data22['Non Current Liabilities  '][key]!=0 else -1 for key,value in data23['Non Current Liabilities'].items()}]
        balance_sheet[2024]['Non Current Liabilities '] = [data24['Non Current Liabilities '], {key : value*100 / total_liabilities24 if total_liabilities24!=0 else -1 for key, value in data24['Non Current Liabilities '].items()}, {key: 100*(value - data23['Non Current Liabilities'][key])/data23['Non Current Liabilities'][key] if data23['Non Current Liabilities'][key]!=0 else -1 for key,value in data24['Non Current Liabilities '].items()}]

        balance_sheet[2022]['Shareholders Equity  '] = [data22['Shareholders Equity  '], {key : value*100 / total_equity_liabilities22 if total_equity_liabilities22!=0 else -1 for key, value in data22['Shareholders Equity  '].items()}, {-1 for key,value in data22['Current Assets  '].items()}]
        balance_sheet[2023]['Shareholders Equity'] = [data23['Shareholders Equity'], {key : value*100 / total_equity_liabilities23 if total_equity_liabilities23!=0 else -1 for key, value in data23['Shareholders Equity'].items()}, {key: 100*(value - data22['Shareholders Equity  '][key])/data22['Shareholders Equity  '][key] if data22['Shareholders Equity  '][key]!=0 else -1 for key,value in data23['Shareholders Equity'].items()}]
        balance_sheet[2024]['Shareholders Equity '] = [data24['Shareholders Equity '], {key : value*100 / total_equity_liabilities24 if total_equity_liabilities24!=0 else -1 for key, value in data24['Shareholders Equity '].items()}, {key: 100*(value - data23['Shareholders Equity'][key])/data23['Shareholders Equity'][key] if data23['Shareholders Equity'][key]!=0 else -1 for key,value in data24['Shareholders Equity '].items()}]
#--------------------------------------------------------------------------------------------------------------------------------------------------
        data22['PnL + Cash Flow  ']['Gross Profit (loss)'] = data22['PnL + Cash Flow  ']['Revenues'] - data22['PnL + Cash Flow  ']['COGS'] - data22['PnL + Cash Flow  ']['Depreciation']

        try:
            data22['PnL + Cash Flow  ']['Gross Profit Margin'] = 100*(data22['PnL + Cash Flow  ']['Gross Profit (loss)'] / data22['PnL + Cash Flow  ']['Revenues'])
        except:
            data22['PnL + Cash Flow  ']['Gross Profit Margin'] = -1
  
        data22['PnL + Cash Flow  ']['Operating Profit (loss)'] = data22['PnL + Cash Flow  ']['Gross Profit (loss)'] - data22['PnL + Cash Flow  ']['Operating Expenses'] - data22['PnL + Cash Flow  ']['G&A'] - data22['PnL + Cash Flow  ']['Selling Expense'] - data22['PnL + Cash Flow  ']['Depreciation/Amortizatoin']  + data22['PnL + Cash Flow  ']['Other Operating Income']
        data22['PnL + Cash Flow  ']['Net Profit'] = data22['PnL + Cash Flow  ']['Operating Profit (loss)'] - data22['PnL + Cash Flow  ']['Finance Cost (interest)'] + data22['PnL + Cash Flow  ']['Income (loss) from Investments'] - data22['PnL + Cash Flow  ']['Taxes/Zakat']

        try:
            data22['PnL + Cash Flow  ']['Net Profit Margin'] = 100*(data22['PnL + Cash Flow  ']['Net Profit'] / data22['PnL + Cash Flow  ']['Revenues'])
        except:
            data22['PnL + Cash Flow  ']['Net Profit Margin'] = -1

        data22['PnL + Cash Flow  ']['EBIT'] = data22['PnL + Cash Flow  ']['Finance Cost (interest)'] + data22['PnL + Cash Flow  ']['Taxes/Zakat'] + data22['PnL + Cash Flow  ']['Net Profit']
        data22['PnL + Cash Flow  ']['EBITDA'] = data22['PnL + Cash Flow  ']['EBIT'] + data22['PnL + Cash Flow  ']['Depreciation'] + data22['PnL + Cash Flow  ']['Depreciation/Amortizatoin']

#--------------------------------------------------------------------------------------------------------------------------------------------------
        data23['PnL + Cash Flow']['Gross Profit (loss)'] = data23['PnL + Cash Flow']['Revenues'] - data23['PnL + Cash Flow']['COGS'] - data23['PnL + Cash Flow']['Depreciation']

        try:
            data23['PnL + Cash Flow']['Gross Profit Margin'] = 100*(data23['PnL + Cash Flow']['Gross Profit (loss)'] / data23['PnL + Cash Flow']['Revenues'])
        except:
            data23['PnL + Cash Flow']['Gross Profit Margin'] = -1

        data23['PnL + Cash Flow']['Operating Profit (loss)'] = data23['PnL + Cash Flow']['Gross Profit (loss)'] + data23['PnL + Cash Flow']['Other Operating Income'] - data23['PnL + Cash Flow']['Operating Expenses'] - data23['PnL + Cash Flow']['G&A'] - data23['PnL + Cash Flow']['Selling Expense'] - data23['PnL + Cash Flow']['Depreciation/Amortizatoin']
        data23['PnL + Cash Flow']['Net Profit'] = data23['PnL + Cash Flow']['Operating Profit (loss)'] - data23['PnL + Cash Flow']['Finance Cost (interest)'] + data23['PnL + Cash Flow']['Income (loss) from Investments']  - data23['PnL + Cash Flow']['Taxes/Zakat']

        try:
            data23['PnL + Cash Flow']['Net Profit Margin'] = 100*(data23['PnL + Cash Flow']['Net Profit'] / data23['PnL + Cash Flow']['Revenues'])
        except:
            data23['PnL + Cash Flow']['Net Profit Margin'] = -1

        data23['PnL + Cash Flow']['EBIT'] = data23['PnL + Cash Flow']['Finance Cost (interest)'] + data23['PnL + Cash Flow']['Taxes/Zakat'] + data23['PnL + Cash Flow']['Net Profit']
        data23['PnL + Cash Flow']['EBITDA'] = data23['PnL + Cash Flow']['EBIT'] + data23['PnL + Cash Flow']['Depreciation'] + data23['PnL + Cash Flow']['Depreciation/Amortizatoin']
#--------------------------------------------------------------------------------------------------------------------------------------------------
        data24['PnL + Cash Flow ']['Gross Profit (loss)'] = data24['PnL + Cash Flow ']['Revenues'] - data24['PnL + Cash Flow ']['COGS'] - data24['PnL + Cash Flow ']['Depreciation']

        try:
            data24['PnL + Cash Flow ']['Gross Profit Margin'] = 100*(data24['PnL + Cash Flow ']['Gross Profit (loss)'] / data24['PnL + Cash Flow ']['Revenues'])
        except:
            data24['PnL + Cash Flow ']['Gross Profit Margin'] = -1

        data24['PnL + Cash Flow ']['Operating Profit (loss)'] = data24['PnL + Cash Flow ']['Gross Profit (loss)'] + data24['PnL + Cash Flow ']['Other Operating Income'] - data24['PnL + Cash Flow ']['Operating Expenses'] - data24['PnL + Cash Flow ']['G&A'] - data24['PnL + Cash Flow ']['Selling Expense'] - data24['PnL + Cash Flow ']['Depreciation/Amortizatoin']
        data24['PnL + Cash Flow ']['Net Profit'] = data24['PnL + Cash Flow ']['Operating Profit (loss)'] - data24['PnL + Cash Flow ']['Finance Cost (interest)'] + data24['PnL + Cash Flow ']['Income (loss) from Investments']  - data24['PnL + Cash Flow ']['Taxes/Zakat']

        try:
            data24['PnL + Cash Flow ']['Net Profit Margin'] = 100*(data24['PnL + Cash Flow ']['Net Profit'] / data24['PnL + Cash Flow ']['Revenues'])
        except:
            data24['PnL + Cash Flow ']['Net Profit Margin'] = -1

        data24['PnL + Cash Flow ']['EBIT'] = data24['PnL + Cash Flow ']['Finance Cost (interest)'] + data24['PnL + Cash Flow ']['Taxes/Zakat'] + data24['PnL + Cash Flow ']['Net Profit']
        data24['PnL + Cash Flow ']['EBITDA'] = data24['PnL + Cash Flow ']['EBIT'] + data24['PnL + Cash Flow ']['Depreciation'] + data24['PnL + Cash Flow ']['Depreciation/Amortizatoin']
## --------------------------------------------------------------------------------------------------------------------------------------------------
        PnL = {2022:{}, 2023:{}, 2024:{}}

        # print(PnL[2022])
        # PnL[2022] = [data22['PnL + Cash Flow  '], {key: (value)*100/data22['PnL + Cash Flow  ']['Revenues'] if data22['PnL + Cash Flow  ']['Revenues'] != 0 else -1 for key,value in data22['PnL + Cash Flow  '].items()} , {key: -1 for key,value in data22['PnL + Cash Flow  '].items()}]
        # PnL[2023] = [data23['PnL + Cash Flow'], {key: (value)*100/data23['PnL + Cash Flow']['Revenues'] if data23['PnL + Cash Flow']['Revenues'] != 0 else -1 for key,value in data23['PnL + Cash Flow'].items()} , {key: (value - data22['PnL + Cash Flow  '][key])*100 / data22['PnL + Cash Flow  '][key] if data22['PnL + Cash Flow  '][key] != 0 else -1 for key,value in data23['PnL + Cash Flow'].items()}]
        # PnL[2024] = [data24['PnL + Cash Flow '], {key: (value)*100/data24['PnL + Cash Flow ']['Revenues'] if data24['PnL + Cash Flow ']['Revenues'] != 0 else -1 for key,value in data24['PnL + Cash Flow '].items()} , {key: (value - data23['PnL + Cash Flow'][key])*100 / data23['PnL + Cash Flow'][key] if data23['PnL + Cash Flow'][key] != 0 else -1 for key,value in data24['PnL + Cash Flow '].items()}]

        with open('input_data22.json', 'w') as file:
            json.dump({key.rstrip(): value for key, value in data22.items()}, file, indent=4)
        with open('input_data23.json', 'w') as file:
            json.dump({key.rstrip(): value for key, value in data23.items()}, file, indent=4)
        with open('input_data24.json', 'w') as file:
            json.dump({key.rstrip(): value for key, value in data24.items()}, file, indent=4)
        
        ratios = {
            2022: {
            "Liquidity Ratios": {
                "Current Ratio":0,
                "Quick Ratio":0,
                "Cash flow from oerating activities":0,
                "Working Capital - Net (SAR 000)":0
            },
            "Leverage Financial ratios": {
                "Debt Ratio":0,
                "External Debt / Sales ratio":0,
                "Leverage Ratio":0,
                "Interest Coverage":0,
                "Gearing Ratio":0,
                "Debt Service (SAR 000)":0,
                "DSCR":0
            },
            "Activity Ratios": {
                "Receivables Days":0,
                "Inventory Days":0,
                "Payables Days":0,
                "CCC":0
            },
            "Performance Ratios": {
                "Gross Profit Margin (GPM)":0,
                "Operating Profit Margin (OPM)":0,
                "Net Profit Margin (NPM)":0,
                "Revenues Growth":0,
                "GP Growth":0,
                "GPM Growth":0,
                "OP Growth":0,
                "NP Growth":0,
                "NPM Growth":0
            }
            },
            2023: {
            "Liquidity Ratios": {
                "Current Ratio":0,
                "Quick Ratio":0,
                "Cash flow from oerating activities":0,
                "Working Capital - Net (SAR 000)":0
            },
            "Leverage Financial Ratios": {
                "Debt Ratio":0,
                "External Debt / Sales ratio":0,
                "Leverage Ratio":0,
                "Interest Coverage":0,
                "Gearing Ratio":0,
                "Debt Service (SAR 000)":0,
                "DSCR":0
            },
            "Activity Ratios": {
                "Receivables Days":0,
                "Inventory Days":0,
                "Payables Days":0,
                "CCC":0
            },
            "Performance Ratios": {
                "Gross Profit Margin (GPM)":0,
                "Operating Profit Margin (OPM)":0,
                "Net Profit Margin (NPM)":0,
                "Revenues Growth":0,
                "GP Growth":0,
                "GPM Growth":0,
                "OP Growth":0,
                "NP Growth":0,
                "NPM Growth":0
            }
            },
            2024: {
            "Liquidity Ratios": {
                "Current Ratio":0,
                "Quick Ratio":0,
                "Cash flow from oerating activities":0,
                "Working Capital - Net (SAR 000)":0
            },
            "Leverage Financial Ratios": {
                "Debt Ratio":0,
                "External Debt / Sales ratio":0,
                "Leverage Ratio":0,
                "Interest Coverage":0,
                "Gearing Ratio":0,
                "Debt Service (SAR 000)":0,
                "DSCR":0
            },
            "Activity Ratios": {
                "Receivables Days":0,
                "Inventory Days":0,
                "Payables Days":0,
                "CCC":0
            },
            "Performance Ratios": {
                "Gross Profit Margin (GPM)":0,
                "Operating Profit Margin (OPM)":0,
                "Net Profit Margin (NPM)":0,
                "Revenues Growth":0,
                "GP Growth":0,
                "GPM Growth":0,
                "OP Growth":0,
                "NP Growth":0,
                "NPM Growth":0
            }
        }}

        def calculate_ratios(data,dataP,year):

            # print(year)

            if list(data.keys())[0] == 'Current Assets  ':
                x = "  "
            if list(data.keys())[0] == 'Current Assets':
                x = ""
                y = "  "
            if list(data.keys())[0] == 'Current Assets ':
                x = " "
                y = ""

            current_assets = data['Current Assets'+x]['Total Current Assets']
            non_current_assets = data['Non Current Assets'+x]['Total Fixed Assets']
            total_assets = current_assets + non_current_assets

            current_liabilities = data['Current Liabilities'+x]['Total Current Liabilities']  # Make positive
            non_current_liabilities = data['Non Current Liabilities'+x]['Total Non Current Liabilities']  # Make positive
            total_liabilities = current_liabilities + non_current_liabilities

            total_shareholder_equity = data['Shareholders Equity'+x]['Total Shareholders Equity']

            revenues = data['PnL + Cash Flow'+x]['Revenues']
            net_profit = data['PnL + Cash Flow'+x]['Net Profit']
            cash_flow = data['PnL + Cash Flow'+x]['Net Cash from Operating Activities']
            
            def calculate_ICR(c23, c15):
                if c23 < 0:
                    return 0
                elif c15 == 0:
                    return 0
                elif c15 >= 0:
                    return data['PnL + Cash Flow'+x]['EBIT'] / data['PnL + Cash Flow'+x]['Finance Cost (interest)']
                
            def calculate_DSCR(c24, c12):
                if c24 < 0:
                    return 0
                elif c12 == 0:
                    return 0
                elif c24 > 0:
                    return c24 / c12
                
            ratios = {
                "Liquidity Ratios": {
                    "Current Ratio": current_assets / current_liabilities if current_liabilities != 0 else -1,
                    "Quick Ratio": (data['Current Assets'+x]['Cash & Cash Equivalents'] + data['Current Assets'+x]['Marketable Securities'] +data['Current Assets'+x]['Trade Receivables - Net']) / current_liabilities if current_liabilities != 0 else -1,
                    "Cash flow from operating activities": cash_flow,
                    "Working Capital - Net (SAR 000)": current_assets - current_liabilities,
                },
                "Leverage Financial Ratios": {
                    "Debt Ratio": total_liabilities / (total_assets) if total_assets != 0 else -1,
                    "External Debt / Sales ratio": data['PnL + Cash Flow'+x]['Total loans as per SIMAH'] / revenues if revenues != 0 else -1,
                    "Leverage Ratio": total_liabilities / total_shareholder_equity if total_shareholder_equity != 0 else -1,
                    "Interest Coverage": calculate_ICR(data['PnL + Cash Flow'+x]['EBIT'], data['PnL + Cash Flow'+x]['Finance Cost (interest)']),
                    "Gearing Ratio": (data['Current Liabilities'+x]['Short Term Loans - Banks'] + data['Current Liabilities'+x]['Short Term Loans - NBFI'] + data['Non Current Liabilities'+x]['TL - Banks'] + data['Non Current Liabilities'+x]['TL - NBFI']) / (total_shareholder_equity) if (total_shareholder_equity) != 0 else -1,
                    "Debt Service (SAR 000)": data['PnL + Cash Flow'+x]['Finance Cost (interest)'] + data['Current Liabilities'+x]['Short Term Loans - Banks'] + data['Current Liabilities'+x]['Short Term Loans - NBFI'],
                },
                "Activity Ratios": {
                    "Receivables Days": 365*data['Current Assets'+x]['Trade Receivables - Gross']/(data['PnL + Cash Flow'+x]['Revenues']) if data['PnL + Cash Flow'+x]['Revenues'] != 0 else -1,
                    "Inventory Days": 365*data['Current Assets'+x]['Inventory - Gross']/(data['PnL + Cash Flow'+x]['COGS']) if data['PnL + Cash Flow'+x]['COGS'] != 0 else -1,
                    "Payables Days":  365*data['Current Liabilities'+x]['Trade Payables']/(data['PnL + Cash Flow'+x]['COGS']) if data['PnL + Cash Flow'+x]['COGS'] != 0 else -1,
                },
                "Performance Ratios": {
                    "Gross Profit Margin (GPM)": (data['PnL + Cash Flow'+x]['Gross Profit (loss)'] / revenues) * 100 if revenues != 0 else -1,
                    "Operating Profit Margin (OPM)": (data['PnL + Cash Flow'+x]['Operating Profit (loss)'] / revenues) * 100 if revenues != 0 else -1,
                    "Net Profit Margin (NPM)": (net_profit / revenues) * 100 if revenues != 0 else -1,

                    "Revenues Growth": None if year==2022 else (data['PnL + Cash Flow' + x]['Revenues'] - dataP['PnL + Cash Flow' + y]['Revenues']) * 100 / dataP['PnL + Cash Flow' + y]['Revenues'],
                    # None if (dataP is None or not dataP.get('PnL + Cash Flow' + y) or dataP['PnL + Cash Flow' + y]['Revenues'] == 0)
                    # else (data['PnL + Cash Flow' + x]['Revenues'] - dataP['PnL + Cash Flow' + y]['Revenues']) * 100 / dataP['PnL + Cash Flow' + y]['Revenues'],

                    "GP Growth": None if year==2022
                    else abs((data['PnL + Cash Flow' + x]['Gross Profit (loss)'] - dataP['PnL + Cash Flow' + y]['Gross Profit (loss)']) * 100 / dataP['PnL + Cash Flow' + y]['Gross Profit (loss)']),

                    "GPM Growth": None if year==2022
                    else abs((data['PnL + Cash Flow' + x]['Gross Profit Margin'] - dataP['PnL + Cash Flow' + y]['Gross Profit Margin']) * 100 / dataP['PnL + Cash Flow' + y]['Gross Profit Margin']),

                    "OP Growth": None if year==2022
                    else abs((data['PnL + Cash Flow' + x]['Operating Profit (loss)'] - dataP['PnL + Cash Flow' + y]['Operating Profit (loss)']) * 100 / dataP['PnL + Cash Flow' + y]['Operating Profit (loss)']),

                    "NP Growth": None if year==2022
                    else abs((data['PnL + Cash Flow' + x]['Net Profit'] - dataP['PnL + Cash Flow' + y]['Net Profit']) * 100 / dataP['PnL + Cash Flow' + y]['Net Profit']),

                    "NPM Growth": None if year==2022
                    else abs((data['PnL + Cash Flow' + x]['Net Profit Margin'] - dataP['PnL + Cash Flow' + y]['Net Profit Margin']) * 100 / dataP['PnL + Cash Flow' + y]['Net Profit Margin'])}} 

            ratios['Activity Ratios']['CCC'] = ratios['Activity Ratios']['Receivables Days'] + ratios['Activity Ratios']['Inventory Days'] - ratios['Activity Ratios']['Payables Days']
            ratios['Leverage Financial Ratios']['DSCR'] = calculate_DSCR(data['PnL + Cash Flow'+x]['EBITDA'], ratios['Leverage Financial Ratios']['Debt Service (SAR 000)'])
            import pandas as pd
            # print(ratios)

            return ratios

        ratios[2022] = calculate_ratios(data22,None,2022)
        ratios[2023] = calculate_ratios(data23,data22,2023)
        ratios[2024] = calculate_ratios(data24,data23,2024)
        # with open('balance_sheet0.json', 'w') as file:
        #     json.dump(balance_sheet, file, indent=4)
        # with open('balance_sheet1.json', 'w') as file:
        #     json.dump(balance_sheet[1], file, indent=4)
        # with open('balance_sheet2.json', 'w') as file:
        #     json.dump(balance_sheet[2], file, indent=4)

        # with open('PnL0.json', 'w') as file:
        #     json.dump(PnL[0], file, indent=4)
        # with open('PnL1.json', 'w') as file:
        #     json.dump(PnL[1], file, indent=4)
        # with open('Pn:2.json', 'w') as file:
        #     json.dump(PnL[2], file, indent=4)

        # with open('ratios.json', 'w') as file:
        #     json.dump(ratios[0], file, indent=4)
        return balance_sheet, PnL, ratios

    def calculate_revenue_growth(self, sheet_b3, balance_sheet_n2, ratios_e21, ratios_d21, ratios_c21, master_sheet):

        ratios_c21 = ratios_c21/100
        ratios_d21 = ratios_d21/100
        if ratios_e21==None:
            ratios_e21 = 1/100

        print(f"Revenue Growth {ratios_c21,ratios_d21,ratios_e21}")

        if sheet_b3 == balance_sheet_n2:
            if ratios_c21 <= 0 and ratios_d21 <= 0:
                return master_sheet[124]
            elif ratios_c21 < (0.9 - 1) and ratios_d21 > 0:
                return master_sheet[125]
            elif 0 > ratios_c21 >= (0.9 - 1) and ratios_d21 > 0:
                return master_sheet[126]
            elif 0 < ratios_c21 < 0.05:
                return master_sheet[127]
            elif 0.05 <= ratios_c21 <= 0.3:
                return master_sheet[128]
            elif ratios_c21 > 0.3:
                return master_sheet[129]
        else:
            if ratios_d21 < 0 and ratios_e21 < 0:
                return master_sheet[124]
            elif ratios_d21 < (0.9 - 1) and ratios_e21 > 0:
                return master_sheet[125]
            elif 0 > ratios_d21 >= (0.9 - 1) and ratios_e21 > 0:
                return master_sheet[126]
            elif 0 < ratios_d21 < 0.05:
                return master_sheet[127]
            elif 0.05 <= ratios_d21 <= 0.3:
                return master_sheet[128]
            elif ratios_d21 > 0.3:
                return master_sheet[129]

    def calculate_GPM_Change(self, sheet_b3, balance_sheet_n2, ratios_c23, ratios_d23, master_sheet):

        ratios_c23 = ratios_c23/100
        ratios_d23 = ratios_d23/100
        print(f"GPM_Change*****{ratios_c23,ratios_d23}")
        if sheet_b3 == balance_sheet_n2:
            if ratios_c23 < (0.8 - 1):
                return master_sheet[132]
            elif 0 > ratios_c23 >= (0.8 - 1):
                return master_sheet[133]
            elif 0 <= ratios_c23 < 0.03:
                return master_sheet[134]
            elif 0.03 <= ratios_c23 <= 0.2:
                return master_sheet[135]
            elif ratios_c23 > 0.2:
                return master_sheet[136]
        
        else:
            if ratios_d23 < (0.8 - 1):
                return master_sheet[132]
            elif 0 > ratios_d23 >= (0.8 - 1):
                return master_sheet[133]
            elif 0 < ratios_d23 < 0.03:
                return master_sheet[134]
            elif 0.03 <= ratios_d23 <= 0.2:
                return master_sheet[135]
            elif ratios_d23 > 0.2:
                return master_sheet[136]

    def calculate_NPM(self, sheet_b3, balance_sheet_n2, ratios_c20, ratios_d20, master_sheet):

        ratios_c20 = ratios_c20 /100
        ratios_d20 = ratios_d20 / 100
        print(f"NPM*****{ratios_c20,ratios_d20}")
        if sheet_b3 == balance_sheet_n2:
            if ratios_c20 < 0:
                return master_sheet[139]
            elif 0 <= ratios_c20 < 0.05:
                return master_sheet[140]
            elif 0.05 <= ratios_c20 <= 0.15:
                return master_sheet[141]
            elif ratios_c20 > 0.15:
                return master_sheet[142]
        else:
            if ratios_d20 < 0:
                return master_sheet[139]
            elif 0 <= ratios_d20 < 0.05:
                return master_sheet[140]
            elif 0.05 <= ratios_d20 <= 0.15:
                return master_sheet[141]
            elif ratios_d20 > 0.15:
                return master_sheet[142]

    def calculate_change_NPM(self, sheet_b3, balance_sheet_n2, ratios_c20, ratios_d20, master_sheet):

        ratios_c20 = ratios_c20 /100
        ratios_d20 = ratios_d20 / 100
        
        if sheet_b3 == balance_sheet_n2:
            if ratios_c20 < 0:
                return master_sheet[139]
            elif 0 <= ratios_c20 < 0.05:
                return master_sheet[140]
            elif 0.05 <= ratios_c20 <= 0.15:
                return master_sheet[141]
            elif ratios_c20 > 0.15:
                return master_sheet[142]
        else:
            if ratios_d20 < 0:
                return master_sheet[139]
            elif 0 <= ratios_d20 < 0.05:
                return master_sheet[140]
            elif 0.05 <= ratios_d20 <= 0.15:
                return master_sheet[141]
            elif ratios_d20 > 0.15:
                return master_sheet[142]

    def calculate_NPM_Change(self, sheet_b3, balance_sheet_n2, ratios_c26, ratios_d26, master_sheet):

        
        ratios_c26 = ratios_c26/100
        ratios_d26 = ratios_d26/100
        print(f"NPM_Change**********{ratios_c26,ratios_d26}")
        if sheet_b3 == balance_sheet_n2:
            if ratios_c26 < (0.8 - 1):
                return master_sheet[145]
            elif 0 > ratios_c26 >= (0.8 - 1):
                return master_sheet[146]
            elif 0 <= ratios_c26 < 0.03:
                return master_sheet[147]
            elif 0.03 <= ratios_c26 <= 0.2:
                return master_sheet[148]
            elif ratios_c26 > 0.2:
                return master_sheet[149]
        else:
            if ratios_d26 < (0.8 - 1):
                return master_sheet[145]
            elif 0 > ratios_d26 >= (0.8 - 1):
                return master_sheet[146]
            elif 0 < ratios_d26 < 0.03:
                return master_sheet[147]
            elif 0.03 <= ratios_d26 <= 0.2:
                return master_sheet[148]
            elif ratios_d26 > 0.2:
                return master_sheet[149]

    def calculate_cash_flow(self, sheet_b3, balance_sheet_n2, ratios_c5, ratios_d5, master_sheet):


        if sheet_b3 == balance_sheet_n2:
            if ratios_c5 >= 0:
                return master_sheet[153]
            else:
                return master_sheet[152]
        else:
            if ratios_d5 >= 0:
                return master_sheet[153]
            else:
                return master_sheet[152]

    def calculate_current_ratio(self, sheet_b3, balance_sheet_n2, ratios_c3, ratios_d3, master_sheet):

        print(f"*******Current Ratio**********{ratios_c3}**********{ratios_d3}")
        if sheet_b3 == balance_sheet_n2:
            if ratios_c3 < 1:
                return master_sheet[156]
            elif 1 <= ratios_c3 <= 2:
                return master_sheet[157]
            elif ratios_c3 > 2:
                return master_sheet[158]
        else:
            if ratios_d3 < 1:
                return master_sheet[156]
            elif 1 <= ratios_d3 <= 2:
                return master_sheet[157]
            elif ratios_d3 > 2:
                return master_sheet[158]

    def calculate_leveraged_ratio(self, sheet_b3, balance_sheet_n2, ratios_c9, ratios_d9, master_sheet):
        if sheet_b3 == balance_sheet_n2:
            if ratios_c9 > 3 or ratios_c9 < 0:
                return master_sheet[161]
            elif 2 <= ratios_c9 <= 3:
                return master_sheet[162]
            elif 1 <= ratios_c9 < 2:
                return master_sheet[163]
            elif 0 <= ratios_c9 < 1:
                return master_sheet[164]
        else:
            if ratios_d9 > 3 or ratios_d9 < 0:
                return master_sheet[161]
            elif 2 <= ratios_d9 <= 3:
                return master_sheet[162]
            elif 1 <= ratios_d9 < 2:
                return master_sheet[163]
            elif ratios_d9 < 1:
                return master_sheet[164]

    def calculate_ICR0(self, sheet_b3, balance_sheet_n2, ratios_c10, ratios_d10, master_sheet):

        print(f"*******Current ICR*********{ratios_c10}**********{ratios_d10}")
        if sheet_b3 == balance_sheet_n2:
            if ratios_c10 < 1:
                return master_sheet[167]
            elif 1 <= ratios_c10 <= 4:
                return master_sheet[168]
            elif ratios_c10 > 4:
                return master_sheet[169]
        else:
            if ratios_d10 < 1:
                return master_sheet[167]
            elif 1 <= ratios_d10 <= 4:
                return master_sheet[168]
            elif ratios_d10 > 4:
                return master_sheet[169]

    def calculate_DSCR2(self, sheet_b3, balance_sheet_n2, ratios_c13, ratios_d13, master_sheet):

        # if ratios_c13 == None:  # PATCH
        #     return 0
        print(f"***DSCR Ratios****{ratios_c13},{ratios_d13}")
        if sheet_b3 == balance_sheet_n2:
            if ratios_c13 < 1:
                return master_sheet[172]
            elif 1 <= ratios_c13 <= 2:
                return master_sheet[173]
            elif ratios_c13 > 2:
                return master_sheet[174]
        else:
            if ratios_d13 < 1:
                return master_sheet[172] #-2
            elif 1 <= ratios_d13 <= 2:
                return master_sheet[173] #1
            elif ratios_d13 > 2:
                return master_sheet[174] #2

    def calculate_receivable_days(self, sheet_b3, balance_sheet_n2, ratios_c14, ratios_d14, master_sheet):

        print(f"**********{ratios_c14}******{ratios_d14}")
        if sheet_b3 == balance_sheet_n2:
            if ratios_c14 > 270:
                return master_sheet[185]
            elif 180 <= ratios_c14 <= 270:
                return master_sheet[186]
            elif 120 <= ratios_c14 < 180:
                return master_sheet[187]
            elif ratios_c14 < 120:
                return master_sheet[188]
        else:
            if ratios_d14 > 270:
                return master_sheet[185]
            elif 180 <= ratios_d14 <= 270:
                return master_sheet[186]
            elif 120 <= ratios_d14 < 180:
                return master_sheet[187]
            elif ratios_d14 < 120:
                return master_sheet[188]
            
    def calculate_debt_sales_ratio(self, sheet_b3, balance_sheet_n2, ratios_c8, ratios_d8, master_sheet):

        # print(f"**************{ratios_c8}***********{ratios_d8}")
        if sheet_b3 == balance_sheet_n2:
            if ratios_c8 <= 0.25:
                return master_sheet[193]
            elif 0.25 < ratios_c8 <= 0.5:
                return master_sheet[192]
            elif ratios_c8 > 0.5:
                return master_sheet[191]
        else:
            if ratios_d8 <= 0.25:
                return master_sheet[193]
            elif 0.25 < ratios_d8 <= 0.5:
                return master_sheet[192]
            elif ratios_d8 > 0.5:
                return master_sheet[191]
            
    def calculate_auditable_finances(self, sheet_b3, balance_sheet_n2, balance_sheet_n4, balance_sheet_o4, master_sheet):

        if sheet_b3 == balance_sheet_n2:
            if balance_sheet_n4 == "In-house":
                return master_sheet[197]
            elif balance_sheet_n4 == "Projections":
                return master_sheet[196]
            elif balance_sheet_n4 == "Audited":
                return master_sheet[199]
            elif balance_sheet_n4 == "Draft":
                return master_sheet[198]
        else:
            if balance_sheet_o4 == "In-house":
                return master_sheet[197]
            elif balance_sheet_o4 == "Projections":
                return master_sheet[196]
            elif balance_sheet_o4 == "Audited":
                return master_sheet[199]
            elif balance_sheet_o4 == "Draft":
                return master_sheet[198]
        
    def calculate_quality_internal_report(self, sheet_b3, balance_sheet_n2, balance_sheet_n6, balance_sheet_o6, master_sheet):
        if sheet_b3 == balance_sheet_n2:
            if balance_sheet_n6 == "Unsatisfying":
                return master_sheet[202]
            elif balance_sheet_n6 == "No Concerns/Moderate":
                return master_sheet[203]
            elif balance_sheet_n6 == "Professional":
                return master_sheet[204]
        else:
            if balance_sheet_o6 == "Unsatisfying":
                return master_sheet[202]
            elif balance_sheet_o6 == "No Concerns/Moderate":
                return master_sheet[203]
            elif balance_sheet_o6 == "Professional":
                return master_sheet[204]

    def calculate_score(self, client_info, reporting_year, data22, data23, data24):

        balance_sheet, PnL, ratios = self.financial_calculations(data22, data23, data24)
        
        ratios[2024]['Performance Ratios']['Cash flow from operating activities'] = 0
        ratios[2023]['Performance Ratios']['Cash flow from operating activities'] = 0
        ratios[2022]['Performance Ratios']['Cash flow from operating activities'] = 0

        revenue_growth = self.calculate_revenue_growth(reporting_year, client_info[2024]["Year"], ratios[2022]['Performance Ratios']['Revenues Growth'], ratios[2023]['Performance Ratios']['Revenues Growth'], ratios[2024]['Performance Ratios']['Revenues Growth'], {124: -4, 125: -2, 126: -1, 127: 1, 128: 3, 129: 4})
        GPM_Change = self.calculate_GPM_Change(reporting_year, client_info[2024]["Year"], ratios[2024]['Performance Ratios']['GPM Growth'], ratios[2023]['Performance Ratios']['GPM Growth'], {132: -3, 133: -1.5, 134: 0.75, 135: 2.25, 136: 3})
        NPM = self.calculate_NPM(reporting_year, client_info[2024]["Year"], ratios[2024]['Performance Ratios']['Net Profit Margin (NPM)'], ratios[2023]['Performance Ratios']['Net Profit Margin (NPM)'], {139: -6, 140: -0.75, 141: 1.5, 142: 3})
        NPM_Change = self.calculate_NPM_Change(reporting_year, client_info[2024]["Year"], ratios[2024]['Performance Ratios']['NPM Growth'], ratios[2023]['Performance Ratios']['NPM Growth'], {145: -3, 146: -1.5, 147: 0.75, 148: 2.25, 149:3})
        Cash_Flow = self.calculate_cash_flow(reporting_year, client_info[2024]["Year"], ratios[2024]['Performance Ratios']['Cash flow from operating activities'], ratios[2023]['Performance Ratios']['Cash flow from operating activities'], {152: -2, 153: 2})
        Current_Ratio = self.calculate_current_ratio(reporting_year, client_info[2024]["Year"], ratios[2024]['Liquidity Ratios']['Current Ratio'], ratios[2023]['Liquidity Ratios']['Current Ratio'], {156: -6, 157: 1.5, 158: 3})
        Leveraged_Ratio = self.calculate_leveraged_ratio(reporting_year, client_info[2024]["Year"], ratios[2024]['Leverage Financial Ratios']['Leverage Ratio'], ratios[2023]['Leverage Financial Ratios']['Leverage Ratio'], {161: -8, 162: -4, 163: 2, 164:4})
        Interest_Coverage_Ratio = self.calculate_ICR0(reporting_year, client_info[2024]["Year"], ratios[2024]['Leverage Financial Ratios']['Interest Coverage'], ratios[2023]['Leverage Financial Ratios']['Interest Coverage'], {167: -2, 168: 1.5, 169: 2})
        DSCR = self.calculate_DSCR2(reporting_year, client_info[2024]["Year"], ratios[2024]['Leverage Financial Ratios']['DSCR'], ratios[2023]['Leverage Financial Ratios']['DSCR'], {172: -2, 173: 1, 174: 2})
        Receivable_Quality = 4 # Need to be added in dropbox
        Receivable_Days = self.calculate_receivable_days(reporting_year, client_info[2024]["Year"], ratios[2024]['Activity Ratios']['Receivables Days'], ratios[2023]['Activity Ratios']['Receivables Days'], {185: -2, 186: -1, 187: 0, 188:2})
        Debt_Sales_Ratio = self.calculate_debt_sales_ratio(reporting_year, client_info[2024]["Year"], ratios[2024]['Leverage Financial Ratios']['External Debt / Sales ratio'], ratios[2023]['Leverage Financial Ratios']['External Debt / Sales ratio'], {191: -1, 192: 0, 193: 2})
        Availibility_Audited_Financials = self.calculate_auditable_finances(reporting_year, client_info[2024]["Year"], client_info[2024]["Type of FS"], client_info[2023]["Type of FS"], {196: 0.25, 197: 0.25, 198: 0.40, 199:0.50})
        Quality_Internal_Report = self.calculate_quality_internal_report(reporting_year, client_info[2024]["Year"], client_info[2024]["Quality of Internal Reports"], client_info[2023]["Quality of Internal Reports"], {202:0.25, 203:0.35, 204:0.43})

        financial_scores = {
            "revenue_growth"  : revenue_growth,
            "GPM_Change" : GPM_Change,
            "NPM" : NPM,
            "NPM_Change" : NPM_Change,
            'Cash_Flow' : Cash_Flow,
            "Current_Ratio" : Current_Ratio,
            "Leveraged_Ratio" : Leveraged_Ratio,
            "Interest_Coverage_Ratio" : Interest_Coverage_Ratio,
            "DSCR" : DSCR,
            "Recievable_Quality" : Receivable_Quality,
            "Recievable_Days" : Receivable_Days,
            "Debt_Sales_Ratio" : Debt_Sales_Ratio,
            "Availibility_Audited_Financials" : Availibility_Audited_Financials,
            "Quality_Internal_Report" : Quality_Internal_Report
        }

        with open('financial_scores.json', 'w') as file:
            json.dump(financial_scores, file, indent=4)

        # return 0.1

        return revenue_growth + GPM_Change + NPM + NPM_Change + Cash_Flow + Current_Ratio + Leveraged_Ratio + Interest_Coverage_Ratio + DSCR + Receivable_Quality + Receivable_Days + Debt_Sales_Ratio + Availibility_Audited_Financials + Quality_Internal_Report