import re


def email_validator(email):
    return bool(re.search(r'[^@]+@[^@]+\.[^@]+', email))


def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
        file.close()
