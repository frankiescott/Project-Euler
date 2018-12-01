num = 1
while True:
    divisible = True
    for i in range(1, 21):
        if num % i > 0:
            divisible = False
            num += 1
            break
    if divisible == True:
        break
print(num)
