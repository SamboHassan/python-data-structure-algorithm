# FIRST CLASS OBJECT

items = {"number": 42, "text": "Hello World"}

items["func"] = abs  # Add the abs() function
import math

items["mod"] = math  # Add a module
items["error"] = ValueError  # Add an exception type
nums = [1, 2, 3, 4]
items["append"] = nums.append  # Add a method of another object

print(items["mod"].sqrt(4))

line = "GOOGLE,100,490.10"
field_types = [str, int, float]
raw_fields = line.split(",")

fields = [ty(val) for ty, val in zip(field_types, raw_fields)]
# print(fields, end="\n")

l1 = [2, 3, 4, 5, 6]
l2 = [32, 45, 67]

l1.extend(l2)

# print(l1)


def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x - 1)


countdown(5)
