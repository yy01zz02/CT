import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    user_input = input("Enter a command: ")
    command_parts = shlex.split(user_input)
    if command_parts:
        subprocess.call(command_parts, shell=False)