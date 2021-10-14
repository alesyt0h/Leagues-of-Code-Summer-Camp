arrCount = int(input())
x = list(map(int, input().split()))

# string = str(input())
# x = string.split()
# NOT Accepted because it was a list of strings instead of a list of integers ??¿¿

pits = 0

for index, item in enumerate(x, start=0):
    if index == 0:
        continue
    elif index == arrCount - 1:
        continue
    else:
        if item < x[index - 1] and item < x[index + 1]:
            pits += 1

print(pits)