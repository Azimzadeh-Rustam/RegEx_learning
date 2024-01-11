import re

# квантификатор {m,n}. Его обычный режим работы - ищет наиболее длинную последовательность (мажорный или жадный)
text = "Google, Goooogle, Goooooogle"
match = re.findall(r"o{2,5}", text)
print(match)

#Для перевода квантификатора {} в минорный режим работы, после него нужно поставить знак ?
match = re.findall(r"o{2,5}?", text)
print(match)

# {m} = {m,m} - повторение ровно m раз
# {m,} - повторение от m и более
# {,m} - повторение не более m раз

match = re.findall(r"Go{2,}gle", text)
print(match)

match = re.findall(r"Go{,4}gle", text)
print(match)

phone = "89123456789"
match = re.findall(r"8\d{10}", phone)
print(match)

# {0,1} = ? - либо есть либо нет
# {0,} = *
# {1,} = +

# Выполним парсинг этой строки по ключам и значениям
text = "author=Пушкин А.С.; title = Евгений Онегин;price =200; year= 2001"
match = re.findall(r"(\w+)\s*=\s*([^;]+)", text) # ^; - все слова, кроме ;
print(match) # получатся кортежи, состоящие отдельно от ключ - значение

# выделение тега img
text = "<p>Картинка <img alt = 'картинка'  src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text)
print(match)
