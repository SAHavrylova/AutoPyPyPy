n = int(input("n ="))
div = 1
temp = n

while temp > 9:
    temp = temp // 10
    div = div * 10

while div > 0:
    print(n // div)
    n = n % div
    div = div // 10