'''
Напишіть програму-таймер зворотного відліку, яка запитує у користувача кількість секунд n, з якої слід починати відлік.
Пояснення розв’язку
Організовуємо ввід числа n. Потрібно організувати вивід всіх чисел від n до 1, для цього використаємо цикл while. Умова циклу n>=1. В тілі циклу організовуємо вивід числа n, після виводу зменшуємо значення числа n на одиницю. Після закінчення роботи циклу виводимо на екран “Start”.
'''

n = int(input("n ="))

while n >=1:
    print(n)
    n = n - 1

print("Start")
