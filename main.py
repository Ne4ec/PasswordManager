#!/bin/python3

import sys
import random
import time

from animation import logo

print(40 * '-')
print(f"| {logo} ")
print(40 * '-')

def new_line():
    return 40*'_'

def password_generator(length=15): #*default value, the user could change it
    ascii_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!§$@€%&/'#*<>"
    password = []
    for _ in range(length):
        password.append(random.choice(ascii_characters))
    
    return ''.join(password)

user_input = sys.argv

if __name__ == "__main__":
    if (len(user_input) < 2 or user_input[1] == "-h"):
        print(r"""
SYNOPSIS 
    ./main [ARGUMENT]

    [ARGUMENT]
        -a  all
                show the entire list
        -c  create
                create an new Password
        -h  help
                get more help

DESCRPTIONS
    A Password manager, which store a name and a password.

IMPORTANT
    Don't use it as a password manager. It's a hobby project, not a professional one. 
    Passwords are not encrypted at all. Please use a secure, trusted application instead.

AUTHORS
        Created by Ne4ec. More information on the official Githubsite:
        - https://github.com/Ne4ec/PasswordManager/README.me
        """) 
    elif user_input[1] == "-c":
        title_of_new_password = input("What is the title:\n")
        print(f"You password is creating, for {title_of_new_password} ...")
        generated_password = password_generator()
        time.sleep(1.5)
        finished_password = f"{title_of_new_password} | {generated_password}"
        print(f"| {finished_password} |") # Output: "created name" | "password" 
        password_storage_file = open("password_storage.py", 'a')
        password_storage_file.write(f"\n| {finished_password} |")
        password_storage_file.close()
    elif user_input[1] == "-a":
        password_storage_file = open("password_storage.py", 'r')
        print(password_storage_file.read())
        password_storage_file.close()
    else:
        print("Invalid argument. Use '-h' to see the correct usage.")



#* 12 is the default value, its the length of the password
