import pandas as pd
import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta


df = pd.read_csv('sped_files/active_child_count.csv', delimiter=',')
df.rename(columns=df.iloc[0])
df[' age'] = '0'
print(list(df))
dfnew = df[["student_id", " grade", " disability1", " birthdate"]]



now = dt.datetime.now()
dfnew[" birthdate"] = pd.to_datetime(dfnew[' birthdate'])
print(dfnew[" birthdate"])
for i in range(0, len(df)):
    diff = now - dfnew[" birthdate"]
    years = diff.days // 365
    days = diff.days - (years*365)
    df['age'][i] = str(years) + ' years ' + str(days) + ' days'

print(df)


dfnew[" birthdate"] = pd.to_datetime(dfnew[' birthdate'])

print(df)
print(dfnew.sort_values(by=' birthdate'))




