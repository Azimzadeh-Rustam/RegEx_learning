import re

# re.match - ищет совпадения начиная с самого начала строки

text = "+7(123)456-78-90"
match = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(match)

# re.split - выполняет разбивку строки по которой происходит поиск по заданному шаблону
text = """<point lon="40.8482" lat="52.6274" />
<point lon="40.8559" lat="52.6361" />; <point lon="40.8614" lat="52.651" />
<point lon="40.8676" lat="52.6585" />, <point lon="40.8672" lat="52.6626" />
"""
ar = re.split(r"[\n;,]+", text)
print(ar)

# re.sub - выполняет замену в строке найденных совпадений строкой
# или результатом работы функции repl и возвращает преобразованную строку.
text = """Москва
Казань
Тверь
Самара
Уфа"""
list = re.sub(r"\s*(\w+)\s*", r"<option>\1</option>\n", text)
print(list)

count = 0
def replFind(m):
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>\n"

list = re.sub(r"\s*(\w+)\s*", replFind, text)
print(list)

# re.subn - возвращает не только строку, но и количество произведенных замен
list, total = re.subn(r"\s*(\w+)\s*", r"<option>\1</option>\n", text)
print(list, total)

# re.compile(pattern, flags) - компилирует регулярное выражения и возвращает его в виде экземпляра класса Pattern.
# полезно когда один и тот же шаблон используется многократно и можно просто передавать ссылку на него.
text = """Москва
Казань
Тверь
Самара
Уфа"""

count = 0

rx = re.compile(r"\s*(\w+)\s*")
list, total = rx.subn(r"<option>\1</option>\n", text)
list2 = rx.sub(replFind, text)
print(list, total, list2, sep="\n")
