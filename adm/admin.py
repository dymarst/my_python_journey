def all_data(cursor):
    cursor.execute("SELECT id, username, telepon, hobi FROM users")
    users = cursor.fetchall()

    if not users:
        print("Belum ada data pengguna.")
        return

    for user in users:
        print(f"\nID       : {user[0]}")
        print(f"Username : {user[1]}")
        print(f"No HP    : {user[2] if user[2] else 'Tidak ada'}")
        print(f"Hobi     : {user[3] if user[3] else 'Tidak ada'}")

def hapus_user(cursor, db):
    try:
        id_user = int(input("Masukkan ID user yang akan dihapus: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    cursor.execute("SELECT username FROM users WHERE id=%s", (id_user,))
    user = cursor.fetchone()
    if not user:
        print("User dengan ID tersebut tidak ditemukan.")
        return

    cursor.execute("DELETE FROM users WHERE id=%s", (id_user,))
    db.commit()
    print(f"User '{user[0]}' dengan ID {id_user} berhasil dihapus.")