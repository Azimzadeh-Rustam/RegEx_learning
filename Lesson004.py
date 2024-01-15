import re

text = "<font color=#CC0000>"
match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", text)
print(match)

match = re.search(r"(\w+)=(#[\da-fA-F]{7})\b", text)
print(match)

match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", text)
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(0, 1, 2)) # кортеж из групп перечисленных индексов
print(match.groups()) # кортеж из всех групп начиная с индекса 1
print(match.lastindex)
print(match.start(1))
print(match.end(1))
print(match.span(0)) # кортеж с начальным и конечным индексами соответствующей группы
print(match.re) # скомпилированный шаблон
print(match.string) # возвращает анализируемую строку

match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match)
print(match.groupdict())
print(match.lastgroup)
print(match.expand(r"\g<key>:\g<value>"))

# re.search(pattern, string, flags) - ищет только первое вхождение (совпадение по шаблону в строке)

# re.finditer(pattern, string, flags) - ищет все совпадения и возвращает итерируемый объект
# этот метод возвращает объект Match который содержит очень много всего

# re.findall(pattern, string, flags) - возвращает список всех совпадений
# недостаток этого метода - ограниченность полученных данных

text = "<font color=#CC0000 bg=#ffffff>"

match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match)

for match in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text):
    print(match)

match = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match)