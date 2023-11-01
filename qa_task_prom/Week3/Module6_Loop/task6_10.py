import math
n = int(input("n ="))
flag = False
div = 2

while div <= math.sqrt(n) and not (flag):
    if n % div == 0:
        flag = True
    div = div + 1
if flag:
    print("Not a prime number")
else:
    print("Prime number")