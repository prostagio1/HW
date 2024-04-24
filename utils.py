import validators

def menu():
    print("1. Register User")
    print("2. Add balance")
    print("3. Transfer Funds")
    print("4. Quit")

def register():
    name = input("Please enter the name and surname of the user: ")
    iban = input("Please enter the IBAN of the user: ")
    initial_balance = input("Please enter the initial balance: ")
    if validators.validate_iban(iban) and validators.validate_balance(initial_balance):
        user = {"name": name, "IBAN": iban, "Balance": float(initial_balance)}
        return (user)
    else:
        return (False)
    
def add_funds(db):
    iban = input("Please enter the IBAN: ")
    amount = input("Please enter the amount: ")
    if validators.validate_balance(amount) and validators.validate_iban:
        for i in db:
            if i.get("IBAN") == iban:
                i["Balance"] = i["Balance"] + float(amount)
    else:
        print("Invalid Inputs! ")


def check_existance(iban,db):
    exists = False
    for i in db:
        if i.get("IBAN") == iban:
            exists = True
    return exists


def transfer(db):
    iban1 = input("From where: ")
    iban2 = input("To where: ")
    amount = input("Amount: ")
    if validators.validate_iban(iban1) and validators.validate_iban(iban2) and validators.validate_balance(amount):
        amount = float(amount)
    if check_existance(iban1,db) and check_existance(iban2,db):
        balance1 = 0
        for i in db:
            if i.get("IBAN") == iban1:
                balance1 = i.get("Balance")
        if balance1 > amount:
            for i in db:
                if i.get("IBAN") == iban1:
                    i["Balance"] = i["Balance"] - amount
                if i.get("IBAN") == iban2:
                    i["Balance"] = i["Balance"] + amount
        else:
            print("Not Enough Funds! ")
        






    