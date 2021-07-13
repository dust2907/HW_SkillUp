# =======================================================================
# ========== Дан текстовый файл. Посчитать сколько раз в ================
# =========нем встречается заданное пользователем слово. ================
# =======================================================================

with open("text2.txt", "r", encoding="utf8") as file:
    text = file.readlines()
text2 = []
for i in text:
    i.strip()
    text2.append(i)
text = " ".join(text2)
words_list = text.lower().split(" ")
word = input("Введите слово: ")
words = 0
for i in words_list:
    if i.strip() == word:
        words += 1
print(f"Слово '{word}' встречается {words} раз")
