from database.database import Database

database = Database()

def show_questions():

    pertanyaan_all = database.select_all("ask")

    if not pertanyaan_all:
        print("tidak ada pertanyaan")

    for pertanyaan in pertanyaan_all:
        print(f"\nID : {pertanyaan['id']}")
        print(f"Username : {pertanyaan['username']}")
        print(f"Pertanyaan : {pertanyaan['pertanyaan']}")
        print(f"Jawaban : {pertanyaan['jawaban'] if pertanyaan['jawaban'] else 'belum di jawab'}")

def answer():
    id_pertanyaan = input("masukan id pertanyaan : ")
    jawaban = input("masukan jawaban : ")
    database.update("ask", "jawaban", "username", jawaban, id_pertanyaan)
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