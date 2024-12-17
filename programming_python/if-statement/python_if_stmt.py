Python if statement which is the main statement used for selecting from alternative
actions based on test results.

Because this is our first in-depth
look at compound statements—statements that embed other statements



-------- General Format
The Python if statement is typical of if statements in most procedural languages. 
It takes the form of an if test, followed by one or more optional elif (“else if”) 
tests and a final optional else block.


if test1: # if test
 	statements1 # Associated block
elif test2: # Optional elifs
 	statements2
else: # Optional else
 	statements3


>>> if 1:
... print('true')
...
true


To handle a false result, code the else:
>>> if not 1:
... 	print('true')
... else:
... 	print('false')
...
false


-------------- Multiway Branching

Now here’s an example of a more complex if statement, with all its optional parts
present:

>>> x = 'killer rabbit'
>>> if x == 'roger':
... 	print("shave and a haircut")
... elif x == 'bugs':
... 	print("what's up doc?")
... else:
... 	print('Run away! Run away!')
...
Run away! Run away!


There is no switch or case statement in Python that selects an action based on a variable’s
value. Instead, you usually code multiway branching as a series of if/elif tests, as in
the prior example, and occasionally by indexing dictionaries or searching lists.



>>> choice = 'ham'
>>> print({'spam': 1.25, # A dictionary-based 'switch'
... 'ham': 1.99, # Use has_key or get for default
... 'eggs': 0.99,
... 'bacon': 1.10}[choice])
1.99


>>> if choice == 'spam': # The equivalent if statement
... print(1.25)
... elif choice == 'ham':
... print(1.99)
... elif choice == 'eggs':
... print(0.99)
... elif choice == 'bacon':
... print(1.10)
... else:
... print('Bad choice')
...
1.99


------------------Handling switch defaults

>>> branch = {'spam': 1.25,
... 'ham': 1.99,
... 'eggs': 0.99}
>>> print(branch.get('spam', 'Bad choice'))
1.25



>>> print(branch.get('bacon', 'Bad choice'))
Bad choice
An in membership test in an if statement can have the same default effect:
>>> choice = 'bacon'
>>> if choice in branch:
... print(branch[choice])
... else:
... print('Bad choice')
...
Bad choice



>>> try:
... print(branch[choice])
... except KeyError:
... print('Bad choice')
...
Bad choice

-------------------- Handling larger actions
def function(): ...
def default(): ...
branch = {'spam': lambda: ..., # A table of callable function objects
 'ham': function,
 'eggs': lambda: ...}
branch.get(choice, default)()


Statements may span multiple lines if you’re continuing an open syntactic
pair. Python lets you continue typing a statement on the next line if you’re coding
something enclosed in a (), {}, or [] pair.


• Statements may span multiple lines if they end in a backslash. This is a somewhat outdated feature that’s not generally recommended, but if a statement needs
to span multiple lines, you can also add a backslash (a \ not embedded in a string
literal or comment) at the end of the prior line to indicate you’re continuing on the
next line.


------------ A Few Special Cases

L = ["Good",
 "Bad",
 "Ugly"] # Open pairs may span lines


 if a == b and c == d and \
 d == e and f == g:
 print('olde') # Backslashes allow continuations...


if (a == b and c == d and
 d == e and e == f):
 print('new') # But parentheses usually do too, and are obvious


Python allows you to write more than one noncompound
statement (i.e., statements without nested statements) on the same line, separated by
semicolons. Some coders use this form to save program file real estate, but it usually
makes for more readable code if you stick to one statement per line for most of your
work:
x = 1; y = 2; print(x) # More than one simple statement



S = """
aaaa
bbbb
cccc"""
S = ('aaaa'
 'bbbb' # Comments here are ignored
 'cccc')


Finally, Python lets you move a compound statement’s body up to the header line,
provided the body contains just simple (noncompound) statements.

if 1: print('hello') # Simple statement on header line



---------------------- Truth Values and Boolean Tests

Python’s Boolean operators are a bit different from their counterparts 
in languages like C. In Python:

