#!/bin/python3.6.9
import random
import user

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '`#^*&$|<>}+@!~'
length = input('password length?')
length = int(length)
combined_pass = chars + digits + symbols

password = ''
for i in range(length):
    password += random.choice(combined_pass)
print(password)