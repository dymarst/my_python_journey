import bcrypt
import database.crud as database

def register():
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    
    user = database.select("users", "username", username)
    
    if user:            
        print("Username sudah digunakan, silakan pilih username lain.\n")
    else:
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        database.insert("users", {"username" : username, "password" : hashed})
        print("Akun berhasil dibuat!")