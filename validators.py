def validate_iban(iban):
    if len(iban) == 5 and iban.startswith("TB") and iban[2:].isdigit():
        return True
    else:
        return False
    
def validate_balance(amount):
    if amount.replace(".","").replace("-","").isdigit():
        return True
    else:
        return False
    
