while True:
    try:
        a = list(map(int, input("Введите числа через пробел: ").split()))
        break
    except ValueError:
        print("Ошибка! Введите только целые числа.")

is_prime = False
count_pairs = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            count_pairs += 1
            break
print("Количество пар элементов, равных друг другу:", count_pairs)
