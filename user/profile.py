import bcrypt
import database.crud as database

def lihat_data(username):
    user = database.select("users", "username", username)

    print(f"\nUsername : {user['username']}")
    print(f"Number Phone    : {user['number_phone']}")
    print(f"Hobby     : {user['hobby']}")

def set_number_phone(username):
    number_phone = input("Masukkan No HP: ").strip()
    database.update("users", "number_phone", "username", number_phone, username)
    print(f"berhasil menambahkan nomer nomer telepon {number_phone}")

def set_user_hobby(username):
    hobby = input("Masukkan hobby: ").strip()
    database.update("users", "hobby", "username", hobby, username)
    print(f"berhasil menambahkan hobi {hobby}")

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
        hashed_new = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        confirm = input("Apakah yakin ingin mengganti password? (y/n): ").strip().lower()
        if confirm == "y":
            database.update("users", "password", "username", hashed_new, username)
  
            print("Password berhasil diganti")
        else:
            print("Batal menghapus akun.")
            print(f"password yang baru {new_password}")
    else: 
        print("password salah!")