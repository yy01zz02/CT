
    return min_length, max_length


def get_value_in(min_length, max_length, padding=0, required_length=0):
    return random.randint(
        *get_range_endpoints(min_length, max_length, padding, required_length))


def random_string(length, chars=ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))


_last_position_hint = -1
_next_position_hint = itertools.count()


class TypeMeta(type):

    """