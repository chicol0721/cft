import pandas as pd

xls_data = pd.ExcelFile('slr06.xls')
print(xls_data.sheet_names)
