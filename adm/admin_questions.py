def show_questions(cursor, db):
    cursor.execute("SELECT id, username, pertanyaan, jawaban FROM ask")
    pertanyaan_all = cursor.fetchall()

    if not pertanyaan_all:
        print("tidak ada pertanyaan")

    for pertanyaan in pertanyaan_all:
        print(f"\nID : {pertanyaan['id']}")
        print(f"Username : {pertanyaan['username']}")
        print(f"Pertanyaan : {pertanyaan['pertanyaan']}")
        print(f"Jawaban : {pertanyaan['jawaban'] if pertanyaan['jawaban'] else 'belum di jawab'}")

def answer(cursor, db):
    id_pertanyaan = input("masukan id pertanyaan : ")
    jawaban = input("masukan jawaban : ")
    cursor.execute("UPDATE ask set jawaban = %s WHERE id = %s", (jawaban, id_pertanyaan))
    db.commit()
    print(f"berhasil jawab pertanyaan id : {id_pertanyaan}")

def del_questions(cursor, db):
    try:
        id_pertanyaan = int(input("hapus pertanyaan (id) :"))
    except ValueError:
        print("ID harus berupa angka")

    cursor.execute("SELECT * FROM ask WHERE id = %s", (id_pertanyaan,))
    pertanyaan = cursor.fetchone()
    if pertanyaan is None:
        print("id pertanyaan tidak ditemukan")
        return

    cursor.execute("DELETE FROM ask WHERE id = %s", (id_pertanyaan,))
    db.commit()
    print(f"kamu telah menghapus pertanyaan id : {id_pertanyaan}")