import bcrypt
from database.database import Database

def register():
    database = Database()
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    
    user = database.select("users", "username", username)
    
    if user:            
        print("Username sudah digunakan, silakan pilih username lain.\n")
    else:
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        database.insert("users", {"username" : username, "password" : hashed})
        print("Akun berhasil dibuat!")