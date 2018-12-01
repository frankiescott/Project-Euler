sum = 0
fib1 = 0
fib2 = 1
while fib2 < 4000000:
    if (fib1 + fib2) % 2 == 0:
        sum = sum + fib1 + fib2
    tmp = fib1
    fib1 = fib2
    fib2 = tmp + fib2
print(sum)
