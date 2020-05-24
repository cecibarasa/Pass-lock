#!/usr/bin/env python3.6
import pyperclip
import random
from user import User
from credentials import Credentials
import login
from termcolor import colored, cprint

def create_user(service_provider, username, password):
    '''
    Create User
    '''
    new_user = User( username, password)
    return new_user

def create_credentials(service_provider, username, password):
    '''
    Create credentials
    '''
    new_credentials = Credentials(service_provider, username, password)
    return new_credentials

def save_user(user):
    '''
    save user
    '''
    user.save_user()

def save_credentials(credentials):
    '''
    save user credentials
    '''
    credentials.save_credentials()

def delete_user(user):
    '''
    delete saved user
    '''
    user.delete_user()

def delete_credentials(credentials):
    '''
    delete saved credentials
    '''
    credentials.delete_credentials()

def display_user():
    '''
    Method to display saved user
    '''
    return User.display_user()

def display_credentials():
    '''
    Method to display user credentials
    '''
    return Credentials.display_credentials()

def find_user_by_username(cls,username):
        '''
        Method that takes in a service provider and returns a user that matches that service provider.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user    


def main():
    print("Welcome to The Password Locker, select any option")

    while True:
        print("\n 1- Main menu \n 2- Create a new user account with your own password  \n 3- Register new credentials with auto-generated password \n 4- Display existing users \n 5- Delete Account \n 6- Exit")

        option_1 = input()
        if option_1 == '1':
            print("displayMenu()")

        elif option_1 == '2':
            
            print("New User")
            cprint("-"*50, "yellow")

            print("service provider...")
            service_provider = input()

            print("username..")
            username = input()

            print("password..")
            password = input()
            pyperclip.copy(password)
            #password = pyperclip.paste()
            
            save_user(create_user(service_provider, username, password))
            save_credentials(create_credentials(service_provider, username, password))
            print("\n")
            
            print(f"The {service_provider} account by {username} with {password} password has been successfully registered")
            #print(f"{username} your password is {password}")

            print("\n")

        elif option_1 == '3':
            no_of_accounts = int(input("How many accounts would you like to have?"))
            for i in range(no_of_accounts):
                print("New User")
                cprint("-" * 40, "yellow")
                
                print("service provider")
                service_provider = input()

                print("username")
                username = input()

                chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                digits = '0123456789'
                symbols = '`#^*&$|<>}+@!~=-+_'
                length = input('password length?')
                length = int(length)
                combined_pass = chars + digits + symbols

                password = ''
                # for i in range(length):
                #     password = random.choice(combined_pass)
                
                for i in range(length):
                    password += random.choice(combined_pass)
                print(password)

                save_user(create_user(service_provider, username, password))
                save_credentials(create_credentials(service_provider, username, password))

                print("\n")

                print(f"The {service_provider} account by {username} has been successfully registered")
                print(f"Your password is {password}")

        elif option_1 == '4':

            if display_user():
                print("Here is a alist of all the accounts")
                print("\n")

                for user in display_user():
                    cprint(f"Hey {user.username} your {user.password} password is safely stored!", "yellow")
                    print("\n")

        elif option_1 == '5':
            print("\n")
            
            # for credentials in save_credentials(credential.username):
            #     print(f"Are you sure you want to delete {credential.username} ?")
            #     print("\n")
            #     return Credentials.credentials_list.remove(credential.username)            

        elif option_1 == '6':
            print("\n")
            cprint("Thank you for your time!", "green")
            break
        else:
            cprint("Sorry wrong input", "red")
    

if __name__ == '__main__':
    main()