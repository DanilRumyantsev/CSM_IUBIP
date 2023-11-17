import csv

def read_values_from_csv(filename):
    values = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            values[row[0]] = row[1]
    return values

filename = 'your_file.csv'  # Укажите имя вашего CSV-файла

# Чтение значений из CSV-файла
values = read_values_from_csv(filename)

# Использование значений
for key, value in values.items():
    exec(f"{key} = '{value}'")  # Создание переменной из имени в CSV и присваивание значения

# Вывод значений переменных
print(a)  # Выведет 'hello'
print(b)  # Выведет 'bay'