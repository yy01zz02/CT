

def add_coaches():
    """
    Adds two coaches (for testing)
    """
    user_1 = models.User(
        id='ecf1bcae-9c8f-11e5-b5b4-d895b95699bb',
        fullname='Pat Blargstone',
        username='pat',
        password=hashlib.md5('secret').hexdigest())
    coach_1 = models.Coach(
        id='ee8d1d30-9c8f-11e5-89d4-d895b95699bb',
        user_id=user_1.id)
    user_2 = models.User(
        id='ef2a95b0-9c8f-11e5-bd27-d895b95699bb',
        fullname='Sandy Blargwright',
        username='sandy',
        password=hashlib.md5('secret').hexdigest())
    coach_2 = models.Coach(