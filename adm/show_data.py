def all_data(cursor):
    cursor.execute("SELECT id, username, telepon, hobi, last_login FROM users")
    users = cursor.fetchall()

    if not users:
        print("Belum ada data pengguna.")
        return

    for user in users:
        print(f"\nID       : {user[0]}")
        print(f"Username : {user[1]}")
        print(f"No HP    : {user[2] if user[2] else 'Tidak ada'}")
        print(f"Hobi     : {user[3] if user[3] else 'Tidak ada'}")
        print(f"last login : {user[4]}")