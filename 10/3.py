i = 600851475143
factors = []
pfactors = []
if i%2==0:
    factors.append(2)
for x in range(3,i,2):
    if i%x==0:
        factors.append(x)
pfactors = factors.copy()
for x in factors:
    for y in factors:
        if x in pfactors and x%y==0 and x>y and y!=x:
            pfactors.remove(x)
print(pfactors)
