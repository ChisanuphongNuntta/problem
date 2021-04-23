#Filter Primes from a List
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n%i:
            return False
    return True

def filter_primes(num):
	return [i for i in num if is_prime(i)]

print(filter_primes([7, 9, 3, 9, 10, 11, 27]))