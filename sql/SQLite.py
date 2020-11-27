import sqlite3
import random
import numpy as np


class SqlClient:
    """
    Python class to interface the sqlite database
    """

    def __init__(self, db_file='data.db'):
        """
        Create an instance of the SqlClient class.

        :param db_dile: Path to the database file to store data in
        """
        self._db_file = db_file
        self._conn = sqlite3.connect(self._db_file)
        self._cur = self._conn.cursor()

    def _query(self, query, data=None):
        """
        Execute a query against the database

        :param data: a tuple that stores values for parametrized query
        """
        if data:
            self._cur.execute(query, data)
            results = self._cur.fetchall()
        else:
            results = self._cur.execute(query)
            results = self._cur.fetchall()

        if len(results) == 1:
            return results[0]
        else:
            return results

    def _execute(self, exec, data=None):
        """
        Execute a command against the database

        :param data: a tuple that stores values for parametrized exec
        """

        if data:
            self._cur.execute(exec, data)
        else:
            self._cur.execute(exec)
        self._conn.commit()
    
    def check_track_exists(self, id):
        """
        Check to see if a track already exists in the database

        :param id: the track id
        """
        q = '''
            SELECT 1
            FROM TrackData
            WHERE ID = ?
            '''
        result = self._query(q,data=(id,))
        if len(result) == 0:
            return False
        else:
            return True

    def insert_track(self, name=None, artist=None,
                     uri=None, id=None, href=None, popularity=None):
        """
        Insert a track into the database

        :param name: name of the track
        :param artist: artist for the track
        :param uri: spotify uri for the track
        :param id: spotify id for the track
        :param href: href for the track
        :Param popularity: popularity value for the track
        """
        q = '''
            INSERT INTO TrackData (Name, Artist, URI, ID, href, Popularity)
            VALUES(?, ?, ?, ?, ?, ?);
            '''
        self._execute(q, data=(name, artist, uri, id, href, popularity))

    def insert_analysis(self, uri=None, id=None, acousticness=None,
                        danceability=None, duration_ms=None, energy=None,
                        instrumentalness=None, key=None, liveness=None,
                        loudness=None, mode=None, speechiness=None,
                        tempo=None, time_signature=None, valence=None):
        """
        Insert an analysis datapoint into the database
        :param uri: The URI of a track
        :param id: The tracks id
        :param acousticness: The acousticness of a track (0 -> 1.0)
        :param danceability: The danceability of a track (0 -> 1.0)
        :param duration_ms: Duration of a track in milliseconds
        :param energy: The energy of a track (0 -> 1.0)
        :param instrumentalness: The instrumentalness of a track (0 -> 1.0)
        :param key: The track's key (pitch key notation)
        :param liveness: The tracks liveness (0 -> 1.0)
        :param loudness: The tracks loudness (0 -> 1.0)
        :param mode: The tracks mode (major/minor [1/0])
        :param speechiness: The track's speechiness (0 -> 1.0)
        :param tempo: A tracks tempo in bpm
        :param time_signature: time signature of a track (3->7, x/4)
        :param valence: A track's valence (0 -> 1.0)
        """
        q = '''
            INSERT INTO AnalysisData (URI, ID, Acousticness, Danceability,
                                      Duration_ms, Energy, Instrumentalness,
                                      Key, Liveness, Loudness, Mode, Speechiness,
                                      Tempo, Time_Signature, Valence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
        self._execute(
            q,
            data=(
                uri,
                id,
                acousticness,
                danceability,
                duration_ms,
                energy,
                instrumentalness,
                key,
                liveness,
                loudness,
                mode,
                speechiness,
                tempo,
                time_signature,
                valence))

    def get_all_tracks(self):
        """
        Pull all the track objects from the database
        """
        q = '''
            SELECT Name, Artist, URI, ID, href, Popularity
            FROM TrackData
            '''
        results = self._query(q)
        tracks = []
        for row in results:
            tracks.append({
                'Name': row[0],
                'Artist': row[1],
                'URI': row[2],
                'ID': row[3],
                'href': row[4],
                'Popularity': row[5]
            })
        return tracks

    def popularity_data(self):
        """
        Get all the populrity data-points in an array from the database
        """

        q = '''
            SELECT Popularity FROM TrackData
            '''
        results = self._query(q)
        data = []
        for row in results:
            data.append(row[0])
        return data
    
    def key_pop_data(self):
        """
        Get a dictionary of song keys that associate with a list of popularity values
        """
        q = '''
            SELECT TrackData.Popularity, AnalysisData.Key 
            FROM TrackData
            INNER JOIN AnalysisData
            ON TrackData.ID = AnalysisData.ID
            '''
        results = self._query(q)
        data = []
        for row in results:
            data.append({
                'Popularity': row[0],
                'Key': row[1]
            })
        return data
    
    def time_sig_pop_data(self):
        """
        Get a dictionary of song time_signatures that associate with a list of popularity values
        """
        q = '''
            SELECT TrackData.Popularity, AnalysisData.Time_Signature
            FROM TrackData
            INNER JOIN AnalysisData
            ON TrackData.ID = AnalysisData.ID
            '''
        results = self._query(q)
        data = []
        for row in results:
            data.append({
                'Popularity': row[0],
                'Time_Signature': row[1]
            })
        return data
    
    def danceability_pop_data(self):
        """
        Get a list of danceability-popularity datapoints
        """
        q = '''
            SELECT TrackData.Popularity, AnalysisData.Danceability
            FROM TrackData
            INNER JOIN AnalysisData
            ON TrackData.ID = AnalysisData.ID
            '''
        results = self._query(q)
        data = []
        for row in results:
            data.append({
                'Popularity': row[0],
                'Danceability': row[1]
            })
        return data

    def energy_pop_data(self):
        """
        Get a list of energy-popularity datapoints
        """
        q = '''
            SELECT TrackData.Popularity, AnalysisData.Energy
            FROM TrackData
            INNER JOIN AnalysisData
            ON TrackData.ID = AnalysisData.ID
            '''
        results = self._query(q)
        data = []
        for row in results:
            data.append({
                'Popularity': row[0],
                'Energy': row[1]
            })
        return data

    def loudness_pop_data(self):
        """
        Get a list of loudness-popularity datapoints
        """
        q = '''
            SELECT TrackData.Popularity, AnalysisData.Loudness
            FROM TrackData
            INNER JOIN AnalysisData
            ON TrackData.ID = AnalysisData.ID
            '''
        results = self._query(q)
        data = []
        for row in results:
            data.append({
                'Popularity': row[0],
                'Loudness': row[1]
            })
        return data
    
    def tempo_pop_data(self):
        """
        Get's a list of datapoints on a song's tempo and popularity
        """
        q = '''
            SELECT TrackData.Popularity, AnalysisData.Tempo
            FROM TrackData
            INNER JOIN AnalysisData
            ON TrackData.ID = AnalysisData.ID
            '''
        results = self._query(q)
        data = []
        for row in results:
            data.append({
                'Popularity': row[0],
                'Tempo': row[1]
            })
        return data
    
    def get_training_validation_data(self, training_split=0.8):
        """
        Method to get a set of training and validation data from the database. Can be called as such:
            x_train, y_train, x_valid, y_valid = SqlClient.get_training_validation_data()
        
        :param training_split: decimal - split data according to this value - default is 80% training (and thus 20% validation)
        """
        q = '''
            SELECT AnalysisData.Acousticness, 
                   AnalysisData.Danceability, 
				   AnalysisData.Energy, 
				   AnalysisData.Instrumentalness,
				   AnalysisData.Key,
				   AnalysisData.Liveness,
				   AnalysisData.Loudness,
				   AnalysisData.Mode,
				   AnalysisData.Speechiness,
				   AnalysisData.Tempo,
				   AnalysisData.Time_Signature,
				   AnalysisData.Valence,
				   TrackData.Popularity
            FROM TrackData
            INNER JOIN AnalysisData
            ON TrackData.ID = AnalysisData.ID
            '''
        results = self._query(q)
        random.shuffle(results)
        data = np.array(results)
        data_length = len(data)

        # split data into inputs and outputs (x and y)
        x_full = data[:,:-1]
        y_full = data[:,-1]

        x_train = x_full[:int(data_length*training_split)]
        y_train = y_full[:int(data_length*training_split)]

        x_valid = x_full[int(data_length*training_split):]
        y_valid = y_full[int(data_length*training_split):]

        return x_train, y_train, x_valid, y_valid
    
    def get_random_datapoint(self):
        """
        Simply gets a random datapoint from the database
        """
        q = '''
            SELECT AnalysisData.Acousticness, 
                   AnalysisData.Danceability, 
				   AnalysisData.Energy, 
				   AnalysisData.Instrumentalness,
				   AnalysisData.Key,
				   AnalysisData.Liveness,
				   AnalysisData.Loudness,
				   AnalysisData.Mode,
				   AnalysisData.Speechiness,
				   AnalysisData.Tempo,
				   AnalysisData.Time_Signature,
				   AnalysisData.Valence,
				   TrackData.Popularity
            FROM TrackData
            INNER JOIN AnalysisData
            ON TrackData.ID = AnalysisData.ID
            '''
        results = self._query(q)
        random.shuffle(results)
        data = np.array(results)
        return data[0,:]


    def __del__(self):
        """
        This method is called when the object gets deleted. Leveraged to close the connection on object garbage collection.
        """
        self._conn.close()
