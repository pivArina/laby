print("Введите диапазон чисел")
while True:
    try:
        a = int(input("Начало диапазона: "))
        b = int(input("Конец диапазона: "))
        break
    except ValueError:
        print("Ошибка! Введите только целые числа.")

is_prime = False

for i in range(a, b + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print("Простые числа в диапазоне:", i)
            is_prime = True

if not is_prime:
    print("Простых чисел нет.")
