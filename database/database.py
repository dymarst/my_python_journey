from database.db import connect_db

class Database:

    def _conn(self):
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        print("loop terus ni")
        return conn, cursor

    def insert(self, table, data: dict):
        conn, cursor = self._conn()

        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        values = tuple(data.values())

        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    def select(self, table, key, value):
        conn, cursor = self._conn()
        sql = f"SELECT * FROM {table} WHERE {key} = %s"
        cursor.execute(sql, (value,))
        result = cursor.fetchone()
        conn.close()
        return result
    
    def select_all(self, table):
        conn, cursor = self._conn()
        sql = f"SELECT * FROM {table}"
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

    def delete(self, table, key, value):
        conn, cursor = self._conn()
        sql = f"DELETE FROM {table} WHERE {key} = %s"
        cursor.execute(sql, (value,))
        conn.commit()
        conn.close()

    def update(self, table, test, key, value1, value2):
        conn, cursor = self._conn()
        sql = f"UPDATE {table} set {test} = %s WHERE {key} = %s"
        cursor.execute(sql, (value1, value2))
        conn.commit()
        conn.close()