import os

# Using generator expression
nums = [1, 2, 3, 4, 5, 6]

s = sum(x * x for x in nums)
print(s)

files = os.listdir(os.path.expanduser("."))

if any(name.endswith(".py") for name in files):
    print("There be python")
else:
    print("Sorry no python")


# Output a tuple as csv - convert list to string
s = ("ACME", 50, 123.67)

print(",".join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {"name": "GOOG", "shares": 50},
    {"name": "YHOO", "shares": 75},
    {"name": "AOL", "shares": 20},
    {"name": "SCOX", "shares": 65},
]
# Using gerator expression
min_shares = min(s["shares"] for s in portfolio)
print(min_shares)
