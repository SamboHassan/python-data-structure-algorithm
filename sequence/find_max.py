def find_max(data):
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest


data = [8, 10, 8, 2, 6, 7, 10, 110]

print(find_max(data))
