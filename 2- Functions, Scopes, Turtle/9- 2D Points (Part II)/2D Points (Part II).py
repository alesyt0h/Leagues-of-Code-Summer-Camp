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


def area() -> int:
    res = 0
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            for k in range(j + 1, len(xs)):
                for l in range(k + 1, len(xs)):
                    xp = [xs[i], xs[j], xs[k], xs[l]]
                    xp.sort()
                    yp = [ys[i], ys[j], ys[k], ys[l]]
                    yp.sort()
                    cond_x = xp[0] == xp[1] and xp[2] == xp[3]
                    cond_y = yp[0] == yp[1] and yp[2] == yp[3]
                    if cond_x and cond_y:
                        new_area = (xp[2] - xp[1]) * (yp[2] - yp[1])
                        if new_area > res:
                            res = new_area
    return res



add_point(0, 0)
add_point(2, 0)
add_point(0, 4)
print(closest()) # should print 4
print(area()) # should print 0
add_point(2, 4)
print(area()) # should print 8
del_point(0, 0)
del_point(0, 4)
print(closest()) # should print 16
print(area()) # should print 0
add_point(3, 4)
print(closest()) # should print 1
print(area()) # should print 0
add_point(3, 0)
print(area()) # should print 4
add_point(-100, -100)
add_point(-100, 100)
add_point(100, -100)
add_point(100, 100)
print(area()) # should print 40000