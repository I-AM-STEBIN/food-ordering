
def add():
    print("**** ADDITION ****")
    a=int(input("Enter a value:"))
    b=int(input("Enter a value:"))
    print("The total:",a+b)

def sub():
    print("**** SUBTRATION ****")
    a=int(input("Enter a value:"))
    b=int(input("Enter a value:"))
    print("The total:",a-b)

def multi():
    print("**** MULTIPLICATION ****")
    a=int(input("Enter a value:"))
    b=int(input("Enter a value:"))
    print("The total:",a*b)

def div():
    print("**** DIVISION ****")
    a=int(input("Enter a value:"))
    b=int(input("Enter a value:"))
    print("The total:",a/b)

def guess():
    secret=6
    print("**** NUMBER GUESSER ****")
    a=int(input("Enter the number:"))
    while secret==a:
        print("correct")
        break
    if secret>a:
        print("*** too Low ***")
    elif secret<a:
        print("*** too High ***")




while True:
    print("\n===== MAIN MENU =====")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. NUMBER GUESSER")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        add()
    elif choice == '2':
        sub()
    elif choice == '3':
        multi()
    elif choice == '4':
        div()
    elif choice == '5':
        guess()    
    elif choice == '6':
        print("Exit")
        continue
    else:
        print("Invalid choice try again,")
