n = int(input("n ="))
avg = 0

for i in range(n):
    mark = int(input("mark ="))
    avg = avg + mark

avg = avg / n

print(avg)