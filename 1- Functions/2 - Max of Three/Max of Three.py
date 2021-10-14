def max(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c


print(max(3, 1, 5))  # should print 5
print(max(4, 7, 1))  # should print 7
print(max(10, 1, 5))  # should print 10