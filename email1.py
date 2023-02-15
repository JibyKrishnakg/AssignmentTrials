import re
print("This is the email_checker.py file")
print("Python thinks this is called {}".format(__name__))


def is_email(s):
    x = r'[a-zA-Z0-9]+[\.]?[\-]?[\_]?[a-z0-9]+@[a-zA-Z0-9]+[\-]?[a-zA-Z0-9]+.[a-zA-Z]{2}'
    if re.match(x, s):
        return True
    else:
        return False


if __name__ == '__main__':
    is_email(email)
