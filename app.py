import pandas as pd
df=pd.read_csv("sales_data_sample.csv",encoding="latin1")
print(df)
pd.set_option('display.max_columns', None)