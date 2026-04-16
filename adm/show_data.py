import database.crud as database

def all_data():
    users = database.select_all("users")
    if not users:
        print("Belum ada data pengguna.")
        return

    for user in users:
        print(f"\nID       : {user['id']}")
        print(f"Username : {user['username']}")
        print(f"No HP    : {user['telepon'] if user['telepon'] else 'Tidak ada'}")
        print(f"Hobi     : {user['hobi'] if user['hobi'] else 'Tidak ada'}")
        print(f"last login : {user['last_login']}")