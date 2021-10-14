def inter_len(l1: int, r1: int, l2: int, r2: int) -> int:
    counter = 0
    
    for a in range((l2)+1,(r2)+1):
        if a <= r1 and a > l1:
            counter += 1
    return counter
    
print(inter_len(5, 7, 4, 6))  # should print 1
print(inter_len(1, 5, 2, 4))  # should print 2
print(inter_len(1, 7, 4, 9))  # should print 3
print(inter_len(2, 5, 6, 8))  # should print 0






# Not cleaned
#
# def inter_len(l1: int, r1: int, l2: int, r2: int) -> int:
    # List = []
    
    # counter = 0
    
    # for i in range(1,(max(l1,r1,l2,r2))+1):
        # List.append(i)
    # for a in range((l2)+1,(r2)+1):
        # if a <= r1 and a > l1:
            # counter += 1
            # print(a)
    # print(List)
    
    # return counter

# print(inter_len(5, 7, 4, 6))  # should print 1
# print(inter_len(1, 5, 2, 4))  # should print 2
# print(inter_len(1, 7, 4, 9))  # should print 3
# print(inter_len(2, 5, 6, 8))  # should print 0