"""
The language’s two main looping constructs—statements that repeat an action over and
over. The first of these, the while statement, provides a way to code general loops. 
The second, the for statement, is designed for stepping through the items in a 
sequence or other iterable object and running a block of code for each.

"""


In simple terms, it repeatedly executes a block of (normally indented) statements as long
as a test at the top keeps evaluating to a true value. It is called a “loop” because control
keeps looping back to the start of the statement until the test becomes false. When the
test becomes false, control passes to the statement that follows the while block. The
net effect is that the loop’s body is executed repeatedly while the test at the top is true.
If the test is false to begin with, the body never runs and the while statement is skipped.


----------------------  General Format

while test: # Loop test
 	statements # Loop body
else: # Optional else
 	statements # Run if didn't exit loop with break


>>> while True:
... print('Type Ctrl-C to stop me!')


>>> x = 'spam'
>>> while x: # While x is not empty
... print(x, end=' ') # In 2.X use print x,
... x = x[1:] # Strip first character off x
...
spam pam am m


# The following code counts from the value of a up to, but not including, b.
>>> a=0; b=10
>>> while a < b: # One way to code counter loops
... print(a, end=' ')
... a += 1 # Or, a = a + 1






