from database.db import connect_db
from author.login import login
from author.register import register
import bcrypt

def main():
    db = connect_db()

    if db is None:
        print("Program dihentikan karena database tidak connect")
        return
    cursor = db.cursor(dictionary=True)
    print("1. login")
    print("2. daftar")
    pilihan = input("mau apa? (1/2):")
    if pilihan == "1":
        login(cursor, db)
    elif pilihan == "2":
        register(cursor, db)
    db.close()

main()