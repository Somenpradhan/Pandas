# Write a function to generate a random password with the following conditions:
# - At least 8 characters long but it can also be extended to any character
# - At least one uppercase letter
# - At Least one digit
# - At least one special character like $,*,@,?,#,!,.


# - First code

# import random
# import string

# def generate_password():
#     uppercase_alphabet = string.ascii_uppercase
#     lowercase_alphabet = string.ascii_lowercase
#     digits = string.digits
#     special_characters = "$*@?#!."
#     password = []
#     password.append(random.choice(uppercase_alphabet))
#     password.append(random.choice(lowercase_alphabet))
#     password.append(random.choice(digits))
#     password.append(random.choice(special_characters))
#     remaining_length = 8 - len(password)
#     password.extend(random.choices(uppercase_alphabet + lowercase_alphabet + digits + special_characters, k=remaining_length))
#     random.shuffle(password)
#     return ''.join(password)
# password = generate_password()
# print(password)
        

# Another example
import random

def password(l):
    if l < 8:
        return 
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_chars = "$*@?#!."

    password = [random.choice(upper_case),
                random.choice(lower_case),
                random.choice(digits),
                random.choice(special_chars)]
    
    all_password = upper_case + lower_case + digits + special_chars
    for _ in range(l - 4):
        password.append(random.choice(all_password))
    while password[0] not in upper_case or lower_case:
        random.suffle(password)
    while password[1] not in lower_case or digits:
        random.shuffle(password)
    while password[2] not in digits:
        random.shuffle(password)
    while password[3] not in special_chars:
        random.shuffle(password)
    return ''.join(password)
print(password)