def prime(n: int) -> bool:
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False

print(prime(7))  # should print True
print(prime(4))  # should print False
print(prime(11)  # should print True
print(prime(1))  # should print False
