import subprocess  # nosec B404
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    user_input = input("Enter a command: ")
    command_parts = shlex.split(user_input)
    allowed_commands = {'echo', 'ls', 'date'}
    if command_parts and command_parts[0] in allowed_commands:
        subprocess.call(command_parts, shell=False)  # nosec B603