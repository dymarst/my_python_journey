def lihat_data(cursor, username):
    cursor.execute("SELECT username, telepon, hobi FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()

    print(f"\nUsername : {user[0]}")
    print(f"No HP    : {user[1] if user[1] else 'Tidak ada'}")
    print(f"Hobi     : {user[2] if user[2] else 'Tidak ada'}")

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
    cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
    password = cursor.fetchone()
    password_lama = input("password lama : ")
    if password_lama == password[0]:
        password_baru = input("password baru : ")
        confirm = input("Apakah yakin ingin mengganti password? (y/n): ").strip().lower()
        if confirm == "y":
            cursor.execute("UPDATE users SET password=%s WHERE username=%s", (password_baru, username))
            db.commit()
            
            print("Password berhasil diganti")
        else:
            print("Batal menghapus akun.")
            print(f"password yang baru {password_baru}")
    else:
        print("password salah!")