In Python, you can use an expression as a statement, too—that is, on a line by itself.
But because the result of the expression won’t be saved, it usually makes sense to do
so only if the expression does something useful as a side effect. 


Table 11-4. Common Python expression statements
Operation Interpretation
spam(eggs, ham) Function calls
spam.ham(eggs) Method calls
spam Printing variables in the interactive interpreter
print(a, b, c, sep='') Printing operations in Python 3.X
yield x ** 2 Yielding expression statements

For instance, though you normally run a 3.X print call on a line by itself as an expression
statement, it returns a value like any other function call (its return value is None, the
default return value for functions that don’t return anything meaningful):
>>> x = print('spam') # print is a function call expression in 3.X
spam
>>> print(x) # But it is coded as an expression statement
None


>>> L = [1, 2]
>>> L.append(3) # Append is an in-place change
>>> L
[1, 2, 3]
However, it’s not unusual for Python newcomers to code such an operation as an assignment statement instead, intending to assign L to the larger list:
>>> L = L.append(4) # But append returns None, not L
>>> print(L) # So we lose our list!
None


------------------PRINT EXPRESSION statements

• sep is a string inserted between each object’s text, which defaults to a single space
if not passed; passing an empty string suppresses separators altogether.
• end is a string added at the end of the printed text, which defaults to a \n newline
character if not passed. Passing an empty string avoids dropping down to the next
output line at the end of the printed text—the next print will keep adding to the
end of the current output line.
• file specifies the file, standard stream, or other file-like object to which the text
will be sent; it defaults to the sys.stdout standard output stream if not passed. Any
object with a file-like write(string) method may be passed, but real files should
be already opened for output.


• flush, added in 3.3, defaults to False. It allows prints to mandate that their text be
flushed through the output stream immediately to any waiting recipients. Normally, whether printed output is buffered in memory or not is determined by
file; passing a true value to flush forcibly flushes the stream.


>>> print(x, y, z, sep='') # Suppress separator
spam99['eggs']
>>>
>>> print(x, y, z, sep=', ') # Custom separator
spam, 99, ['eggs']



>>> print(x, y, z, end='') # Suppress line break
spam 99 ['eggs']>>>
>>>
>>> print(x, y, z, end=''); print(x, y, z) # Two prints, same output line
spam 99 ['eggs']spam 99 ['eggs']
>>> print(x, y, z, end='...\n') # Custom line end
spam 99 ['eggs']...
>>>


>>> print(x, y, z, sep='...', end='!\n') # Multiple keywords
spam...99...['eggs']!
>>> print(x, y, z, end='!\n', sep='...') # Order doesn't matter
spam...99...['eggs']!


>>> print(x, y, z, sep='...', file=open('data.txt', 'w')) # Print to a file
>>> print(x, y, z) # Back to stdout
spam 99 ['eggs']
>>> print(open('data.txt').read()) # Display file text
spam...99...['eggs']



>>> text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
>>> print(text)
Result: 3.1416, 00042
>>> print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))
Result: 3.1416, 00042



Test Your Knowledge: Answers
1. You can use multiple-target assignments (A = B = C = 0), sequence assignment
(A, B, C = 0, 0, 0), or multiple assignment statements on three separate lines (A
= 0, B = 0, and C = 0). With the latter technique, as introduced in Chapter 10, you
can also string the three separate statements together on the same line by separating
them with semicolons (A = 0; B = 0; C = 0).
2. If you assign them this way:
A = B = C = []



all three names reference the same object, so changing it in place from one (e.g.,
A.append(99)) will affect the others. This is true only for in-place changes to mutable objects like lists and dictionaries; for immutable objects such as numbers and
strings, this issue is irrelevant.
3. The list sort method is like append in that it makes an in-place change to the subject
list—it returns None, not the list it changes. The assignment back to L sets L to
None, not to the sorted list. As discussed both earlier and later in this book (e.g.,
Chapter 8), a newer built-in function, sorted, sorts any sequence and returns a new
list with the sorting result; because this is not an in-place change, its result can be
meaningfully assigned to a name.


4. To print to a file for a single print operation, you can use 3.X’s print(X, file=F)
call form, use 2.X’s extended print >> file, X statement form, or assign
sys.stdout to a manually opened file before the print and restore the original after.
You can also redirect all of a program’s printed text to a file with special syntax in
the system shell, but this is outside Python’s scope.



