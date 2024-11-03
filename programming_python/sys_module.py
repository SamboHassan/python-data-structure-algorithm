# As mentioned earlier, the sys and os modules form the core of
# much of Python’s system-related tool set.

import sys

# print(sys.platform, sys.maxsize, sys.version)
if sys.platform[:3] == "win":
    print("hello windows")


# If you have code that must act differently on different machines, simply test the
# sys.platform string as done here; although most of Python is cross-platform, nonportable tools are usually wrapped in if tests like the one here. For instance, we’ll see later
# that some program launch and low-level console interaction tools may vary per platform—simply test sys.platform to pick the right tool for the machine on which your
# script is running.


# The sys module also lets us inspect the module search path both interactively and
# within a Python program. sys.path is a list of directory name strings representing the
# true search path in a running Python interpreter.


# print(sys.path)

# sys.modules, for example, is
# a dictionary containing one name:module entry for every module imported in your
# Python session or program
print(list(sys.modules.keys()))


# Also in the interpret hooks category, an object’s reference count is available via
# sys.getrefcount, and the names of modules built-in to the Python executable are listed
# in sys.builtin_module_names. See Python’s library manual for details; these are mostly
# Python internals information, but such hooks can sometimes become important to
# programmers writing tools for other programmers to use.


# -----sys module allow us to fetch all the information related to the
# most recently raised Python exception.

"""
try:
    raise IndexError
except:
    print(sys.exc_info())

"""


# We might use such information to format our own error message to display in a GUI
# pop-up window or HTML web page (recall that by default, uncaught exceptions
# terminate programs with a Python error display).

# >>> import traceback, sys
# >>> def grail(x):
# ... raise TypeError('already got one')
# ...
# >>> try:
# ... grail('arthur')
# ... except:
# ... exc_info = sys.exc_info()
# ... print(exc_info[0])
# ... print(exc_info[1])
# ... traceback.print_tb(exc_info[2])


# • Command-line arguments show up as a list of strings called sys.argv.
# • Standard streams are available as sys.stdin, sys.stdout, and sys.stderr.
# • Program exit can be forced with sys.exit calls.


# Table 2-1. Commonly used os module tools
# Tasks 					Tools
# Shell variables 			os.environ
# Running programs 			os.system, os.popen, os.execv, os.spawnv
# Spawning processes 		os.fork, os.pipe, os.waitpid, os.kill
# Descriptor files, locks 	os.open, os.read, os.write
# File processing 			os.remove, os.rename, os.mkfifo, os.mkdir, os.rmdir
# Administrative tools 		os.getcwd, os.chdir, os.chmod, os.getpid, os.listdir, os.access
# Portability tools 		os.sep, os.pathsep, os.curdir, os.path.split, os.path.join
# Pathname tools 			os.path.exists('path'), os.path.isdir('path'), os.path.getsize('path')
import os

# print(os.getpid())
# >>> os.getpid()
# 7980
# >>> os.getcwd()
# 'C:\\PP4thEd\\Examples\\PP4E\\System'
# >>> os.chdir(r'C:\Users')
# >>> os.getcwd()
# 'C:\\Users'


# >>> os.pathsep, os.sep, os.pardir, os.curdir, os.linesep
# (';', '\\', '..', '.', '\r\n')


# ------------- os.sep
# is whatever character is used to separate directory components on the platform
# on which Python is running; it is automatically preset to \ on Windows, / for POSIX
# machines, and : on some Macs.


# --------------os.pathsep
# provides the character that separates directories on
# directory lists, : for POSIX and ; for DOS and Windows.


# For instance, a call of the form
# dirpath.split(os.sep)
# For instance, a call of the form dir
# path.split(os.sep) will correctly split platform-specific directory names into components, though dirpath may look like dir\dir on Windows, dir/dir on Linux, and
# dir:dir on some Macs.


# -------------------- Common os.path Tools

os.path.isdir(r"C:\Users")
os.path.isfile(r"C:\Users")
# (True, False)

os.path.isdir(r"C:\config.sys")
os.path.isfile(r"C:\config.sys")

os.path.isdir("nonesuch")
os.path.isfile("nonesuch")


os.path.exists(r"c:\Users\Brian")
os.path.exists(r"c:\Users\Default")
os.path.getsize(r"C:\autoexec.bat")


os.path.split(r"C:\temp\data.txt")
# ('C:\\temp', 'data.txt')
os.path.join(r"C:\temp", "output.txt")
# 'C:\\temp\\output.txt'
name = r"C:\temp\data.txt"  # Windows paths
os.path.dirname(name), os.path.basename(name)
# ('C:\\temp', 'data.txt')
name = "/home/lutz/temp/data.txt"  # Unix-style paths
os.path.dirname(name), os.path.basename(name)
# ('/home/lutz/temp', 'data.txt')
os.path.splitext(r"C:\PP4thEd\Examples\PP4E\PyDemos.pyw")
# ('C:\\PP4thEd\\Examples\\PP4E\\PyDemos', '.pyw')


"""
os.path.split separates a filename from its directory path, and os.path.join 
puts them back together—all in entirely portable fashion using the path 
conventions of the machine on which they are called.

"""

