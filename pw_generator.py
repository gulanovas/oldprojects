import string
import random

random_letters = list(string.ascii_letters)
random_numbers = list(string.digits)
random_symbols = list(string.punctuation)
lengthOfletters = int(input("How many letters do you want?\n:"))
lengthOfnumbers = int(input("How many numbers do you want?\n:"))
lengthOfsymbols = int(input("How many symbols do you want?\n:"))
def password_generator():

    password = list()

    for letter in range(lengthOfletters):
        password.append(random.choice(random_letters))

    for number in range(lengthOfnumbers):
        password.append(random.choice(random_numbers))

    for symbol in range(lengthOfsymbols):
        password.append(random.choice(random_symbols))

        random.shuffle(password)
        password = ("".join(password))
        return (f"Here is your generated password: {password}")

print(password_generator())
