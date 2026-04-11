def show_questions(cursor, db):
    cursor.execute("SELECT id, username, pertanyaan, jawaban FROM ask")
    pertanyaan_all = cursor.fetchall()

    if not pertanyaan_all:
        print("tidak ada pertanyaan")

    for pertanyaan in pertanyaan_all:
        print(f"\nID : {pertanyaan[0]}")
        print(f"Username : {pertanyaan[1]}")
        print(f"Pertanyaan : {pertanyaan[2]}")
        print(f"Jawaban : {pertanyaan[3] if pertanyaan[3] else "belum di jawab"}")

def answer(cursor, db):
    id_pertanyaan = input("masukan id pertanyaan : ")
    jawaban = input("masukan jawaban : ")
    cursor.execute("UPDATE ask set jawaban = %s WHERE id = %s", (jawaban, id_pertanyaan))
    db.commit()
    print(f"berhasil jawab pertanyaan id : {id}")