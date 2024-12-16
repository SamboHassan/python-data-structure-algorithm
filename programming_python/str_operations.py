"""
In Python 3.X there are three string types:

str is used for Unicode text (including ASCII), 
bytes is used for binary data (including encoded text), and 
bytearray is a mutable variant of bytes. 

Files work in two modes: text, which represents content as str and implements Unicode 
encodings, and binary, which deals in raw bytes and does no data translation.

"""


"""
Once text is in memory, it’s a Python string of characters that supports all the basics we’ll study in this chapter. In fact, the primary
distinction of Unicode often lies in the translation (a.k.a. encoding) step required to
move it to and from files. Beyond that, it’s largely just string processing.

"""

String Basics
From a functional perspective, strings can be used to represent just about anything that
can be encoded as text or bytes. In the text department, this includes symbols and
words (e.g., your name), contents of text files loaded into memory, Internet addresses,
Python source code, and so on. Strings can also be used to hold the raw bytes used for
media files and network transfers, and both the encoded and decoded forms of nonASCII
Unicode text used in internationalized programs.




For processing,
strings support expression operations such as concatenation 
(combining strings), slicing (extracting sections), indexing (fetching by offset), 
and so on


Operation Interpretation
S = '' Empty string
S = "spam's" Double quotes, same as single
S = 's\np\ta\x00m' Escape sequences
S = """...multiline...""" Triple-quoted block strings
S = r'\temp\spam' Raw strings (no escapes)
B = b'sp\xc4m' Byte strings in 2.6, 2.7, and 3.X (Chapter 4, Chapter 37)
U = u'sp\u00c4m' Unicode strings in 2.X and 3.3+ (Chapter 4, Chapter 37)
S1 + S2
S * 3
Concatenate, repeat
S[i]
S[i:j]
len(S)
Index, slice, length
"a %s parrot" % kind String formatting expression
"a {0} parrot".format(kind) String formatting method in 2.6, 2.7, and 3.X
S.find('pa')
S.rstrip()
S.replace('pa', 'xx')
S.split(',')
String methods (see ahead for all 43): search,
S.find('pa')
S.rstrip()
S.replace('pa', 'xx')
S.split(',')
String methods (see ahead for all 43): search,
remove whitespace,
replacement,
split on delimiter,

Operation Interpretation
S.isdigit()
S.lower()
S.endswith('spam')
'spam'.join(strlist)
S.encode('latin-1')
B.decode('utf8')
content test,
case conversion,
end test,
delimiter join,
Unicode encoding,
Unicode decoding, etc. (see Table 7-3)
for x in S: print(x)
'spam' in S
[c * 2 for c in S]
map(ord, S)
Iteration, membership


[c * 2 for c in S]
map(ord, S)
re.match('sp(.*)am', line) Pattern matching: library module






Table 7-2. String backslash characters
Escape Meaning
\newline Ignored (continuation line)
\\ Backslash (stores one \)
\' Single quote (stores ')
\" Double quote (stores ")
\a Bell
\b Backspace
\f Formfeed
\n Newline (linefeed)
\r Carriage return
\t Horizontal tab
\v Vertical tab
\xhh Character with hex value hh (exactly 2 digits)
\ooo Character with octal value ooo (up to 3 digits)
\0 Null: binary 0 character (doesn’t end string)
\N{ id } Unicode database ID
\uhhhh Unicode character with 16-bit hex value
\Uhhhhhhhh Unicode character with 32-bit hex valuea
\other Not an escape (keeps both \ and other)




myfile = open('C:\new\text.dat', 'w')
myfile = open(r'C:\new\text.dat', 'w') # Raw string turns off the escape mechanism.

# letter r can be (uppercase or lowercase) 
# This is just the sort of thing that raw strings are useful for.

# OR you can keep your backslashes by simply doubling them up:
myfile = open('C:\\new\\text.dat', 'w')


"""
Offsets and slices: positive offsets start from the left end (offset 0 is the first 
item), and negatives count back from the right end (offset −1 is the last item). 
Either kind of offset can be used to give positions in indexing and slicing 
operations.

Slicing (S[i:j]) extracts contiguous sections of sequences:
• The upper bound is noninclusive.
• Slice boundaries default to 0 and the sequence length, if omitted.
• S[1:3] fetches items at offsets 1 up to but not including 3.
• S[1:] fetches items at offset 1 through the end (the sequence length).
• S[:3] fetches items at offset 0 up to but not including 3.
• S[:−1] fetches items at offset 0 up to but not including the last item.
• S[:] fetches items at offsets 0 through the end—making a top-level copy of S.
Extended slicing (S[i:j:k]) accepts a step (or stride) k, which defaults to +1:
• Allows for skipping items and reversing order—see the next section


"""

# The left offset is taken to be the lower bound (inclusive), and the right is the 
# upper bound (noninclusive). That is, Python fetches all items from the lower 
# bound up to but not including the upper bound, and returns a new object 
# containing the fetched items.

# S[:−1] fetches all but the last item—the lower bound
# defaults to 0, and −1 refers to the last item, noninclusive.

