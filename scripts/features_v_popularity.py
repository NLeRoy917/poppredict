import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('..')

from sql.SQLite import SqlClient
from utils.Utils import Utils

utils = Utils()
sql = SqlClient(db_file='data.db')

danceability_pop = sql.danceability_pop_data()
energy_pop = sql.energy_pop_data()
loudness_pop = sql.loudness_pop_data()

dance_x = []
dance_y = []
for data_point in danceability_pop:
    dance_x.append(data_point['Danceability'])
    dance_y.append(data_point['Popularity'])

energy_x = []
energy_y = []
for data_point in energy_pop:
    energy_x.append(data_point['Energy'])
    energy_y.append(data_point['Popularity'])

loudness_x = []
loudness_y = []
for data_point in loudness_pop:
    loudness_x.append(data_point['Loudness'])
    loudness_y.append(data_point['Popularity'])

fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()

ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)
ax3 = fig3.add_subplot(111)

ax1.scatter(loudness_x, loudness_y, c='g', label='Loudness', s=1)
ax1.set_title('Loudness v Popularity')
ax1.set_xlabel('Loudness')
ax1.set_ylabel('Popularity')

ax2.scatter(dance_x, dance_y, c='r', label='Danceability', s=1)
ax2.set_title('Danceability v Popularity')
ax2.set_xlabel('Danceability')
ax2.set_ylabel('Popularity')

ax3.scatter(energy_x, energy_y, c='b', label='Energy', s=1)
ax3.set_title('Energy v Popularity')
ax3.set_xlabel('Energy')
ax3.set_ylabel('Popularity')

plt.show()
