import csv

filename = 'test.csv'  # Укажите имя вашего CSV-файла

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
  value = data[0][0]
   value2 = data[0][1]
    value3 = data[0][2]
     value3 = data[0][3]
      value3 = data[0][4]
       value3 = data[0][5]
        value3 = data[0][6]
         value3 = data[0][7]
          value3 = data[0][8]
           value3 = data[0][9]
            value3 = data[0][10]
             value3 = data[0][11]
              value3 = data[0][12]
               value3 = data[0][13]
                value3 = data[0][14]

    print(value2)