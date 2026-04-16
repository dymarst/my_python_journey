from adm.del_user import hapus_user
from adm.show_data import all_data
from user.menu import menu_user
from adm.admin_questions import show_questions, answer, del_questions
from database.db import connect_db

def menu_admin():
    while True:
        print("\n === MENU ADMIN ===")
        print("1. View all users")
        print("2. Delete user")
        print("3. Login as User")
        print("4. View questions")
        print("5. Answer question")
        print("6. Delete question")
        pilihan = input("mau apa? : ")
        
        if pilihan == "1":
            all_data()
        elif pilihan == "2":
            hapus_user()
        elif pilihan == "3":
            menu_user("dymarr")
        elif pilihan == "4":
            show_questions()
        elif pilihan == "5":
            answer()
        elif pilihan == "6":
            del_questions()
        else:
            break