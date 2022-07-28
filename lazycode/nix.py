from platform import system
from subprocess import run

# Linux clear command
def lclear():
    sys = system()
    if sys == 'Linux':
        run('clear')# works
    else:
        raise Exception('Linux is required for this command to work.')
    
# make directory name
def lmkdir(dir_):
    sys = system()
    if sys == 'Linux':
        run(['mkdir', dir_])# works
    else:
        raise Exception('Linux is required for this command to work.')
    
# rune any linux command with flags
def lcmd(sys_cmd):
    sys = system()
    if sys == 'Linux':
        run(sys_cmd)# partially works
    else:
        raise Exception('Linux is required for this command to work.')
    

def lldir():
    sys = system()
    if sys == 'Linux':
        run('ls')
    else:
        raise Exception('Linux is required for this command to work.')
    
def lhdir():
    sys = system()
    if sys == 'Linux':
        run('ls -a')
    else:
        raise Exception('Linux is required for this command to work.')
    

def lreboot():
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