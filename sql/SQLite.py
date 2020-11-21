import sqlite3


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

    def __del__(self):
        """
        This method is called when the object gets deleted. Leveraged to close the connection on object garbage collection.
        """
        self._conn.close()
