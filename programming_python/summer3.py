>>> sums = {}
>>> for line in open('table4.txt'):
... cols = [float(col) for col in line.split()]
... for pos, val in enumerate(cols):
... sums[pos] = sums.get(pos, 0.0) + val
...
>>> for key in sorted(sums):
... print(key, '=', sums[key])
...
0 = 111.3
1 = 222.6
2 = 333.9
3 = 40.4
>>> sums
{0: 111.3, 1: 222.6, 2: 333.90000000000003, 3: 40.4}


"""

we begin our Python programming tour by exploring
the systems application domain—scripts that deal with files, programs, and the general
environment surrounding a program. Although the examples in this domain focus on
particular kinds of tasks, the techniques they employ will prove to be useful in later
parts of the book as well. In other words, you should begin your journey here, unless
you are already a Python systems programming wizard.
"""