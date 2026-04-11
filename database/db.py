import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="test"
        )

        if db.is_connected():
            print("Koneksi ke MySQL berhasil")
            return db

    except Error as e:
        print("Koneksi gagal:", e)
        return None