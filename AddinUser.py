
print("Available commands")
print("1 Add user")
print("2 Delete user")
command = input("Choose one of options!")

if command == "1":
    print("Adding user")
elif command == "2":
    print("Deleting user")
else:
    print("Unkown command:" + command) #Prints the text and the user's input


n = int(input("Plz choose a nummber"))

for i in range(0,n):
    print("Enter 1 for adding user 1\n")
    print("Enter 2 for adding user 2\n")

    choice = int(input("Enter your choice"))

    if choice == 1:
        print("Adding user")
    elif choice == 2:
        print("Deleting user")
    else:
        print("Invalid choice")
