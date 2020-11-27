import tensorflow as tf

from poppredict import PopPredict
from sql import SQLite

sql = SQLite.SqlClient(db_file='data.db')
pp = PopPredict.PopPredict(path='./model/')

random = sql.get_random_datapoint()
inputs = random[:-1]
popularity = random[-1]

print(inputs.shape)
pp.summary()
pop_predict = pp.predict(tf.expand_dims(inputs, axis=0))
print('Real:',popularity, '|', 'Prediction:', pop_predict[0][0])




