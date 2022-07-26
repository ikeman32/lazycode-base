# lazycode

This is a personal library I decided to publish in case others find it useful. It's still very much a work in progress and is mostly experimental. I made it in order to save me a few key strokes while coding in python.

## importing library

prefered method: from lazycode.libName import function

## shell library: platform independent

**clear**
Clears the console screen, detects OS and outputs the commandline equivelant for that OS. For example, windows command prompt command is cls and Linux is ls.

usage:
clear()

**cmd**
This is intended to send all or most of the commandline commands to the system but only partially works.

working example: cmd('cls') or cmd('ls -a')

failing example: cmd('echo Echo this > output.txt)

**ldir**
Literally list directory, detects OS and outputs to the system commandline for the detected OS. The result is a list of all the visible files and directories.

usage: 
ldir()

**hdir** 
Same as ldir except is shows hidden files and directories as well.

usage:
hdir()

**reboot**
Reboots the computer. This works on Linux and should work on Windows. I am unable to test this on a Mac OS as I do not have a Mac and unable to find a VM.

## nix library for Linux only

**These commands are the same as the shell library except the only work in Linux**
commands:
-clear
-cmd
-ldir
-hdir
-reboot

**mkdir**
Linux command to make a directory.

usage: mkdir('dir_name')

## pythonfunctions
Some python helper functions.

**fprint**
This is my feeble attempt to use f Strings in a print function: print(f'Age: {age}'). It is limited to six arguments for now.

usage:
fprint('Age:', age)
This is the same as: print(f'Age: {age}') but without the need to include a space as that space is inserted by the fprint function.

**lprint**
This excepts numbered argument of 1 or 2 and any numer of other arguments and prints the result in a human readable list:

usage:
lprint(1, 1, 2, 3)

output:
1
2
3

lprint(2, 'Name:', 'John', 'Age:', 25, 'Married:', 'Yes')

output:
Name: John
Age: 25
Married: Yes

**wait**
This makes use of the time.sleep function.

usage: wait(10)'''waits 10 seconds'''

**start_time, stop_time, elapse_time**
An implementation of the time.per_counter.

usage:

start = start_time()
some_function()
stop = stop_time()
elapse_time(start, stop)

output:
Time elapse is: N seconds.
