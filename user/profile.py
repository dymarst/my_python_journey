import bcrypt
import database.crud as database

def lihat_data(username):
    user = database.select("users", "username", username)

    print(f"\nUsername : {user['username']}")
    print(f"No HP    : {user['telepon'] if user['telepon'] else 'Tidak ada'}")
    print(f"Hobi     : {user['hobi'] if user['hobi'] else 'Tidak ada'}")

def isi_telepon(username):
    telepon = input("Masukkan No HP: ").strip()
    database.update("users", "telepon", "username", telepon, username)
    print(f"berhasil menambahkan nomer telepon {telepon}")

def isi_hobi(username):
    hobi = input("Masukkan HOBI: ").strip()
    database.update("users", "hobi", "username", hobi, username)
    print(f"berhasil menambahkan hobi {hobi}")

def del_akun(username):
    confirm = input("Apakah yakin ingin menghapus akun? (y/n): ").strip().lower()
    if confirm == "y":
        database.delete("users", "username", username)
        
        print("Akun berhasil dihapus!")
        return True
    else:
        print("Batal menghapus akun.")

def ganti_password(username):
    hasil = database.select("users", "username", username)
    password = hasil['password']
    old_password = input("password lama : ")
    if bcrypt.checkpw(old_password.encode(), password.encode()):
        new_password = input("password baru : ")
        hashed_new = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        confirm = input("Apakah yakin ingin mengganti password? (y/n): ").strip().lower()
        if confirm == "y":
            database.update("users", "password", "username", hashed_new, username)
  
            print("Password berhasil diganti")
        else:
            print("Batal menghapus akun.")
            print(f"password yang baru {new_password}")
    else: 
        print("password salah!")