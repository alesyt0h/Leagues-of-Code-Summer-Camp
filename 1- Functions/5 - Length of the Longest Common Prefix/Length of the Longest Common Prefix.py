def max_len_prefix(s: str, t: str) -> int:
    counter = 0
    longerString = max(len(s),len(t))
    
    for i in range(0,longerString):
        try:
            if s[i] == t[i]:
                counter += 1
        except IndexError:
            pass
        
    return counter

print(max_len_prefix("abc", "ad"))  # should print 1
print(max_len_prefix("John", "Johnson")  # should print 4
print(max_len_prefix("abc", "hello"))  # should print 0