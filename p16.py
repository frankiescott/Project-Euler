result = pow(2, 1000)
sum = 0
while result > 0:
    digit = result % 10
    sum += digit
    result = result // 10
print(sum)
