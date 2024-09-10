import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

POL_POP= 36820000
ESP_POP= 47780000
xlabels= ['01-2020', '04-2020', '07-2020', '10-2020', '01-2021', '04-2021', '07-2021', '10-2021', '01-2022', '04-2022', '07-2022', '10-2022', '01-2023', '04-2023', '07-2023', '10-2023', '01-2024','04-2024']

#loading data 1/2
data_esp=pd.read_csv("../data/esp_for_plot.csv")
data_pol=pd.read_csv("../data/pol_for_plot.csv")
x_esp=data_esp["date"].to_numpy()
x_pol=data_pol["date"].to_numpy()
data_esp["total_cases"]=data_esp["total_cases"]/ESP_POP
total_cases_esp=data_esp["total_cases"].to_numpy()
data_pol["total_cases"]=data_pol["total_cases"]/POL_POP
total_cases_pol=data_pol["total_cases"].to_numpy()
data_esp["total_deaths"]=data_esp["total_deaths"]/ESP_POP
total_deaths_esp=data_esp["total_deaths"].to_numpy()
data_pol["total_deaths"]=data_pol["total_deaths"]/POL_POP
total_deaths_pol=data_pol["total_deaths"].to_numpy()

#ploting 2/4
fig, axs = plt.subplots(2,2, figsize=(20,16))

#TOTAL CASES
axs[0,0].plot(x_esp, total_cases_esp, c='#ffd301', label="Spain")
axs[0,0].set_xlabel("Date")
axs[0,0].set_ylabel("Total cases / Population")
axs[0,0].grid(True,which="major", linestyle="--", linewidth=0.5, color='grey', alpha=0.3)

#formatting y axis to perecent format
def to_percent(x, pos):
    return f'{x*100:.1f}%'
axs[0, 0].yaxis.set_major_formatter(FuncFormatter(to_percent))

#xlabels
axs[0,0].set_xticks(np.arange(0,len(x_esp),91)) #365/4=91.25
axs[0,0].set_xticklabels(xlabels)
axs[0,0].tick_params(axis='x', labelsize=6)

#ploting Poland
axs[0,0].plot(x_pol,total_cases_pol, c='#d72353', label="Poland")
axs[0,0].legend(loc='lower right', fontsize='16')

#title
axs[0,0].set_title("Total Cases / Population [%]")

#TOTAL DEATHS
axs[0,1].plot(x_esp, total_deaths_esp, c='#ffd301', label="Spain")
axs[0,1].set_xlabel("Date")
axs[0,1].set_ylabel("Total deaths / Population")
# axs[0,1].set_ylim(0,140000)
axs[0,1].grid(True,which="major", linestyle="--", linewidth=0.5, color='grey', alpha=0.3)

#formatting y axis to promille format
def to_promille(x, pos):
    return f'{x * 1000:.1f}‰'
axs[0,1].yaxis.set_major_formatter(FuncFormatter(to_promille))

#xlabels
axs[0,1].set_xticks(np.arange(0,len(x_esp),91)) #365/4=91.25
axs[0,1].set_xticklabels(xlabels)
axs[0,1].tick_params(axis='x', labelsize=6)

# #ploting Poland
axs[0,1].plot(x_pol,total_deaths_pol, c='#d72353', label="Poland")
axs[0,1].legend(loc='lower right', fontsize='16')

#title
axs[0,1].set_title("Total Deaths / Population [‰]")




#loading data 2/2
data_esp=pd.read_csv("../data/new_cases_and_deaths.csv")
data_pol=pd.read_csv("../data/new_cases_and_deaths_pol.csv")
x_esp=data_esp["date"].to_numpy()
x_pol=data_pol["date"].to_numpy()
data_esp["new_cases_rolling_average"]=data_esp["new_cases_rolling_average"]/ESP_POP*10000
new_cases_esp=data_esp["new_cases_rolling_average"].to_numpy()
data_pol["new_cases_rolling_average"]=data_pol["new_cases_rolling_average"]/POL_POP*10000
new_cases_pol=data_pol["new_cases_rolling_average"].to_numpy()
data_esp["new_deaths_rolling_average"]=data_esp["new_deaths_rolling_average"]/ESP_POP*1000000
new_deaths_esp=data_esp["new_deaths_rolling_average"].to_numpy()
data_pol["new_deaths_rolling_average"]=data_pol["new_deaths_rolling_average"]/ESP_POP*1000000
new_deaths_pol=data_pol["new_deaths_rolling_average"].to_numpy()


#plotting 4/4
#NEW CASES
axs[1,0].set_title("New Cases per 10000 people")
axs[1,0].plot(x_esp, new_cases_esp, c='#ffd301', alpha=0.2)
axs[1,0].set_xlabel("Date")
axs[1,0].set_ylabel("New Cases per 10000 people")
axs[1,0].grid(True,which="major", linestyle="--", linewidth=0.5, color='grey', alpha=0.3)

#fill the area under the curve
axs[1,0].fill_between(x_esp, new_cases_esp, color='#ffd301', alpha=0.5, label="Spain")

#xlabels
xlabels= ['01-2020', '04-2020', '07-2020', '10-2020', '01-2021', '04-2021', '07-2021', '10-2021', '01-2022', '04-2022', '07-2022', '10-2022', '01-2023', '04-2023']
axs[1,0].set_xticks(np.arange(0,len(x_esp),91)) #365/4=91.25
axs[1,0].set_xticklabels(xlabels)
axs[1,0].tick_params(axis='x', labelsize=6)

#ploting poland
axs[1,0].plot(x_esp,new_cases_pol[0:len(x_esp)], '#d72353', alpha=0.2)
axs[1,0].fill_between(x_esp,new_cases_pol[0:len(x_esp)], color='#d72353', alpha=0.5, label="Poland")
axs[1,0].legend(loc='upper right', fontsize='16')

#NEW DEATHS
axs[1,1].set_title("New Deaths per million people")
axs[1,1].plot(x_esp, new_deaths_esp, c='#ffd301', alpha=0.2)
axs[1,1].set_xlabel("Date")
axs[1,1].set_ylabel("New Deaths per million people")
axs[1,1].grid(True,which="major", linestyle="--", linewidth=0.5, color='grey', alpha=0.3)

#fill the area under the curve
axs[1,1].fill_between(x_esp, new_deaths_esp, color='#ffd301', alpha=0.5, label="Spain")

#xlabels
xlabels= ['01-2020', '04-2020', '07-2020', '10-2020', '01-2021', '04-2021', '07-2021', '10-2021', '01-2022', '04-2022', '07-2022', '10-2022', '01-2023', '04-2023']
axs[1,1].set_xticks(np.arange(0,len(x_esp),91)) #365/4=91.25
axs[1,1].set_xticklabels(xlabels)
axs[1,1].tick_params(axis='x', labelsize=6)

#ploting poland
axs[1,1].plot(x_esp,new_deaths_pol[0:len(x_esp)], '#d72353', alpha=0.2)
axs[1,1].fill_between(x_esp,new_deaths_pol[0:len(x_esp)], color='#d72353', alpha=0.5, label="Poland")
axs[1,1].legend(loc='upper right', fontsize='16')

#title and layout
fig.suptitle("Comparison between Spain and Poland", fontsize=32)
plt.tight_layout()

plt.savefig("../plots/comparison_pop.png")

