import re

# Нужно выделить только пара ключ-значение с ключами lat либо lon
text = "lat = 5, pi= 3,a = 5, lon=7"
match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text) # (:?...) - не сохраняющая группировка
print(match)

match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)
print(match)

# Парсинг пути к файлу из атрибута src
text = "<p>Картинка <img alt = 'картинка'  src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text) # \1 означает что сюда нужно подставить значение первой сохраняющей скобки ()
print(match)

# Но не всегда удобно указывать цифру сохраняющей скобки, если их много. Поэтому используют следующую конструкцию
# (?P<название>...)
# (?P=name) - обращение
match = re.findall(r"<img\s+[^>]*src=(?P<quotation>[\"'])(.+?)(?P=quotation)", text) # \1 означает что сюда нужно подставить значение первой сохраняющей скобки ()
print(match)

# Парсинг xml документа
with open("map.xml", "r") as file:
    lat = []
    lon = []
    for text in file:
        match = re.search(r"<point\s+[^>]*?lon=([\"\'])(?P<lon>[0-9.,]+)\1\s+[^>]*lat=\1(?P<lat>[0-9.,]+)\1", text)
        if match:
            v = match.groupdict()
            if "lon" in v and "lat" in v:
                lon.append(v["lon"])
                lat.append(v["lat"])
    print(lon, lat, sep = "\n")
