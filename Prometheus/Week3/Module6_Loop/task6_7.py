age = int(input("age ="))

if age %2 == 0:
    start = 0
else:
    start = 1

for i in range(start, age +1, 2):
    print(i)
