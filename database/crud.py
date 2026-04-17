from database.db import connect_db
from psycopg2.extras import RealDictCursor

def _conn():
    conn = connect_db()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cursor

def insert(table, data: dict):
    conn, cursor = _conn()

    columns = ", ".join(data.keys())
    placeholders = ", ".join(["%s"] * len(data))
    values = tuple(data.values())

    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def select(table, key, value):
    conn, cursor = _conn()
    sql = f"SELECT * FROM {table} WHERE {key} = %s"
    cursor.execute(sql, (value,))
    result = cursor.fetchone()
    conn.close()
    return result

def select_all(table):
    conn, cursor = _conn()
    sql = f"SELECT * FROM {table}"
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result

def delete(table, key, value):
    conn, cursor = _conn()
    sql = f"DELETE FROM {table} WHERE {key} = %s"
    cursor.execute(sql, (value,))
    conn.commit()
    conn.close()

def update(table, test, key, value1, value2):
    conn, cursor = _conn()
    sql = f"UPDATE {table} set {test} = %s WHERE {key} = %s"
    cursor.execute(sql, (value1, value2))
    conn.commit()
    conn.close()