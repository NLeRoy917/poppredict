import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('..')

from sql.SQLite import SqlClient
from utils.Utils import Utils

utils = Utils()
sql = SqlClient(db_file='data.db')

key_pop_data = sql.key_pop_data()
dist_data = {
    'C':[],
    'C#':[],
    'D':[],
    'D#':[],
    'E':[],
    'F':[],
    'F#':[],
    'G':[],
    'G#':[],
    'A':[],
    'A#':[],
    'B':[]
}
colors = ['lightcoral', 'coral', 'bisque', 'gold', 'yellowgreen', 'palegreen', 'aquamarine', 'teal', 'skyblue', 'mediumpurple', 'violet', 'pink']
for datapoint in key_pop_data:
    pop = datapoint['Popularity']
    key = datapoint['Key']
    if pop > 50:
        dist_data[utils.int_to_key(key)].append(pop)
    else:
        continue

fig, axs = plt.subplots(12,1)
fig.suptitle('Key and Popularity Distribution')
for key,i,color in zip(dist_data,range(len(dist_data)),colors):
    axs[i].hist(dist_data[key], bins=30, facecolor=color)
    axs[i].set_title(key)

plt.show()
