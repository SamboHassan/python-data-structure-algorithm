# This chapter begins our in-depth tour of specific Python statements. We’ll
# begin with the basics: # assignment statements, expression statements,
# and print operations.


# Assignments create object references.
# Names are created when first assigned
# Names must be assigned before being referenced
# Some operations perform assignments implicitly.

"""
In this section we’re concerned with the = statement, but assignment occurs 
in many contexts in Python. For instance, we’ll see later that module imports, function and class definitions,
for loop variables, and function arguments are all implicit assignments. 
Because assignment works the same everywhere it pops up, all these contexts 
simply bind names to object references at runtime.

"""

# They always create references to objects instead of copying the objects.
# Because of that,Python variables are more like pointers than data
# storage areas.

"""
Operation 						Interpretation
spam = 'Spam' 					Basic form
spam, ham = 'yum', 'YUM' 		Tuple assignment (positional) unpacking
[spam, ham] = ['yum', 'YUM'] 	List assignment (positional) unpacking
a, b, c, d = 'spam' 			Sequence assignment, generalized, unpacking
a, *b = 'spam' 					Extended sequence unpacking (Python 3.X)
spam = ham = 'lunch' 			Multiple-target assignment
spams += 42 					Augmented assignment (equivalent to spams = 
								spams + 42)
"""


# -------- Sequence-unpacking Assignments

# Basic assignment
x = 1
y = 2

# print(x, y)

# Tuple assignment
a, b = x, y

# print(a, b)

# List assignment
[e, f, _] = [x, y, 0]
[c, _, _] = [x, y, _]
# print(c)

# Tuples: swaps values
foo = 30
bar = 50
# print(foo, bar)

foo, bar = bar, foo
# print(foo, bar)

# accept any type of sequence (really, iterable)
[a, b, c] = (1, 2, 3)  # Assign tuple of values to list of names

(a, b, c) = "ABC"  # Assign string of characters to tuple
# print((a, b, c))
# print((a, _, c))
# print((a, c))

r = "SPAM"
a, b, c = r[0], r[1], r[2:]


# Advanced sequence assignment patterns
>>> a, b, c = string[0], string[1], string[2:] # Index and slice
>>> a, b, c
('S', 'P', 'AM')
>>> a, b, c = list(string[:2]) + [string[2:]] # Slice and concatenate
>>> a, b, c
('S', 'P', 'AM')
>>> a, b = string[:2] # Same, but simpler
>>> c = string[2:]
>>> a, b, c
('S', 'P', 'AM')
>>> (a, b), c = string[:2], string[2:] # Nested sequences
>>> a, b, c
('S', 'P', 'AM')

>>> ((a, b), c) = ('SP', 'AM') # Paired by shape and position
>>> a, b, c
('S', 'P', 'AM')


for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: ... # Simple tuple assignment
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: ... # Nested tuple assignment

for a, *b, c in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(b)

# When used in this context, on each iteration Python simply assigns 
# the next tuple of values to the tuple of names.

# for a, b, _ in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
#     print(a, b)

for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
	a, b, c = all[0], all[1:3], all[3]


for a in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
    print(a)

for a in (1, 2, 3):
    print(a)



# for a, b, c in ("abr", "by8", "cuu"):
#     print(a, b, c)

>>> red, green, blue = range(3)
>>> red, blue
(0, 2)


Another place you may see a tuple assignment at work is for splitting a sequence into
its front and the rest in loops like this:
>>> L = [1, 2, 3, 4]
>>> while L:
... front, L = L[0], L[1:] # See next section for 3.X * alternative
or:
... front = L[0]
... L = L[1:]

... print(front, L)
...
1 [2, 3, 4]
2 [3, 4]
3 [4]
4 []

# ------------ Extended unpacking in action

>>> a, *b = seq
>>> a
1
>>> b
[2, 3, 4]


>>> *a, b = seq
>>> a
[1, 2, 3]
>>> b
4


>>> *a, b = seq
>>> a
[1, 2, 3]
>>> b
4


>>> a, *b, c = seq
>>> a
1
>>> b
[2, 3]
>>> c
4


>>> a, b, *c = seq
>>> a
1
>>> b
2
>>> c
[3, 4]



Naturally, like normal sequence assignment, extended sequence unpacking syntax
works for any sequence types (really, again, any iterable), not just lists. Here it is unpacking characters in a string and a range (an iterable in 3.X):
>>> a, *b = 'spam'
>>> a, b
>>> a, *b = 'spam'
>>> a, b
('s', ['p', 'a', 'm'])
>>> a, *b, c = 'spam'
>>> a, b, c
('s', ['p', 'a'], 'm')
>>> a, *b, c = range(4)
>>> a, b, c
(0, [1, 2], 3)




This is similar in spirit to slicing, but not exactly the same—a sequence unpacking
assignment always returns a list for multiple matched items, whereas slicing returns a
sequence of the same type as the object sliced:
>>> S = 'spam'
>>> S[0], S[1:] # Slices are type-specific, * assignment always returns a list
('s', 'pam')
>>> S[0], S[1:3], S[3]
('s', 'pa', 'm')


>>> L = [1, 2, 3, 4]
>>> while L:
... front, *L = L # Get first, rest without slicing
... print(front, L)
...
1 [2, 3, 4]
2 [3, 4]
3 [4]
4 []



# -------------  Boundary cases
# The starred name may match just a single item, but is always assigned 
# a list:
seq = [1, 2, 3, 4]

