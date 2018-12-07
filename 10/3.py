n = 600851475143
i = 2
found = set()
while True:
    if i == n or n in found:
        print(i)
        break
    if n%i == 0:
        n /= i
        found.add(i)
        i = 2
    else:
        i += 1