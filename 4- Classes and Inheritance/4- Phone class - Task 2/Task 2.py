from typing import List    

class Phone:
    def __init__(self, company: str, release_year: int, model: str):
        self.company = company
        self.release_year = release_year
        self.model = model

def min_release_year(phones: List[Phone]) -> int:
    list = []
    for element in phones:
        list.append(element.release_year)
    return min(list)

p = Phone("Samsung", 2018, "Galaxy S9");
q = Phone("Samsung", 2021, "Galaxy S21");
r = Phone("Apple", 2018, "XS");
l_phones = [p, q, r]
print(min_release_year(l_phones))  # should print 2018