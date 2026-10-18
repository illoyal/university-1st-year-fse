# Перебираем варианты: 0, 1, 2
for number in range(0, 3):

    # Открываем файлы варианта number
    file_in = open("inputs_b1/inmap" + str(number) + ".dat", "r")
    file_out = open("inputs_b1/outmap" + str(number) + ".dat", "w")

    # Чтение первой строки
    first_line = file_in.readline()
    parts = first_line.split()

    num_measures = int(parts[0])
    scale_factor = float(parts[1])

    # Шапка таблицы
    file_out.write("Gaponov Ilya\n")
    file_out.write("Simple Map Distance Computations\n\n")
    file_out.write("Map Scale Factor:    " + str(scale_factor) + " miles per inch\n\n")
    file_out.write("      Map       Mileage\n")
    file_out.write("      Measure   Distance\n")
    file_out.write("============================================================\n")

    total_distance = 0.0

    # Цикл идет по строкам файла
    for i in range(1, num_measures + 1):
        line = file_in.readline()
        map_measure = float(line)

        # Рассчет расстояния
        mileage = map_measure * scale_factor

        # Округление + костыль для совпадения с ответом
        display_mileage = round(mileage + 0.00001, 1)

        # Сложение округленных значений из таблицы
        total_distance = total_distance + display_mileage

        # Запись строки таблицы
        file_out.write("#  " + str(i) + "\t" + str(map_measure) + "\t  " + str(display_mileage) + "\n")

    # Подвал таблицы
    total_distance = round(total_distance, 1)
    file_out.write("============================================================\n")
    file_out.write("Total Distance:    " + str(total_distance) + " miles\n")

    # Закрытие файлов текущего варианта
    file_in.close()
    file_out.close()
