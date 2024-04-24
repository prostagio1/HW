from utils import menu
from utils import register
from utils import add_funds
from utils import transfer


db = []
valid_operations = ["1","2","3","4"]

def main():
    while True:
        menu()
        user_input = input("Please enter the operation: ")
        if user_input not in valid_operations:
            print("Invalid Operation!")
            continue
        if user_input == "1":
            user = register()
            if user:
                db.append(user)
                print(db)
            else:
                print("Invalid Inputs! ")
        if user_input == "2":
            add_funds(db)
            print(db)
        if user_input == "3":
            transfer(db)
            print(db)
        if user_input == "4":
            print("Thanks for using our application!")
            break



if __name__ == "__main__":
    main()