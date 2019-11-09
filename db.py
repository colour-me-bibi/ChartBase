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
        url TEXT,
        source TEXT,
        hash TEXT NOT NULL UNIQUE,
        path TEXT
        )""")

        conn.commit()

        return conn


def clearDB(conn):
    c = conn.cursor()

    c.execute('DELETE FROM songs')

    conn.commit()
