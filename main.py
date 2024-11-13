from utilities import extract_table_to_dataframe
from config import DATABASE_NAME, USER_NAME, USER_PASSWORD, HOST_IP, PORT
from utilities import ExcelReportUpdater


#if __name__ == "__main__":

# sql_query = "select * from sama_pr"

# data = extract_table_to_dataframe(DATABASE_NAME,
#                                 USER_NAME,
#                                 USER_PASSWORD,
#                                 HOST_IP,
#                                 PORT, 
#                                 sql_query)

# Converting all numeric values upto 2 Decimal places
# data = data.round(2)

# Format all float and integer columns to use a comma as a thousand separator
# and a dot for decimals (common in English locale).

def format_international(value):
    if isinstance(value, (int, float)):
        return f"{value:,.2f}"
    return value

# Apply the formatting to all cells in the DataFrame
    #data = data.map(format_international)

# Example usage


    #filepath = "C:\\Users\\pankaj.avasthi\\Desktop\\Lendo\\Projects\\BI Analytics\\Risk Analytics\\Sama Report Automation"
    #filename = "SAMA Prudential Forms- Q2 2024- Locked version.xlsx"

    # Create an instance of the ExcelReportUpdater class
    #updater = ExcelReportUpdater(filepath, filename)
    # Open Excel Worksheet
    #updater.open_excel()

    # Code to move dta from existing cells/range to other designated cells/range
    #sheetname = 'Form 1.2'

    source_cell = "C33:D35"  # Cell/Range to copy from
    target_cell = "E33:F35"  # Cell/Range to paste into
    updater.replace_cell_value(sheetname,source_cell, target_cell)

    source_cell = "C39:D42"  # Cell/Range to copy from
    target_cell = "E39:F42"  # Cell/Range to paste into
    updater.replace_cell_value(sheetname,source_cell, target_cell)

    source_cell = "C46:D49"  # Cell/Range to copy from
    target_cell = "E46:F49"  # Cell/Range to paste into
    updater.replace_cell_value(sheetname,source_cell, target_cell)

    source_cell = "C53:D55"  # Cell/Range to copy from
    target_cell = "E53:F55"  # Cell/Range to paste into
    updater.replace_cell_value(sheetname,source_cell, target_cell)

    source_cell = "C59:D61"  # Cell/Range to copy from
    target_cell = "E59:F61"  # Cell/Range to paste into
    updater.replace_cell_value(sheetname,source_cell, target_cell)

    source_cell = "C65:D67"  # Cell/Range to copy from
    target_cell = "E65:F67"  # Cell/Range to paste into
    updater.replace_cell_value(sheetname,source_cell, target_cell)

    
    # Code to move dta from existing cells/range to other designated cells/range
    cell = "G33"
    df = data
    row_value = 1
    column_value = 5

    #updater.update_cell(sheetname, cell, data, row_value, column_value)
    
    
    # Closing existing file after making changes
    updater.save_and_close()