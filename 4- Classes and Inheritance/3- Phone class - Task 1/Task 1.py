class Phone:
    def __init__(self, company: str, release_year: int, model: str):
        self.company = company
        self.release_year = release_year
        self.model = model

def in_same_company(p: Phone, q: Phone) -> str:
    if p.company == q.company:
        return "YES"
    else:
        return "NO"

p = Phone("Samsung", 2018, "Galaxy S9");
q = Phone("Samsung", 2021, "Galaxy S21");
r = Phone("Apple", 2018, "XS");
print(in_same_company(p, q))  # should print "YES"
print(in_same_company(p, r))  # should print "NO"