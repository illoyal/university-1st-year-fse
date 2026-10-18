for number in range(1, 4):
    file_in = open("inputs_b2/" + str(number) + ".WCData.txt", "r")
    file_out = open("inputs_b2/" + str(number) + ".WindChillReport.txt", "w")

    file_out.write("Time     WC temp     WC Effect\n")
    file_out.write("------------------------------\n")

    file_in.readline()
    file_in.readline()

    total_wc_temp = 0.0
    count = 0

    line = file_in.readline()

    while line != "":
        if line.strip() == "":
            line = file_in.readline()
            continue

        parts = line.split()
        time_str = parts[0]
        t_f = float(parts[1])
        v = float(parts[2])

        t_wc = 35.74 + 0.6125 * t_f + (0.4275 * t_f - 35.75) * (v ** 0.16)

        # По той же причине что и в B1 добавляется 0.00001
        display_wc_temp = round(t_wc + 0.00001, 1)

        display_wc_effect = round((t_wc - t_f) + 0.00001, 1)

        total_wc_temp = total_wc_temp + display_wc_temp
        count = count + 1

        file_out.write(time_str + "\t" + str(display_wc_temp) + "\t" + str(display_wc_effect) + "\n")

        line = file_in.readline()

    average_wc = round((total_wc_temp / count) + 0.00001, 1)

    file_out.write("------------------------------\n\n")
    file_out.write(
        "The average adjusted temperature, based on " + str(count) + " observations, was " + str(average_wc) + "\n")

    file_in.close()
    file_out.close()
