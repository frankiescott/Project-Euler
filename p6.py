sum_of_squares = 0
square_of_sum = 0
for i in range(0, 101):
    sum_of_squares += (i * i)
    square_of_sum += i
answer = (square_of_sum * square_of_sum) - sum_of_squares
print(answer)
