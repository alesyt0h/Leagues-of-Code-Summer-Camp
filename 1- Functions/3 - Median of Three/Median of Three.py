def median(a: int, b: int, c: int) -> int:
    list = [a,b,c]
    list.sort()
    return list[1]

print(median(3, 1, 5))  # should print 3
print(median(4, 7, 1))  # should print 4
print(median(10, 1, 5))  # should print 5