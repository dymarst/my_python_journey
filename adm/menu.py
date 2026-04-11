from adm.del_user import hapus_user
from adm.show_data import all_data
from user.menu import menu_user
from adm.admin_questions import show_questions, answer

def menu_admin(cursor, db):

    while True:
        print("\n === MENU ADMIN ===")
        print("1. View all users")
        print("2. Delete user")
        print("3. Login as User")
        print("4. View questions")
        print("5. Answer question")
        pilihan = input("mau apa? : ")
        
        if pilihan == "1":
            all_data(cursor)
        elif pilihan == "2":
            hapus_user(cursor, db)
        elif pilihan == "3":
            menu_user(cursor, db, "dymarr")
        elif pilihan == "4":
            show_questions(cursor, db)
        elif pilihan == "5":
            answer(cursor, db)
        else:
            break