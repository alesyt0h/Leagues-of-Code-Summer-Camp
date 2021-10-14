xs = []
ys = []

def add_point(x: int, y: int) -> None:
    global xs, ys
    xs.append(x)
    ys.append(y)

def del_point(x: int, y: int) -> None:
    global xs, ys
    xi = 0
    for i in range(len(xs)):
        if xs[i] == x and ys[i] == y:
            xi = i
    del xs[xi]
    del ys[xi]

def closest() -> int:
    global xs, ys
    d = (xs[0] - xs[1]) ** 2 + (ys[0] - ys[1]) ** 2
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            new_d = (xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2
            if new_d < d:
                d = new_d
    return d

add_point(1, 0)
add_point(2, 3)
add_point(-1, 1)
print(closest()) # should print 5
del_point(-1, 1)
print(closest()) # should print 10
add_point(3, 3)
print(closest()) # should print 1
del_point(2, 3)
print(closest()) # should print 13
add_point(2, 3)
print(closest()) # should print 1