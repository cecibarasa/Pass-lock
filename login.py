from user import User

def displayMenu():
    print("-"*20)
    status = input("Are you registered user? y/n?").lower()
    if status == "y":
        login()
    elif status == "n":
        register()
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    password2 = input("Confirm password: ")
    # validation
    if password == password2:
        user = User(username, password)
        user.save_user
        print(f"Welcome {username}! You're now registered")
        print("Lets Login")
        print(login())
    else:
        print("Something went wrong. Please try again.")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User(username, password)
    if user is not None:
        user.login
        print(f"Welcome {username}! You're now Logged In")
    else:
        print("Invalid Username or Password.")
displayMenu()