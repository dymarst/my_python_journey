from author.login import login
from author.register import register
import bcrypt

def main():
    print("1. login")
    print("2. daftar")
    pilihan = input("mau apa? (1/2):")
    if pilihan == "1":
        login()
    elif pilihan == "2":
        register()

main()