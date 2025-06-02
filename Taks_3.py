print("Welcome to Password Complexity Checker!!!\nOptions:\n1. Check\t2. Exit\n")

def check(pas):
    sug = "Suggestions:"
    faults = 0
    sugpas = pas
    
    if len(pas) < 8:
        faults += 1
        sug += f"\n{faults}. Password must contain at least 8 characters."
    
    if not any(c.islower() for c in pas):
        faults += 1
        sug += f"\n{faults}. Password must contain at least 1 lowercase alphabet."
        sugpas += 'q'
    
    if not any(c.isupper() for c in pas):
        faults += 1
        sug += f"\n{faults}. Password must contain at least 1 uppercase alphabet."
        sugpas += 'Q'
    
    if not any(c.isdigit() for c in pas):
        faults += 1
        sug += f"\n{faults}. Password must contain at least 1 numeric digit."
        sugpas += '0'
    
    if not any(not c.isalnum() for c in pas):
        faults += 1
        sug += f"\n{faults}. Password must contain at least 1 special character."
        sugpas += '$'

    while len(sugpas) < 8:
        sugpas += 'p'

    print(f"\nPassword Strength: {5 - faults} / 5")
    if faults:
        print(sug)
        print(f"Example: {sugpas}")
    print('\n')

while True:
    try:
        opt = int(input("Enter option: "))
        if opt == 1:
            pas = input("Enter password: ")
            check(pas)
        elif opt == 2:
            print("\nThank you!!")
            break
        else:
            print("Invalid Option!")
    except ValueError:
        print("Invalid input! Please enter a number (1 or 2).")
