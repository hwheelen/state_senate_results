import pandas as pd
import geopandas as gpd
import numpy as np

#input start path
start_path = ''
#load in raw election data 
raw_elec = pd.read_csv(start_path + 'GitHub/MEDSL/2018-elections-official/precinct_2018.csv',encoding = "ISO-8859-1")

#select states and print offices for this state in 2016
states = ['Florida','North Carolina']
for st in states:
    st_df = raw_elec.loc[raw_elec.state == st]
    offices = st_df.office.unique()
    print(offices)
    
#input name of state senate election to aggregate
    sen = 'State Senate'
    st_sen = st_df.loc[st_df.office == sen]
    st_sen_tots = pd.pivot_table(st_sen, index = ['district'], columns = ['party'], values = ['votes'], aggfunc = np.sum)
    st_sen_tots.columns = st_sen_tots.columns.to_series().str.join(' ')
    st_sen_tots['state'] = st
    st_sen_tots['year'] = '2018'
    st_sen_tots.to_csv(start_path + 'GitHub/projects/state_senate_results/2018_results/' + st.replace(' ','_') + '_st_sen_tots.csv')
