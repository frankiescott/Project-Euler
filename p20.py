total = 1
start = 100
while start != 0:
    total = total * start
    start -= 1
strtotal = str(total)
count = 0
for i in range(0, len(strtotal)):
    count = count + int(strtotal[i])
print(count)
