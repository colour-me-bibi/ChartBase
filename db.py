import sqlite3

def initDB(dbFile = 'ChartBase.db'):
    with sqlite3.connect(dbFile) as conn:
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS songs (
        url TEXT NOT NULL UNIQUE,
        source TEXT
        )""")

        conn.commit()

        return conn

def insertSong(conn, url, source):
    c = conn.cursor()

    c.execute('INSERT INTO songs VALUES (?, ?)', (url, source))

    conn.commit()

def clearDB(conn):
    c = conn.cursor()

    c.execute('DELETE FROM songs')

    conn.commit()


if __name__ == '__main__':
    conn = initDB()
