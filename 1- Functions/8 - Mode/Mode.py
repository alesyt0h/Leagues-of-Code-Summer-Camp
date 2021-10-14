from collections import Counter


def mode(a: list) -> int:
    b = Counter(a)
    c = b.most_common(40)
    
    small = 0
    item = []
    
    for j in range(len(c)):
            if c[j][1] >= small:
                small = c[j][1]
                item.append(c[j][0])
    result = int(min(item))
    
    return result
    
print(mode([3, 1, 5, 3, 4, 4, 3]))  # should print 3
print(mode([5, 5, 1, 5, 1, 1, 7, 5, 1]))  # should print 1
print(mode([10, 5, 7, 9, 7, 5, 10]))  # should print 5    