from user import User
from termcolor import colored, cprint

def displayMenu():
    cprint("-"*20, "yellow")
    status = input("Are you registered user? y/n?  "  ).lower()
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
        cprint(f"Welcome {username}! You're now registered", "yellow")
        cprint("Lets Login", "yellow")
        print(login())
    else:
        print("Something went wrong. Please try again.")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User(username, password)
    
    if user is not None:
        user.login
        cprint(f"Welcome {username}! You're now Logged In", "yellow")
    else:
        cprint("Invalid Username or Password.", "red")

def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)         
displayMenu()