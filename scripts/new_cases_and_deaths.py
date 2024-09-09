import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


#loading data
data=pd.read_csv("../data/new_cases_and_deaths.csv")
x=data["date"].to_numpy()
y=data["new_cases_rolling_average"].to_numpy()
y1=data["new_deaths_rolling_average"].to_numpy()

#ploting new cases
fig, ax = plt.subplots()
ax.plot(x, y, "red", alpha=0.2)
ax.set_xlabel("Date")
ax.set_ylabel("New cases", color="red")
ax.grid(True,which="major", linestyle="--", linewidth=0.5, color="#ffd5d8", alpha=0.7)

#fill the area under the curve
plt.fill_between(x, y, color='red', alpha=0.5)

#formatting y axis in ax to thousands format
def thousands(x, pos):
    return f'{x * 1e-3:.1f}K'
ax.yaxis.set_major_formatter(FuncFormatter(thousands))

#xlabels
xlabels= ['01-2020', '04-2020', '07-2020', '10-2020', '01-2021', '04-2021', '07-2021', '10-2021', '01-2022', '04-2022', '07-2022', '10-2022', '01-2023', '04-2023']

ax.set_xticks(np.arange(0,len(x),91)) #365/4=91.25
ax.set_xticklabels(xlabels)
ax.tick_params(axis='x', labelsize=6)
plt.xticks(rotation=45)


#ploting new deaths
ax1= ax.twinx()
ax1.plot(x,y1, "black", alpha=0.2)
ax1.set_ylabel("New deaths", color="black")
ax1.grid(True,which="major", linestyle="--", linewidth=0.5, color="grey", alpha=0.5)

#fill the area under the curve
plt.fill_between(x, y1, color='black', alpha=0.5)


#title and layout
plt.suptitle("New daily cases and deaths", fontsize=18)
plt.title("* 7-day rolling average *",fontsize=6)

plt.tight_layout()

plt.savefig("../plots/new_cases_and_deaths.png")

