import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


#loading data
data=pd.read_csv("../data/esp_for_plot.csv")
x=data["date"].to_numpy()
y=data["total_cases"].to_numpy()
y1=data["total_deaths"].to_numpy()

#ploting total cases
fig, ax = plt.subplots()
ax.plot(x, y, "red")
ax.set_xlabel("Date")
ax.set_ylabel("Total cases", color="red")
# ax.set_ylim(0,15000000)
ax.grid(True,which="major", linestyle="--", linewidth=0.5, color="#ffd5d8", alpha=0.7)

#formatting y axis to "number M" format
def millions(x, pos):
    return f'{x * 1e-6:.1f}M'
ax.yaxis.set_major_formatter(FuncFormatter(millions))

#xlabels
xlabels= ['01-2020', '04-2020', '07-2020', '10-2020', '01-2021', '04-2021', '07-2021', '10-2021', '01-2022', '04-2022', '07-2022', '10-2022', '01-2023', '04-2023', '07-2023', '10-2023', '01-2024','04-2024']

ax.set_xticks(np.arange(0,len(x),91)) #365/4=91.25
ax.set_xticklabels(xlabels)
ax.tick_params(axis='x', labelsize=6)
plt.xticks(rotation=45)


#ploting total deaths
ax1= ax.twinx()
ax1.plot(x,y1, "black")
ax1.set_ylabel("Total deaths", color="black")
ax1.set_ylim(0,180000)
ax1.grid(True,which="major", linestyle="--", linewidth=0.5, color="grey", alpha=0.3)

#formatting y axis in ax1 to thousands format
def thousands(x, pos):
    return f'{x * 1e-3:.1f}K'
ax1.yaxis.set_major_formatter(FuncFormatter(thousands))

#title and layout
plt.title("Total cases and deaths")
plt.tight_layout()

plt.savefig("../plots/total_cases_and_deaths.png")

