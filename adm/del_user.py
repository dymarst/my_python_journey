from database.database import Database

database = Database()

def hapus_user():

    try:
        id_user = int(input("Masukkan ID user yang akan dihapus: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    user = database.select("users", "id", id_user)
    if user is None:
        print("User dengan ID tersebut tidak ditemukan.")
        return

    database.delete("users", "id", id_user)
    print(f"User '{user['username']}' dengan ID {id_user} berhasil dihapus.")