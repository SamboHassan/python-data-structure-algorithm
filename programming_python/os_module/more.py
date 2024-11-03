"""
split and interactively page a string or file of text

"""


def more(text, numlines=15):
    lines = text.splitlines()  # like split('\n') but no '' at end

    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input("More?") not in ["y", "Y"]:
            break


if __name__ == "__main__":
    import sys  # when run, not imported

    more(open(sys.argv[1]).read(), 10)  # page contents of file on cmdline


# They instrument the file to be
# used in either of two ways—as a script or as a library.

# Recall that every Python module has a built-in __name__ variable that Python sets to the
# __main__ string only when the file is run as a program, not when it’s imported as a
# library. Because of that, the more function in this file is executed automatically by the
# last line in the file when this script is run as a top-level program, but not when it is
# imported elsewhere. This simple trick turns out to be one key to writing reusable script
# code: by coding program logic as functions rather than as top-level code, you can also
# import and reuse it in other scripts.


# The splitlines string object method call that this script employs returns a list of substrings split at line ends (e.g., ["line", "line",...]). An alternative splitlines method
# does similar work, but retains an empty line at the end of the result if the last line is
# \n terminated:
# >>> line = 'aaa\nbbb\nccc\n'
# >>> line.split('\n')
# ['aaa', 'bbb', 'ccc', '']
# >>> line.splitlines()
# ['aaa', 'bbb', 'ccc']


# >>> mystr = 'xxxSPAMxxx'
# >>> mystr.find('SPAM') # return first offset
# 3
# >>> mystr = 'xxaaxxaa'
# >>> mystr.replace('aa', 'SPAM') # global replacement
# 'xxSPAMxxSPAM'



# >>> mystr = 'xxxSPAMxxx'
# >>> 'SPAM' in mystr # substring search/test
# True
# >>> 'Ni' in mystr # when not found
# False
# >>> mystr.find('Ni')
# -1
# >>> mystr = '\t Ni\n'
# >>> mystr.strip() # remove whitespace
# 'Ni'
# >>> mystr.rstrip() # same, but just on right side
# '\t Ni'


# >>> mystr = 'SHRUBBERY'
# >>> mystr.lower() # case converters
# 'shrubbery'
# >>> mystr.isalpha() # content tests
# True
# >>> mystr.isdigit()
# False
# >>> import string # case presets: for 'in', etc.
# >>> string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'


# >>> string.whitespace # whitespace characters
# ' \t\n\r\x0b\x0c'
# >>> mystr = 'aaa,bbb,ccc'
# >>> mystr.split(',') # split into substrings list
# ['aaa', 'bbb', 'ccc']
# >>> mystr = 'a b\nc\nd'
# >>> mystr.split() # default delimiter: whitespace
# ['a', 'b', 'c', 'd']
# >>> delim = 'NI'
# >>> delim.join(['aaa', 'bbb', 'ccc']) # join substrings list
# 'aaaNIbbbNIccc'
# >>> ' '.join(['A', 'dead', 'parrot']) # add a space between
# 'A dead parrot'
# >>> chars = list('Lorreta') # convert to characters list
# >>> chars
# ['L', 'o', 'r', 'r', 'e', 't', 'a']
# >>> chars.append('!')
# >>> ''.join(chars) # to string: empty delimiter
# 'Lorreta!'


# >>> mystr = 'xxaaxxaa'
# >>> 'SPAM'.join(mystr.split('aa')) # str.replace, the hard way!
# 'xxSPAMxxSPAM'
# For future reference, also keep in mind that Python doesn’t automatically convert
# strings to numbers, or vice versa; if you want to use one as you would use the other,
# you must say so with manual conversions:
# >>> int("42"), eval("42") # string to int conversions
# (42, 42)
# >>> str(42), repr(42) # int to string conversions
# ('42', '42')
# >>> ("%d" % 42)


>>> "42" + str(1), int("42") + 1 # concatenation, addition
('421', 43)
3.X has two additional string types that support most str string operations: bytes—a sequence of short integers for representing 8-bit binary data, and
bytearray—a mutable variant of bytes.3.X has two additional string types that support most str string operations: bytes—a sequence of short integers for representing 8-bit binary data, and
bytearray—a mutable variant of bytes.


# ---------------- File Operation Basics
open('file').read() # read entire file into string
open('file').read(N) # read next N bytes into string
open('file').readlines() # read entire file into line strings list
open('file').readline() # read next line, through '\n'
