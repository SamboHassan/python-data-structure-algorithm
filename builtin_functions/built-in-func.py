"""
ENUMERATE

Useful for obtaining ab indexed series (0, seq[0]), (1, seq[1])...
start default to zero if not specified

"""
season = ["Spring", "Summer", "Fall", "Winter"]

# for i, seazn in enumerate(season, start=0):
#     print(i, seazn)


"""
ALL()
Return true of all elements are true

"""
all_test = [True, True, True, True]

# print(all(all_test))


"""
ANY()
Return true of ANY of elements are true

"""
all_test = [True, False, False, True]

print(any(all_test))
