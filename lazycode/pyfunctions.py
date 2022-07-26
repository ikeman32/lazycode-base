from time import sleep, perf_counter


def fprint(*args):
    if len(args) > 6:
        raise Exception('Too many args')
    
    if len(args) == 1:
        print(f'{args[0]}')
    elif len(args) == 2:
        print(f'{args[0]} {args[1]}')
    elif len(args) == 3:
        print(f'{args[0]} {args[1]} {args[2]}')
    elif len(args) == 4:
        print(f'{args[0]} {args[1]} {args[2]} {args[3]}')
    elif len(args) == 5:
        print(f'{args[0]} {args[1]} {args[2]} {args[3]} {args[4]}')
    elif len(args) == 6:
        print(f'{args[0]} {args[1]} {args[2]} {args[3]} {args[4]} {args[5]}')
        
# outputs print items one line at at time
def lprint(n, *args):
    if n == 1:
        for i in args:
            print(i)
    if n == 2:
        for i in range(0,len(args),2):
            print(f'{args[i]} {args[i + 1]}')
            
def wait(t):
    sleep(t)
    
def start_time():
    t = perf_counter()
    return t

def stop_time():
    t = perf_counter()
    return t

def elapse_time(start, stop):
    print(f'Time elapse is: {stop - start} seconds.')
    
# def for_r(range_, args):
#     for i in range(0, range_):
#         args

