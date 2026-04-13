from datetime import datetime
from user.menu import menu_user
from adm.menu import menu_admin
import bcrypt

def login(cursor, db):
    max_attempt = 3
    attempt = 0
    while max_attempt > attempt:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        hasil = cursor.fetchone()
        if hasil:
            stored_hash = hasil['password']
            if bcrypt.checkpw(password.encode(), stored_hash.encode()):
                cursor.execute("UPDATE users SET last_login = %s WHERE username = %s" , (datetime.now(), username))
                db.commit()
                if hasil['role'] == 'admin':
                    print("kamu adalah admin")
                    menu_admin()
                else:
                    menu_user(username)
                return
            else:
                attempt += 1
                print(f"username atau password salah, sisa percobaan({attempt}/3)")
        else:
            attempt += 1
            print(f"username atau password salah, sisa percobaan({attempt}/3)")
    print("Silahkan buat akun jika lupa password lama")