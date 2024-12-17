# A Simple Interactive Loop
import sys

if sys.version[0] == "2":
    input = raw_input  # 2.X compatible

while True:
    reply = input("Enter text:")
    if reply == "stop":
        break
    print(reply.upper())

while True:
    reply = input("Enter text:")
    if reply == "stop":
        break
    print(int(reply) ** 2)
print("Bye")


while True:
    reply = input("Enter text:")
    if reply == "stop":
        break
    elif not reply.isdigit():
        print("Bad!" * 8)
    else:
        print(int(reply) ** 2)
    print("Bye")


while True:
    reply = input("Enter text:")
    if reply == "stop":
        break
    try:
        num = int(reply)
    except:
        print("Bad!" * 8)
    else:
        print(num**2)
    print("Bye")


while True:
    reply = input("Enter text:")
    if reply == "stop":
        break
    try:
        print(float(reply) ** 2)
    except:
        print("Bad!" * 8)
    print("Bye")


while True:
    reply = input("Enter text:")
    if reply == "stop":
        break
    elif not reply.isdigit():
        print("Bad!" * 8)
    else:
        num = int(reply)
    if num < 20:
        print("low")
    else:
        print(num**2)
    print("Bye")


# in Python # we normally code one statement per line and indent all the statements in a nested block
# the same amount (indentation is part of Python’s syntax).
