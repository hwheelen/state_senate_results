import pandas as pd
import geopandas as gpd
import numpy as np

#input start path
start_path = ''
#load in raw election data 
raw_elec = gpd.read_file(start_path + 'GitHub/MEDSL/stateoffices2016.csv')

#select states and print offices for this state in 2016
states = ['Florida']
for st in states:
    st_df = raw_elec.loc[raw_elec.state == st]
    offices = st_df.office.unique()
    print(offices)
    
#input name of state senate election to aggregate
    sen = 'State Senator'
    st_sen = st_df.loc[st_df.office == sen]
    st_sen['votes'] = st_sen['candidatevotes'].astype(int)
    st_sen_tots = pd.pivot_table(st_sen, index = ['district'], columns = ['party'], values = ['votes'], aggfunc = np.sum)
    st_sen_tots.columns = st_sen_tots.columns.to_series().str.join(' ')
    st_sen_tots['state'] = st
    st_sen_tots['year'] = '2016'
    st_sen_tots.to_csv(start_path + 'GitHub/projects/state_senate_results/2016_results/' + st + '_st_sen_tots.csv')
