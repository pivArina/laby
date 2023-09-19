shop = {
    "Шины": ["Размер: 205/55 R16", "Материал: Резина", "Цена: 4000", "Кол-во: 10"],
    "Масло": ["Тип: Синтетическое", "Объем: 4 литра", "Цена: 2000", "Кол-во: 5"],
    "Тормозные колодки": ["Марка: Bosch", "Тип: Керамические", "Цена: 3000", "Кол-во: 8"],
    "Аккумулятор": ["Емкость: 60 Ач", "Напряжение: 12 В", "Цена: 5000", "Кол-во: 3"],
    "Фильтр воздушный": ["Тип: Сменный", "Цена: 1000", "Кол-во: 15"],
    "Фильтр масляный": ["Тип: Сменный", "Цена: 1200", "Кол-во: 12"]
}

while True:
    print("Меню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню (1-6): ")

    if choice == '1':
        product = input("Введите название продукции: ")
        if product in shop:
            print(product, "-", ", ".join(shop[product][:-2]))
        else:
            print("Такой продукции нет в магазине")

    elif choice == '2':
        product = input("Введите название продукции: ")
        if product in shop:
            print(product, "-", shop[product][-2])
        else:
            print("Такой продукции нет в магазине")

    elif choice == '3':
        product = input("Введите название продукции: ")
        if product in shop:
            print(product, "-", shop[product][-1])
        else:
            print("Такой продукции нет в магазине")

    elif choice == '4':
        for product in shop:
            print(product, "-", ", ".join(shop[product]))

    elif choice == '5':
        product = input("Введите название продукции (n - выход): ")
        if product == 'n':
            continue
        elif product not in shop:
            print("Такой продукции нет в магазине")
            continue

        quantity = input("Введите количество: ")
        if not quantity.isdigit():
            print("Некорректный ввод количества")
            continue

        quantity = int(quantity)
        if quantity > int(shop[product][-1]):
            print("Недостаточно товара на складе")
            continue

        price = int(shop[product][-2]) * quantity
        print(f"Стоимость: {price}")
        shop[product][-1] = str(int(shop[product][-1]) - quantity)

    elif choice == '6':
        print("До свидания!")
        break

    else:
        print("Некорректный ввод")