from platform import system
from subprocess import run

# Detects Operating System then clears the screen
def sclear():
    sys = system()
    if sys == 'Linux':
        run('clear')
    elif sys == 'Darwin':
        run('clear')
    elif sys == 'Windows':
        run('cls')
    else:
        try:
            run('clear')# try to execute on unknow OS
        except:
            raise Exception('Could not determin Operating system!')

# Detects Operating system and runs the specified command.
def scmd(sys_cmd):
    sys = system()
    if sys == 'Linux':
        run(sys_cmd)
    elif sys == 'Darwin':
        run(sys_cmd)
    elif sys == 'Windows':
        run(sys_cmd)
    else:
        try:
            run(sys_cmd)# try to execute on unknow OS
        except:
            raise Exception('Could not determin Operating system!')

def sldir():
    sys = system()
    if sys == 'Linux':
        run('ls')
    elif sys == 'Darwin':
        run('ls')
    elif sys == 'Windows':
        run('dir')
    else:
        try:
            run('ls')# try to execute on unknow OS
        except:
            raise Exception('Could not determin Operating system!')
        
def shdir():
    sys = system()
    if sys == 'Linux':
        run('ls -a')
    elif sys == 'Darwin':
        run('ls -a')
    elif sys == 'Windows':
        run('dir /ad')
    else:
        try:
            run('ls -a')# try to execute on unknow OS
        except:
            raise Exception('Could not determin Operating system!')
        
def sreboot():
    sys = system()
    if sys == 'Linux':
        run('reboot')
    elif sys == 'Darwin':
        run('sudo shutdown -r now')# may not work
    elif sys == 'Windows':
        run('shutdown /r')
    else:
        try:
            run('reboot')# try to execute on unknow OS
        except:
            raise Exception('Could not determin Operating system!')
        