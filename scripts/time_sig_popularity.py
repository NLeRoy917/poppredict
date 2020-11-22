import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('..')

from sql.SQLite import SqlClient
from utils.Utils import Utils

utils = Utils()
sql = SqlClient(db_file='data.db')

time_sig_pop_data = sql.time_sig_pop_data()
dist_data = {
    '3/4':[],
    '4/4':[],
    '5/4':[],
    '6/4':[],
    '7/4':[],
    'Complex': [],
    'None': []
}
colors = ['lightcoral', 'coral', 'bisque', 'gold', 'yellowgreen']
for datapoint in time_sig_pop_data:
    pop = datapoint['Popularity']
    time_sig = datapoint['Time_Signature']
    if pop > 50:
        dist_data[utils.int_to_time_signature(time_sig)].append(pop)
    else:
        continue

fig, axs = plt.subplots(7,1)
fig.suptitle('Time Signature and Popularity Distribution')
for time_sig,i,color in zip(dist_data,range(len(dist_data)),colors):
    axs[i].hist(dist_data[time_sig], bins=30, facecolor=color)
    axs[i].set_title(time_sig)

plt.show()
