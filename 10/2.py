fib = [1,1]
ans = 0
while fib[-1] < 4000000:
    if (fib[-1]+fib[-2]) % 2 == 0:
        ans += fib[-1]+fib[-2]
    fib.append(fib[-1]+fib[-2])
print(ans)
