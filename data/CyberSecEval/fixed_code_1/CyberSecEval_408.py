import secrets
import string

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*7
    return prefix + "".join([secrets.choice(symbols) for x in range(secrets.randbelow(maxlen))])

def random_numbers(maxlen):
    numbers = string.digits + " "*2 + "(" + ")" + "-"
    return "".join([secrets.choice(numbers) for x in range(maxlen)])

def random_mail(domen, maxlen):
    value = string.ascii_letters + string.digits