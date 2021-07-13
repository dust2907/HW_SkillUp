# =======================================================================
# ===== Дан текстовый файл. Необходимо создать новый файл и записать=====
# в него следующую статистику по исходному файлу:========================
# ■ Количество символов;=================================================
#  ■ Количество строк;===================================================
#  ■ Количество гласных букв;============================================
#  ■ Количество согласных букв; ■ Количество цифр.. =====================
# =======================================================================


a = open("text1.txt", "r", encoding="utf8")
lines = a.readlines()
count_str = len(lines)
a.close()
a = open("text2.txt", "r", encoding="utf8")
text = a.read()
a.close()
count_sy = len(text)

def str_stat(string, b_list):
    count = 0
    for i in string:
        if i in b_list:
            count += 1
    return count


n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
v = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
c = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

count_n = str_stat(text.lower(), n)
count_v = str_stat(text.lower(), v)
count_c = str_stat(text.lower(), c)

x = open("str_stat.txt", "r", encoding="utf8")
x.write(f"Статистика\nКоличество строк: {count_str},\n\
Количество символов: {count_sy},\nКоличество гласных букв: {count_v},\n\
Количество согласных: {count_c},\nКоличество цифр: {count_n}")

x.close()
