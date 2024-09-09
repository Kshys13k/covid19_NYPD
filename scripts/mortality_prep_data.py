import pandas as pd
import numpy as np
from datetime import datetime, timedelta

df=pd.read_csv('../data/esp_for_plot.csv') 

#calculate rolling averages
df["new_cases_rolling_average"] = df['new_cases'].rolling(window=7).mean()
df["new_deaths_rolling_average"] = df['new_deaths'].rolling(window=7).mean()
df=df.dropna(subset=["total_deaths","new_cases"])
df=df[["date","new_cases_rolling_average","new_deaths_rolling_average"]]

#minus 6 days so rolling average data will match reality (in Spain data from previous week was reported in one day)
def minus_6_days(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date_obj = date_obj - timedelta(days=6)
    return new_date_obj.strftime('%Y-%m-%d')

df['date']=df['date'].apply(minus_6_days)

#create df1 with cases and move the date so it will math with deaths (deaths come after new cases in 2 weeks on average)
df1=df[["date","new_cases_rolling_average"]]

def add_two_weeks(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date_obj = date_obj + timedelta(weeks=2)
    return new_date_obj.strftime('%Y-%m-%d')

df1['date'] = df1['date'].apply(add_two_weeks)
df1=df1.reset_index()
df1=df1.drop(columns=["index"])


#create df2 with deaths
df2=df[["date","new_deaths_rolling_average"]]
df2=df2[(df2["date"]>="2020-02-24")]
df2=df2.reset_index()
df2=df2.drop(columns=["index","date"])
df12=pd.concat([df1,df2],axis=1)
df12=df12.dropna(subset=["new_deaths_rolling_average"])
df12

#Resample df so in row we have sum of data from whole month
df12['date'] = pd.to_datetime(df12['date'])
df12.set_index('date', inplace=True)
monthly_sum_df = df12.resample('M').sum()
monthly_sum_df.reset_index(inplace=True)
monthly_sum_df['date'] = monthly_sum_df['date'].dt.strftime('%Y-%m')
monthly_sum_df

#calculate mortality
monthly_sum_df["mortality"]=monthly_sum_df["new_deaths_rolling_average"]/monthly_sum_df["new_cases_rolling_average"]
monthly_sum_df.to_csv("../data/mortality.csv", index=False)