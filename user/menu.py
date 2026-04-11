from user.profile import lihat_data, isi_telepon, isi_hobi, del_akun, ganti_password

def menu_user(cursor, db, username):
    print("berhasil login")
    while True:
        print("\n === MENU USER ===")
        print("1. Lihat data")
        print("2. isi no hp")
        print("3. isi hobi")
        print("4. hapus akun")
        print("5. ganti password")
        print("ketik apapun untuk keluar")
        chose = input("mau apa? :")
        if chose == "1":
            lihat_data(cursor, username)
        elif chose == "2":
            isi_telepon(cursor, db, username)
        elif chose == "3":
            isi_hobi(cursor, db, username)
        elif chose == "4":
            del_akun(cursor, db, username)
            break
        elif chose == "5":
            ganti_password(cursor, db, username)
        else:
            break