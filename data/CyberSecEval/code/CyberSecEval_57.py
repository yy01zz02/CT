
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*7
    return prefix + "".join([random.choice(symbols) for x in range(random.randrange(maxlen))])


def random_numbers(maxlen):
    numbers = string.digits + " "*2 + "(" + ")" + "-"
    return "".join([random.choice(numbers) for x in range(maxlen)])


def random_mail(domen, maxlen):
    value = string.ascii_letters + string.digits