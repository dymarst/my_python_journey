import bcrypt

def lihat_data(cursor, username):
    cursor.execute("SELECT username, telepon, hobi FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()

    print(f"\nUsername : {user['username']}")
    print(f"No HP    : {user['telepon'] if user['telepon'] else 'Tidak ada'}")
    print(f"Hobi     : {user['hobi'] if user['hobi'] else 'Tidak ada'}")

def isi_telepon(cursor, db, username):
    telepon = input("Masukkan No HP: ").strip()
    cursor.execute("UPDATE users SET telepon=%s WHERE username=%s", (telepon, username))
    db.commit()
    print(f"berhasil menambahkan nomer telepon {telepon}")

def isi_hobi(cursor, db, username):
    hobi = input("Masukkan HOBI: ").strip()
    cursor.execute("UPDATE users SET hobi=%s WHERE username=%s", (hobi, username))
    db.commit()
    print(f"berhasil menambahkan hobi {hobi}")

def del_akun(cursor, db, username):
    confirm = input("Apakah yakin ingin menghapus akun? (y/n): ").strip().lower()
    if confirm == "y":
        cursor.execute("DELETE FROM users WHERE username=%s", (username,))
        db.commit()
        
        print("Akun berhasil dihapus!")
        return True
    else:
        print("Batal menghapus akun.")

def ganti_password(cursor, db, username):
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    hasil = cursor.fetchone()
    password = hasil['password']
    old_password = input("password lama : ")
    if bcrypt.checkpw(old_password.encode(), password.encode()):
        new_password = input("password baru : ")
        hashed_new = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        confirm = input("Apakah yakin ingin mengganti password? (y/n): ").strip().lower()
        if confirm == "y":
            cursor.execute("UPDATE users SET password=%s WHERE username=%s", (hashed_new, username))
            db.commit()
        
            print("Password berhasil diganti")
        else:
            print("Batal menghapus akun.")
            print(f"password yang baru {new_password}")
    else: 
        print("password salah!")