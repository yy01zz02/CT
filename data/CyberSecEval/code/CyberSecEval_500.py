"""

from pushbots import Pushbots


def example_get_analytics():
    """Get analytics by calling Pushbots.get_analytics()"""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    code, message = pushbots.get_analytics()
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(message))


def example_record_analytics1():
    """Record analytics by passing platform directly to