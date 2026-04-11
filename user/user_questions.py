def ask(cursor, db, username):
    pertanyaan = input("masukan pertanyaan : ")
    cursor.execute("INSERT INTO ask (username, pertanyaan) VALUES (%s, %s)", (username, pertanyaan))
    db.commit()
    print(f"kamu berhasil nanya {pertanyaan}")