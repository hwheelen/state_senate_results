import pandas as pd
import geopandas as gpd
import numpy as np

#input start path
start_path = ''
#load in raw election data
st_df = gpd.read_file(start_path + 'GitHub/OpenElections/openelections-results-fl/raw/20161108__fl__general__precinct__raw.csv')

#select states and print offices for this state in this year
offices = st_df.office.unique()
print(offices)

#input name of state senate election to aggregate
sen = 'State Senator'
st = 'Florida'
st_sen = st_df.loc[st_df.office == sen]
st_sen['votes'] = st_sen['votes'].astype(int)
st_sen_tots = pd.pivot_table(st_sen, index = ['district'], columns = ['party'], values = ['votes'], aggfunc = np.sum)
st_sen_tots.columns = st_sen_tots.columns.to_series().str.join(' ')
st_sen_tots['state'] = st
st_sen_tots['year'] = '2016'
st_sen_tots.to_csv(start_path + 'GitHub/projects/state_senate_results/2016_results/' + st.replace(' ','_') + '_st_sen_tots_OE.csv')