• All objects have an inherent Boolean true or false value.
• Any nonzero number or nonempty object is true.
• Zero numbers, empty objects, and the special object None are considered false.
• Comparisons and equality tests are applied recursively to data structures.
• Comparisons and equality tests return True or False (custom versions of 1 and 0).
• Boolean and and or operators return a true or false operand object.
• Boolean operators stop evaluating (“short circuit”) as soon as a result is known.


The if statement takes action on truth values, but Boolean operators are used to combine the results of other tests in richer ways to produce new truth values. More formally,
there are three Boolean expression operators in Python:
X and Y
Is true if both X and Y are true
X or Y
Is true if either X or Y is true
not X
Is true if X is false (the expression returns True or False)


Also, Boolean and and or operators return
a true or false object in Python, not the values True or False. Let’s look at a few examples
to see how this works:
>>> 2 < 3, 3 < 2 # Less than: return True or False (1 or 0)
(True, False)


On the other hand, the and and or operators always return an object—either the object
on the left side of the operator or the object on the right


--------------  Python or operator
 
For or tests, Python evaluates the operand objects from left to right and returns 
the first one that is true. Moreover, Python stops at the first true operand 
it finds. This is usually called short-circuit evaluation, as determining a 
result short-circuits (terminates) the rest of the expression as soon as the 
result is known:

>>> 2 or 3, 3 or 2  # Return left operand if true
(2, 3)              # Else, return right operand (true or false)


>>> [] or 3
3
>>> [] or {}
{}

the left operand is false (an empty object), so Python simply evaluates and 
returns the object on the right—which may happen to have either a true or a 
false value when tested.


----------- Python and


Python and operations also stop as soon as the result is known; however, in this case
Python evaluates the operands from left to right and stops if the left operand is a false
object because it determines the result—false and anything is always false:
>>> 2 and 3, 3 and 2 # Return left operand if false
(3, 2) # Else, return right operand (true or false)
>>> [] and {}
[]
>>> 3 and []
[]
Here, both operands are true in the first line, so Python evaluates both sides and returns
the object on the right. In the second test, the left operand is false ([]), so Python stops
and returns it as the test result


t. In the last test, the left side is true (3), so Python evaluates
and returns the object on the right—which happens to be a false [].


The end result of all this is the same as in C and most other languages—you get a value
that is logically true or false if tested in an if or while according to the normal definitions
of or and and. However, in Python Booleans return either the left or the right object,
not a simple integer flag.




------------ The if/else Ternary Expression


if X:
 A = Y
else:
 A = Z


# Python 2.5 introduced a new expression format that allows us to say the same 
# thing in one expression:

A = Y if X else Z


>>> A = 't' if 'spam' else 'f' # For strings, nonempty means true
>>> A
't'
>>> A = 't' if '' else 'f'
>>> A
'f'

A = ((X and Y) or Z)


A = Y if X else Z


# -------short-circuit evaluation of Boolean operators and the if/else,

if f1() or f2():
	print("-----")


Here, if f1 returns a true (or nonempty) value, Python will never run f2. To guarantee
that both functions will be run, call them before the or:

tmp1, tmp2 = f1(), f2()

if tmp1 or tmp2:
	pass 



The any and all built-ins can be used to test if any or all items in a 
collection are true (though they don’t select an item):

>>> L = [1, 0, 2, 0, 'spam', '', 'ham', []]
>>> list(filter(bool, L)) 	# Get true values
[1, 2, 'spam', 'ham']
>>> [x for x in L if x] 	# Comprehensions
[1, 2, 'spam', 'ham']
>>> any(L), all(L) 			# Aggregate truth
(True, False)


The bool function here simply returns its argument’s true or false value, 
as though it were tested in an if


1. How might you code a multiway branch in Python?
2. How can you code an if/else statement as an expression in Python?
3. How can you make a single statement span many lines?
4. What do the words True and False mean?



4. True and False are just custom versions of the integers 1 and 0, respectively: they
always stand for Boolean true and false values in Python. They’re available for use
in truth tests and variable initialization, and are printed for expression results at
the interactive prompt. In all these roles, they serve as a more mnemonic and hence
readable alternative to 1 and 0.