os.sep
# '\\'
pathname = r"C:\PP4thEd\Examples\PP4E\PyDemos.pyw"
os.path.split(pathname)  # split file from dir
# ('C:\\PP4thEd\\Examples\\PP4E', 'PyDemos.pyw')
pathname.split(os.sep)  # split on every slash
# ['C:', 'PP4thEd', 'Examples', 'PP4E', 'PyDemos.pyw']
os.sep.join(pathname.split(os.sep))
# 'C:\\PP4thEd\\Examples\\PP4E\\PyDemos.pyw'
os.path.join(*pathname.split(os.sep))
# 'C:PP4thEd\\Examples\\PP4E\\PyDemos.pyw'


The normpath call comes in handy if your paths become a
jumble of Unix and Windows separators:
>>> mixed
'C:\\temp\\public/files/index.html'
>>> os.path.normpath(mixed)
'C:\\temp\\public\\files\\index.html'
>>> print(os.path.normpath(r'C:\temp\\sub\.\file.ext'))
C:\temp\sub\file.ext


# ------------This module also has an abspath call that portably 
# returns the full directory pathname
# of a file;

>>> os.chdir(r'C:\Users')
>>> os.getcwd()
'C:\\Users'
>>> os.path.abspath('') # empty string means the cwd
'C:\\Users'
>>> os.path.abspath('temp') # expand to full pathname in cwd
'C:\\Users\\temp'
>>> os.path.abspath(r'PP4E\dev') # partial paths relative to cwd
'C:\\Users\\PP4E\\dev'
>>> os.path.abspath('.') # relative path syntax expanded
'C:\\Users'
>>> os.path.abspath('..')
'C:\\'
>>> os.path.abspath(r'..\examples')
'C:\\examples'



>>> os.path.abspath(r'C:\PP4thEd\chapters') # absolute paths unchanged
'C:\\PP4thEd\\chapters'
>>> os.path.abspath(r'C:\temp\spam.txt')
'C:\\temp\\spam.txt'



# ---------------- Running Shell Commands from Python Scripts

"""
os.system
Runs a shell command from a Python script
os.popen
Runs a shell command and connects to its input or output streams
"""

# But because the
# os module’s system and popen calls let Python scripts run any sort of command that the
# underlying system shell understands, our scripts can make use of every command-line
# tool available on the computer, whether it’s coded in Python or not.


C:\...\PP4E\System> python
>>> import os
>>> os.system('dir /B')
helloshell.py
more.py
more.pyc
spam.txt
__init__.py
0
>>> os.system('type helloshell.py')
# a Python program
print('The Meaning of Life')
0

>>> os.system('type hellshell.py')
The system cannot find the file specified.
1




# The os.system call simply runs a shell command line, but os.popen also connects 
# to the standard input or output streams of the command; we get back a 
# file-like object connected to the command’s output by default 
# (if we pass a w mode flag to popen, we connect to the command’s input stream instead).


>>> open('helloshell.py').read()
"# a Python program\nprint('The Meaning of Life')\n"
>>> text = os.popen('type helloshell.py').read()
>>> text
"# a Python program\nprint('The Meaning of Life')\n"
>>> listing = os.popen('dir /B').readlines()
>>> listing
['helloshell.py\n', 'more.py\n', 'more.pyc\n', 'spam.txt\n', '__init__.py\n']


>>> os.system('python helloshell.py') # run a Python program
The Meaning of Life
0
>>> output = os.popen('python helloshell.py').read()
>>> output
'The Meaning of Life\n'

# The 0s at the end of the first two commands here are just the return values of 
# the system call itself (its exit status; zero generally means success).


# ---------- The subprocess module alternativeThe subprocess module alternative

# the subprocess module can achieve the same effect as os.system and os.popen; 
# it generally requires extra code but gives more control over how streams 
# are connected and used. 

>>> import subprocess
>>> subprocess.call('python helloshell.py') # roughly like os.system()
The Meaning of Life
0
>>> subprocess.call('cmd /C "type helloshell.py"') # built-in shell cmd
# a Python program
print('The Meaning of Life')
0
>>> subprocess.call('type helloshell.py', shell=True) # alternative for built-ins
# a Python program
print('The Meaning of Life')
0

# On Windows, we need to pass a shell=True argument to subprocess tools like
# call and Popen (shown ahead) in order to run commands built into the shell. 


os.startfile("webpage.html") # open file in your web browser
os.startfile("document.doc") # open file in Microsoft Word
os.startfile("myscript.py") # run file with Python

"""

The os module’s system and popen calls, as well as the subprocess module, fall under 
the category of 
* program launchers, 
* stream redirectors, and 
* cross-process communication devices


Among the os module’s other weapons are these:
os.environ: Fetches and sets shell environment variables
os.fork: Spawns a new child process on Unix-like systems
os.pipe: Communicates between programs
os.execlp: Starts new programs
os.pipe: Communicates between programs
os.execlp: Starts new programs
os.spawnv: Starts new programs with lower-level control
os.open: Opens a low-level descriptor-based file
os.mkdir: Creates a new directory
os.remove
Deletes a file by its pathname
os.walk
Applies a function or loop body to all parts of an entire directory tree
"""


