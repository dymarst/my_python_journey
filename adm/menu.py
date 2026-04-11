from adm.admin import all_data, hapus_user
from user.menu import menu_user

def menu_admin(cursor, db):

    while True:
        print("\n === MENU ADMIN ===")
        print("1. daftar semua pengguna")
        print("2. hapus akun user (gunakan ID)")
        print("3. login sebagai user")
        pilihan = input("mau apa? : ")
        
        if pilihan == "1":
            all_data(cursor)
        elif pilihan == "2":
            hapus_user(cursor, db)
        elif pilihan == "3":
            menu_user(cursor, db, "dymarr")
        else:
            break