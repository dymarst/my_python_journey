import bcrypt

def register(cursor, db):
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    
    if cursor.fetchone():            
        print("Username sudah digunakan, silakan pilih username lain.\n")
    else:
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed))
        db.commit()

        print("Akun berhasil dibuat!")