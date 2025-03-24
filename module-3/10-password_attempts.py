#/usr/bin/python3

correct_password = "secure123"
attempts = 3
for attempt in range(attempts):
    entered_password = input("Enter your password: ")
    if entered_password == correct_password:
        print("Access Granted!")
        break
    else:
        if attempt < attempts - 1:
            print("Incorrect password. Try again.")
        else:
            print("Access Denied!")
