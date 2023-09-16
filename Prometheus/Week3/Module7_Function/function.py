def maximum(x, y):
    if x > y:
        max = x
    else:
        max = y
    
    return max

a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))
d = float(input("d ="))
max1 = maximum(a, b)
max2 = maximum(c, d)
result = maximum(max1, max2)

print("Max result =", result)