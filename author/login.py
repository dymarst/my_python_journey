from user.menu import menu_user
from adm.menu import menu_admin
def login(cursor, db):
    max_attempt = 3
    attempt = 0
    while max_attempt > attempt:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        hasil = cursor.fetchone()
        if hasil:
            if username == "dymarr":
                print("kamu adalah admin")
                menu_admin(cursor, db)
            else:
                menu_user(cursor, db, username)
            return
        else:
            attempt += 1
            print(f"username atau password salah, sisa percobaan({attempt}/3)")
    print("Silahkan buat akun jika lupa password lama")