import plotly
import plotly.express as px
import requests
import pandas as pd
import json

# get Spain municipal boundaries
res = requests.get(
    "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/spain-provinces.geojson"
)
regions = res.json()

df = pd.read_csv('../data/regions.csv')

fig = px.choropleth_mapbox(df, geojson=regions,
                           locations='postal',
                           color='cases_per_pop',
                           featureidkey = 'properties.cod_prov',
                           color_continuous_scale="Cividis",
                           range_color=(300, 1400),
                           mapbox_style="carto-positron",
                           zoom=6,
                           center = {"lat": 40, "lon": -5},
                           opacity=0.7,
                           labels={'cases_per_pop':'Cases per 10000 people', 'postal':'Postal Code'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

plotly.offline.plot(fig, filename='../plots/map.html')