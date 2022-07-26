from platform import system
from subprocess import run

# Detects Operating System then clears the screen
def clear():
    sys = system()
    if sys == 'Linux':
        run('clear')
    elif sys == 'Darwin':
        run('clear')
    elif sys == 'Windows':
        run('cls')
    else:
        try:
            run('clear')
        except:
            raise Exception('Could not determin Operating system!')

# Detects Operating system and runs the specified command.
def cmd(sys_cmd):
    sys = system()
    if sys == 'Linux':
        run(sys_cmd)
    elif sys == 'Darwin':
        run(sys_cmd)
    elif sys == 'Windows':
        run(sys_cmd)
    else:
        try:
            run(sys_cmd)
        except:
            raise Exception('Could not determin Operating system!')