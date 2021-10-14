rowCol = list(map(int, input().split()))

for x in range(rowCol[0]):
    globals()[f"row{x}"] = list(map(int, input().split()))
    # for a in range(rowCol[1]):
        # sum = sum + eval("row" + str(x) + "[" + str(x) + "]")
    # 
        # pepe = eval("row" + str(x) + "[1]")
        # kek = eval("row" + str(x) + "[" + str(a) + "]") + 2000
        # print(kek)

for i in range(rowCol[1]):
    for q in range(rowCol[0]):
        sum = sum + eval("row" + str(q) + "[" + str(i) + "]")

print(sum)

for t in range(rowCol[1]):
    kekes = eval("row" + str(t) + "[" + str(t) + "]") + eval("row" + str(t) + "[" + str(t) + "]")

# print(eval("row" + str(0)))
# print(eval("row" + str(x) + "[1]"))
# print(row2)
# print(kek)

