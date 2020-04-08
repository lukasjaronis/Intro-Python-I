def is_prime(n):
    if n is not abs(int(n)):
        return False                            
    if n < 2:                                 
        return False
    if n == 2:                                 
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n/2) + 1, 2):
        if n % i == 0:
            print (n, i, (n % i))
            return False

    return True


primes = [2, 3, 5, 7, 11, 13, 17, 19]
non_primes = [0, -2563, 1, 48, 6, 46]

print("primes:")
for i in primes:
    print(i, "\t", is_prime(i))

print("\nnon-primes:")
for i in non_primes:
    print(i, "\t", is_prime(i))