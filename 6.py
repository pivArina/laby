my_tuple = tuple(map(int, input("Введите элементы кортежа через пробел: ").split()))
for i in range(len(my_tuple)):
    if my_tuple[i] < 0:
        print("Индекс первого отрицательного элемента:", i)
        break