import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import argparse
from datetime import datetime

#use argparse to get first and last date for the plot
parser = argparse.ArgumentParser(description="create a plot of mortality from a given date to other given date")
parser.add_argument('f', metavar='from', type=str, help= 'from this date')
parser.add_argument('t', metavar='to', type=str, help= 'to this date')
args = parser.parse_args()
f= args.f
t= args.t

#read data about mortality
df=pd.read_csv("../data/mortality.csv")
df['date'] = pd.to_datetime(df['date'])
f = datetime.strptime(f, "%Y-%m")
t = datetime.strptime(t, "%Y-%m")

#filter data to get only dates in our range
df_filtered=df[df["date"]>=f]
df_filtered=df_filtered[df["date"]<=t]
x=df_filtered["date"].to_numpy()
y=df_filtered["mortality"].to_numpy()


#make a plot
fig, ax = plt.subplots(figsize=(10,6))

ax.bar(x,y, 4.0, color="black")
ax.set_xlabel("Date")
ax.set_ylabel("Mortality")
ax.set_ylim(0,0.05)
ax.set_yticks(np.arange(0, 0.05, 0.005))
ax.grid(which='both', axis='y', linestyle='--', linewidth=0.5)


#formatting y axis to perecent format
def to_percent(x, pos):
    return f'{x*100:.1f}%'
ax.yaxis.set_major_formatter(FuncFormatter(to_percent))
ax.tick_params(axis='x', labelsize=6)
plt.xticks(rotation=45)


plt.title("Estimated Mortality Rate (Deaths/Cases)")
# plt.tight_layout()
plt.savefig("../plots/mortality_argparse.png")