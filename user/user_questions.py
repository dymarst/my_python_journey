from database.database import Database

database = Database()

def ask(username):
    pertanyaan = input("masukan pertanyaan : ")
    database.insert("ask", {"username" : username, "pertanyaan" : pertanyaan})
    print(f"kamu berhasil nanya {pertanyaan}")

def cek_pertanyaan(username):
    user = database.select("ask", "username", username)

    if user:
        print(f"\nUsername : {username}")
        print(f"pertanyaan : {user['pertanyaan']}")
        print(f"jawaban : {user['jawaban'] if user['jawaban'] else "belum dijawab"}")
    else:
        print("kamu tidak punya pertanyaan")