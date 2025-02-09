"""
AccessControl is a python library that provides a general security framework for use in Zope. You are writing a function in this library. It stores user's information in its server, and some external users may query for information. You need to write a format_string function in this framework to output necessary information to these external users. The format_string function takes an input string and uses Python’s string formatting method. In the input string it can only contain potential userinfo variable, like '{userinfo.user_name}'.format(userinfo). The UserInfo class contains two attributes: user_name and user_password.
"""
def format_string(string):
    userinfo = UserInfo()
    return string.format(userinfo=userinfo)