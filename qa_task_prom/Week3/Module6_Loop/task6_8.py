n = int(input("n ="))
s = "#"
count = n

while count > 0:
    # Вивід числа count без переходу на новий рядок
    print(count, end = " ") 
    count1 = 0
    while count1 < count:
        print(s, end = "") 
        count1 = count1 + 1
    print() 
    count = count - 1
