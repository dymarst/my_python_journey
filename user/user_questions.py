import database.crud as database

def ask(username):
    result = database.select_all2("ask", "username", username)
    if len(result) >= 2:
        print("kamu sudah memiliki dua pertanyaan")
    else:    
        pertanyaan = input("masukan pertanyaan : ")
        database.insert("ask", {"username" : username, "pertanyaan" : pertanyaan})
        print(f"kamu berhasil nanya {pertanyaan}")

def cek_pertanyaan(username):
    user = database.select_all2("ask", "username", username)
    index = 1

    if user:
        for users in user:
            print(f"\nPertanyaan ke : {index}")
            print(f"Username : {username}")
            print(f"pertanyaan : {users['pertanyaan']}")
            print(f"jawaban : {users['jawaban']}")
            index += 1
    else:
        print("kamu tidak punya pertanyaan")