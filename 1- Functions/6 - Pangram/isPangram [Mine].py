def is_pangram(s: str):    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    #alphabetCheck = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    
    s = s.lower()
    
    alphabetCheck = []
    
    for i in range(26):
        alphabetCheck.append(False)
    
    
    #if len(s) != 26:
        #return "NO"
    
    for i in range(len(s)):
        if s[i] in alphabet:
            index = alphabet.index(s[i])
            alphabetCheck[index] = True
    
    if False in alphabetCheck:
        return "NO"
    else:
        return "YES"
       
       
s1 = "toosmallword"
print(is_pangram(s1))  # should print NO
s2 = "thequickbrownfoxjumpsoverthelazydog"
print(is_pangram(s2))  # should print YES