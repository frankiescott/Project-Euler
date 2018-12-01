prime_num = 2
count = 0
while True:
    prime = True
    for i in range(2, prime_num):
        if prime_num % i == 0:
            prime = False
            break
    if prime == True:
        count += 1
    if count == 10001:
        print(prime_num)
        break
    prime_num += 1
