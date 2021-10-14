from collections import Counter
n = int(input())
a = list(map(int, input().split()))

if n == 0:
    exit()

b = Counter(a)
c = b.most_common(40)

small = 0
item = []

for j in range(len(c)):
        if c[j][1] >= small:
            small = c[j][1]
            item.append(c[j][0])
result = int(min(item))

print(result)
