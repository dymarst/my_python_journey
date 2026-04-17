import psycopg2

def connect_db():
    try:
        db = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="dymarr",
            database="test",
            port=5432
        )           
        return db

    except:
        print("Gagal terhubung ke database.")
        return None