def ask(cursor, db, username):
    pertanyaan = input("masukan pertanyaan : ")
    cursor.execute("INSERT INTO ask (username, pertanyaan) VALUES (%s, %s)", (username, pertanyaan))
    db.commit()
    print(f"kamu berhasil nanya {pertanyaan}")

def cek_pertanyaan(cursor, username):
    cursor.execute("SELECT pertanyaan, jawaban FROM ask WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        print(f"\nUsername : {username}")
        print(f"pertanyaan : {user['pertanyaan']}")
        print(f"jawaban : {user['jawaban'] if user['jawaban'] else "belum dijawab"}")
    else:
        print("kamu tidak punya pertanyaan")