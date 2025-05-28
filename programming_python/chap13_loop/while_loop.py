"""
looping constructs are statements that repeat an action over and
over.

The language’s two main looping constructs are while and for loop

The while statement, provides a way to code general loops.

The second, the for statement, is designed for stepping through the items in a 
sequence or other iterable object and running a block of code for each.

"""

# It is called a “loop” because control keeps looping back to the start of the 
# statement until the test becomes false.


# ----------------------  General Format

while test: 		# Loop test
 	statements 		# Loop body
else: 				# Optional else
 	statements 		# Run if didn't exit loop with break




while True: 
	print('Type Ctrl-C to stop me!')


x = 'spam'
while x: 				# While x is not empty
	print(x, end=' ') 	# In 2.X use print x,
	x = x[1:] 			# Strip first character off x

spam pam am m


# The following code counts from the value of a up to, but not including, b.

a=0; b=10
while a < b: 			# One way to code counter loops
	print(a, end=' ')
	a += 1 				# Or, a = a + 1

# ---------—---the break and continue statements.

#These are the two simple statements that have a purpose only when nested 
# inside loops

"""
---break
Jumps out of the closest enclosing loop (past the entire loop statement)

---continue
Jumps to the top of the closest enclosing loop (to the loop’s header line)

---pass
Does nothing at all: it’s an empty statement placeholder

---Loop else block
Runs if and only if the loop is exited normally (i.e., without hitting a break)

"""


# -------- General Loop Format
# Factoring in break and continue statements, the general format of the while 
# loop looks like this:

while test:
	statements
	if test: break 			# Exit loop now, skip else if present
 	if test: continue 		# Go to top of loop now, to test1
else:
 	statements 				# Run if we didn't hit a 'break'


# continue  -- The continue statement causes an immediate jump to the top 
# of a loop.
# You can also sometimes avoid nesting by including a break or continue



while True:
	name = input('Enter name:') 
	if name == 'stop': break
	age = input('Enter age: ')
	print('Hello', name, '=>', int(age) ** 2)



