import re


def email_validator(email):
    return bool(re.search(r'[^@]+@[^@]+\.[^@]+', email))


def write_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
        file.close()
