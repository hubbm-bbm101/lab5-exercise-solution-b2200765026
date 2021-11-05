valid = False
while not valid:
    email = input("enter your email ")
    if "@" in email:
        if "." in email:
            print("This is a valid email")
            valid = True
        else:
            print("This is not a valid email")
            valid = False
    else:
        print("This is not a valid email")
        valid = False


