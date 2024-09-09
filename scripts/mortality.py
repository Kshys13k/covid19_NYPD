import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df=pd.read_csv("../data/mortality.csv")
x=df["date"].to_numpy()
y=df["mortality"].to_numpy()

fig, ax = plt.subplots(figsize=(10,5))

ax.bar(x,y, 0.5, color="black")
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
plt.tight_layout()
plt.savefig("../plots/mortality.png")