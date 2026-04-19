import database.crud as database

def show_questions():

    pertanyaan_all = database.select_all("ask")

    if not pertanyaan_all:
        print("tidak ada pertanyaan")

    for pertanyaan in pertanyaan_all:
        print(f"\nID : {pertanyaan['id']}")
        print(f"Username : {pertanyaan['username']}")
        print(f"Pertanyaan : {pertanyaan['question']}")
        print(f"Jawaban : {pertanyaan['answer']}")

def answer():
    id_pertanyaan = input("masukan id pertanyaan : ")
    answer = input("masukan jawaban : ")
    database.update("ask", "answer", "username", answer, id_pertanyaan)
    print(f"berhasil jawab pertanyaan id : {id_pertanyaan}")

def del_questions():
    try:
        id_pertanyaan = int(input("hapus pertanyaan (id) :"))
    except ValueError:
        print("ID harus berupa angka")

    pertanyaan = database.select("ask", "id", id_pertanyaan)
    if pertanyaan is None:
        print("id pertanyaan tidak ditemukan")
        return

    database.delete("ask", "id", id_pertanyaan)
    print(f"kamu telah menghapus pertanyaan id : {id_pertanyaan}")