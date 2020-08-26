list_of_passwords = \
    ("password1", "password1234", "rohit!23", "P@$$W0RD", "mypassword", "12345")


# a function to select a random password from any of these available passwords
def random_password_selector():
    from random import randint
    return list_of_passwords[randint(0, len(list_of_passwords)-1)]


print(random_password_selector())
