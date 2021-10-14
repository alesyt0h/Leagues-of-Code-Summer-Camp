n = int(input())
x = int(input())
y = int(input())

availablet = 0

for i in range(n):
    a = int(input())
    if x <= a and a <= y:
        availablet += 1

print(availablet)