from platform import system
from subprocess import run

# simple ls command to list files and directories in Linux
def ls():
    sys = system()
    if sys == 'Linux':
        run('ls')# works
    else:
        raise Exception('Linux is required for this command to work.')
    
# Linux clear command
def clear():
    sys = system()
    if sys == 'Linux':
        run('clear')# works
    else:
        raise Exception('Linux is required for this command to work.')
    
# make directory name
def mkdir(dir_):
    sys = system()
    if sys == 'Linux':
        run(['mkdir', dir_])# works
    else:
        raise Exception('Linux is required for this command to work.')
    
# rune any linux command with flags
def cmd(sys_cmd):
    sys = system()
    if sys == 'Linux':
        run(sys_cmd)# partially works
    else:
        raise Exception('Linux is required for this command to work.')
    

def ldir():
    sys = system()
    if sys == 'Linux':
        run('ls')
    else:
        raise Exception('Linux is required for this command to work.')
    
def hdir():
    sys = system()
    if sys == 'Linux':
        run('ls -a')
    else:
        raise Exception('Linux is required for this command to work.')
    

def reboot():
    sys = system()
    if sys == 'Linux':
        run('reboot')
    else:
        raise Exception('Linux is required for this command to work.')
    



'''The following 4 functions do not work at this times'''
# output text to a file
# def txt_tofile(txt, file_name):
#     sys = system()
#     if sys == 'Linux':
#         run(''.join(['echo ', txt, ' > ', file_name]))# not working
#     else:
#         raise Exception('Linux is required for this command to work.')
    
# # append text to a file
# def ap_txt_tofile(txt, file_name, ext = 'txt'):
#     sys = system()
#     if sys == 'Linux':
#         run(f'echo {txt} >> {file_name}.{ext}')
#     else:
#         raise Exception('Linux is required for this command to work.')
    
# # send a commands output to a file
# def out_tofile(cmd, file_name, ext = 'txt'):
#     sys = system()
#     if sys == 'Linux':
#         run(f'{cmd} > {file_name}.{ext}')
#     else:
#         raise Exception('Linux is required for this command to work.')

# # append a commands output to a file
# def ap_tofile(cmd, file_name, ext = 'txt'):
#     sys = system()
#     if sys == 'Linux':
#         run(f'{cmd} >> {file_name}.{ext}')
#     else:
#         raise Exception('Linux is required for this command to work.')