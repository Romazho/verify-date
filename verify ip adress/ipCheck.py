import re


def verify_ip(ipAdress):

    match = re.match(
        '(^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$)', ipAdress)

    if match == None:
        return False

    return True


print(verify_ip('127.0.0.1'))
