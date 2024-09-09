import pandas as pd
from datetime import datetime, timedelta

df=pd.read_csv('../data/esp_for_plot.csv')
df["new_cases_rolling_average"] = df['new_cases'].rolling(window=7).mean()
df["new_deaths_rolling_average"] = df['new_deaths'].rolling(window=7).mean()
df2=df[["date","new_cases_rolling_average","new_deaths_rolling_average"]]

#minus 6 days so rolling average data will match reality (in Spain data from previous week was reported in one day)
def minus_6_days(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date_obj = date_obj - timedelta(days=6)
    return new_date_obj.strftime('%Y-%m-%d')
df2["date"]=df2["date"].apply(minus_6_days)
df2=df2.dropna(subset=["new_cases_rolling_average"])

df2.to_csv("../data/new_cases_and_deaths.csv",index=False)


#prepare data pol

df=pd.read_csv('../data/pol_for_plot.csv')
df["new_cases_rolling_average"] = df['new_cases'].rolling(window=7).mean()
df["new_deaths_rolling_average"] = df['new_deaths'].rolling(window=7).mean()
df2=df[["date","new_cases_rolling_average","new_deaths_rolling_average"]]

#minus 6 days so rolling average data will match reality (in Spain data from previous week was reported in one day)
def minus_6_days(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date_obj = date_obj - timedelta(days=6)
    return new_date_obj.strftime('%Y-%m-%d')
df2["date"]=df2["date"].apply(minus_6_days)
df2=df2.dropna(subset=["new_cases_rolling_average"])

df2.to_csv("../data/new_cases_and_deaths_pol.csv",index=False)