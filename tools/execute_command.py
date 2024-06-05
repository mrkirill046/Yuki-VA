# Imports
from tools.command_config import commands_config


# Method
def execute_command_with_intent(command: str, *args: list):
    if command in commands_config:
        commands_config[command](*args)
    else:
        print('ERROR: Command not found')
