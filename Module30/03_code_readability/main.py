from sympy import isprime

print(list(filter(lambda x: isprime(x), range(1001))))
print(list(x for x in range(1001) if isprime(x)))

