import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")

data = [pd.read_excel(filepath, sheet_name="Sheet 1") for filepath in filepaths]
[print(item) for item in data]
