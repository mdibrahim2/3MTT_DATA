##importing pandas LIbrary
import pandas as pd
import numpy as np

## reading the excell file from external source
df = pd.read_excel(r"C:\Users\MDI\Desktop\DATA ANALYSIS\REPORT.xlsx")
##outputing tthe excell dataset
print(df)
# removing unwanted character
df["NAMES"] = df["NAMES"].str.strip("_%%/")

# removing the remark column
df = df.drop(columns = "REMARK")
##outputing tthe clean dataset
print(df)
