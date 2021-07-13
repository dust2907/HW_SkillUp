# =======================================================================
# ===== Дано два текстовых файла. Выяснить, совпадают ли их строки.======
# =====Если нет, то вывести несовпадающую строку из каждого файла. ======
# =======================================================================

with open("text1.txt", "r", encoding="utf8") as file:
    txt1 = file.readlines()

with open("text2.txt", "r", encoding="utf8") as file:
    txt2 = file.readlines()


def output_of_deviations(list1, list2):
    d_lines = []
    for i in list1:
        if i not in list2:
            d_lines.append(i)
    return d_lines


def variance(u_list):
    if u_list:
        for i in u_list:
            print(i, end='')
        print("")


print("Уникальные строки первого файла:")
variance(output_of_deviations(txt1, txt2))
print("Уникальные строки второго файла:")
variance(output_of_deviations(txt1, txt2))
print("Сравнение файлов:")
variance(output_of_deviations(txt1, txt2))
