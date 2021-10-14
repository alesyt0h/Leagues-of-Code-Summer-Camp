def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return "NO"
  
    return "YES"
       
       
s1 = "toosmallword"
print(is_pangram(s1))  # should print NO
s2 = "thequickbrownfoxjumpsoverthelazydog"
print(is_pangram(s2))  # should print YES