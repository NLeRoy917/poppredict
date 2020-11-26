from poppredict import PopPredict
from sql import SQLite

if __name__ == '__main__':
    sql = SQLite.SqlClient()
    pp = PopPredict.PopPredict()
    data = sql.get_training_validation_data()
    # print(data[:20])
    pp.summary()
