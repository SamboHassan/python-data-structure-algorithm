my_list = [3, 2, 5, 75, 9, 0, 1]

print(my_list)
my_list.sort()
# print(my_list)
# modifies the list in-place and return None, is only defined for list data type
# while sorted() function accepts any iterable

list2 = sorted(my_list)
# builds a new sorted list from an iterable without modifying the original
# print(list2)
