candidates = range(2,200000)
candidates.reverse()
primes = set()
primes.add(2)
while len(primes) < 10001:
    z = candidates.pop()
    found = True
    for i in range(2,z):
        if z % i == 0 and z != i:
            found = False
            break
    if found:
        if len(primes) % 1000 == 0: print(len(primes))
        primes.add(z)
print(max(primes))