>>> a, b, c, *d = seq
>>> print(a, b, c, d)
1 2 3 [4]

>>> a, b, c, d, *e = seq
>>> print(a, b, c, d, e)
1 2 3 4 []
>>> a, b, *e, c, d = seq
>>> print(a, b, c, d, e)
1 2 3 4 []


>>> a, *b, c, *d = seq
SyntaxError: two starred expressions in assignment
>>> a, b = seq
ValueError: too many values to unpack (expected 2)
>>> *a = seq
SyntaxError: starred assignment target must be in a list or tuple
>>> *a, = seq
>>> a
[1, 2, 3, 4]



The common “first, rest”
splitting coding pattern, for example, can be coded either way, but slicing involves extra
work:
>>> seq
[1, 2, 3, 4]
>>> a, *b = seq # First, rest
>>> a, b
(1, [2, 3, 4])
>>> a, b = seq[0], seq[1:] # First, rest: traditional
>>> a, b
(1, [2, 3, 4])




# The also-common “rest, last” splitting pattern can similarly be coded 
# either way, but the new extended unpacking syntax requires noticeably 
# fewer keystrokes:

>>> *a, b = seq # Rest, last
>>> a, b
([1, 2, 3], 4)
>>> a, b = seq[:-1], seq[-1] # Rest, last: traditional
>>> a, b
([1, 2, 3], 4)


# Multiple-target assignment and shared references

>>> a = b = 0
>>> b = b + 1
>>> a, b
(0, 1)
Here, changing b only changes b because numbers do not support in-place changes. As
long as the object assigned is immutable, it’s irrelevant if more than one name references
it.


As usual, though, we have to be more cautious when initializing variables to an empty
mutable object such as a list or dictionary:
>>> a = b = []
>>> b.append(42)
>>> a, b
([42], [42])


To avoid the issue, initialize
mutable objects in separate statements instead, so that each creates a distinct empty
object by running a distinct literal expression:
>>> a = []
>>> b = [] # a and b do not share the same object
>>> b.append(42)
>>> a, b
([], [42])



A tuple assignment like the following has the same effect—by running two list expressions, it creates two distinct objects:
>>> a, b = [], [] # a and b do not share the same object


# Augmented Assignments

X = X + Y # Traditional form
X += Y # Newer augmented form


X += Y X &= Y X −= Y X |= Y
X *= Y X ^= Y X /= Y X >>= Y
X %= Y X <<= Y X **= Y X //= Y

1. C/C++ programmers take note: although Python now supports statements like X += Y, it still does not
have C’s auto-increment/decrement operators (e.g., X++, −−X). These don’t quite map to the Python object
model because Python has no notion of in-place changes to immutable objects like numbers.


To add a single item to the end of a list, we
can concatenate or call append:
>>> L = [1, 2]
>>> L = L + [3] # Concatenate: slower
>>> L
[1, 2, 3]
>>> L.append(4) # Faster, but in place
>>> L
[1, 2, 3, 4]


And to add a set of items to the end, we can either concatenate again or call the list
extend method:2
>>> L = L + [5, 6] # Concatenate: slower
>>> L
[1, 2, 3, 4, 5, 6]
>>> L.extend([7, 8]) # Faster, but in place
>>> L
[1, 2, 3, 4, 5, 6, 7, 8]



# In both cases, concatenation is less prone to the side effects of shared 
# object references but will generally run slower than the in-place 
# equivalent. Concatenation operations must create a new object, copy in 
# the list on the left, and then copy in the list on the right. By contrast, in-place method calls simply add items at the end of a memory block
# (it can be a bit more complicated than that internally, but this 
# description suffices).


concatenation operation implied by +:
>>> L += [9, 10] # Mapped to L.extend([9, 10])
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


>>> L = []
>>> L += 'spam' # += and extend allow any sequence, but + does not!


>>> L = [1, 2]
>>> M = L # L and M reference the same object
>>> L = L + [3, 4] # Concatenation makes a new object
>>> L, M # Changes L but not M
([1, 2, 3, 4], [1, 2])
>>> L = [1, 2]
>>> M = L
>>> L += [3, 4] # But += really means extend
>>> L, M # M sees the in-place change too!
([1, 2, 3, 4], [1, 2, 3, 4])



>>> L = [1, 2]
>>> L.append(3) # Append is an in-place change
>>> L
[1, 2, 3]




As described in Chapter 6, objects have a type (e.g.,
integer, list) and may be mutable or not. Names (a.k.a. variables), on the other hand,
are always just references to objects; they have no notion of mutability and have no
associated type information, apart from the type of the object they happen to reference
at a given point in time.
Thus, it’s OK to assign the same name to different kinds of objects at different times:
>>> x = 0 # x bound to an integer object
>>> x = "Hello" # Now it's a string
>>> x = [1, 2, 3] # And now it's a list


names also live in something called a scope, which defines where they can be used; the place where you assign
a name determines where it is visible.4


For additional naming suggestions, see the discussion of naming conventions in Python’s semi-official style guide, known as PEP 8. This
guide is available at http://www.python.org/dev/peps/pep-0008, or via a
web search for “Python PEP 8.” Technically, this document formalizes
coding standards for Python library code.
Though useful, the usual caveats about coding standards apply here.
For one thing, PEP 8 comes with more detail than you are probably ready


there is no notion
of C++’s const declaration in Python; certain objects may be immutable, but names can always be
assigned