from user.profile import lihat_data, isi_telepon, isi_hobi, del_akun, ganti_password
from user.user_questions import ask, cek_pertanyaan

def menu_user(username):
    print("berhasil login")
    while True:
        print("\n === MENU USER ===")
        print("1. Lihat data")
        print("2. isi no hp")
        print("3. isi hobi")
        print("4. hapus akun")
        print("5. ganti password")
        print("6. ask to admin")
        print("7. lihat pertanyaan")
        print("ketik apapun untuk keluar")
        chose = input("mau apa? :")
        if chose == "1":
            lihat_data(username)
        elif chose == "2":
            isi_telepon(username)
        elif chose == "3":
            isi_hobi(username)
        elif chose == "4":
            del_akun(username)
            break
        elif chose == "5":
            ganti_password(username)
        elif chose == "6":
            ask(username)
        elif chose == "7":
            cek_pertanyaan(username)
        else:
            break