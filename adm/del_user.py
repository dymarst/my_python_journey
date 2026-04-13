def hapus_user(cursor, db):
    try:
        id_user = int(input("Masukkan ID user yang akan dihapus: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    cursor.execute("SELECT * FROM users WHERE id=%s", (id_user,))
    user = cursor.fetchone()
    if user is None:
        print("User dengan ID tersebut tidak ditemukan.")
        return

    cursor.execute("DELETE FROM users WHERE id=%s", (id_user,))
    db.commit()
    print(f"User '{user['username']}' dengan ID {id_user} berhasil dihapus.")