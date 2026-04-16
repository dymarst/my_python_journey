from datetime import datetime
from user.menu import menu_user
from adm.menu import menu_admin
import database.crud as database
import bcrypt

def login():
    max_attempt = 3
    attempt = 0
    while max_attempt > attempt:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        hasil = database.select("users", "username", username)
        if hasil:
            stored_hash = hasil['password']
            if bcrypt.checkpw(password.encode(), stored_hash.encode()):
                database.update("users", "last_login", "username", datetime.now(), username)
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