import sqlite3


def initDB(dbFile='ChartBase.db'):
    with sqlite3.connect(dbFile) as conn:
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS links (
        url TEXT NOT NULL UNIQUE,
        source TEXT,
        downloaded INTEGER NOT NULL
        )""")

        c.execute("""CREATE TABLE IF NOT EXISTS songs (
        name TEXT,
        url TEXT NOT NULL UNIQUE,
        source TEXT,
        hash TEXT,
        path TEXT,
        clean INTEGER
        )""")

        conn.commit()

        return conn


def insertSong(conn, url, source):
    c = conn.cursor()

    c.execute('INSERT INTO songs VALUES (?, ?, ?)', (url, source, 0))

    conn.commit()


def clearDB(conn):
    c = conn.cursor()

    c.execute('DELETE FROM songs')

    conn.commit()


if __name__ == '__main__':
    conn = initDB()
