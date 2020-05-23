#!/usr/bin/env python3.6
import pyperclip
import random
from user import User
from credentials import Credentials

def create_user(service_provider, username, password):
    '''
    Create User
    '''
    new_user = User(service_provider, username, password)
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


def main():
    print("Welcome to The Password Locker, select any option")

    while True:
        print("\n 1 - Create a new user account with your own password  \n 2- Register new credentials with auto-generated password \n 3- Display existing users \n 4- Delete Account \n 5- Exit")

        option_1 = input()

        if option_1 == '1':
            
            print("New User")
            print("-"*20)

            print("service provider...")
            service_provider = input()

            print("username..")
            username = input()

            print("password..")
            password = input()
            
            save_user(create_user(service_provider, username, password))
            save_credentials(create_credentials(service_provider, username, password))
            print("\n")
            
            print(f"The {service_provider} account by {username} with {password} password has been successfully registered")
            #print(f"{username} your password is {password}")

            print("\n")

        elif option_1 == '2':
            no_of_accounts = int(input("How many accounts would you like to have?"))
            for i in range(no_of_accounts):
                print("New User")
                print("-" * 20)
                
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
                # pyperclip.copy(password)
                # password = pyperclip.paste()
                print(password)

                save_user(create_user(service_provider, username, password))
                save_credentials(create_credentials(service_provider, username, password))

                print("\n")

                print(f"The {service_provider} account by {username} has been successfully registered")
                print(f"Your password is {password}")

        elif option_1 == '3':

            if display_user():
                print("Here is a alist of all the accounts")
                print("\n")

                for user in display_user():
                    print(f"{user.service_provider}, has the username {user.username} registered!")
                    print("\n")

        elif option_1 == '4':
            print("\n")
            # for credentials in save_credentials(credential.username):
            #     print(f"Are you sure you want to delete {credential.username} ?")
            #     print("\n")
            #     return Credentials.credentials_list.remove(credential.username)            

        elif option_1 == '5':
            print("\n")
            print("Thank you for your time")
        else:
            print("Sorry wrong input")
    

if __name__ == '__main__':
    main()