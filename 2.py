glas = ['а', 'е', 'ё', 'и', 'о', 'ы', 'э', 'ю', 'я']
soglas = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
          'ь']
word = input("Введите слово: ")
count_soglas = 0
count_glas = 0
for letter in word:
    if letter.isalpha():
        if letter.lower() in glas:
            count_glas += 1
        elif letter.lower() in soglas:
            count_soglas += 1
print("Количество гласных букв в словах:", count_glas)
print("Количество согласных букв в словах:", count_soglas)
