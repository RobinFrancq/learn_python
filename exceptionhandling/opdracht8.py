# Maken van custom exception
class Error(Exception):
    pass
class PasswordNotLongEnoughError(Error):
    pass

try:
    pas = raw_input("Enter a password (8 chars minimun): ")
    if len(pas) < 8:
        raise PasswordNotLongEnoughError
    print("Password OK")
except PasswordNotLongEnoughError:
    print("Password is not long enough")