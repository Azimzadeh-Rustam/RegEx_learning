import re

# флаги и проверки
text = "подоходный налог, доход"
# \b \b - границы слова (найдет только как отдельное слово, а не в составе другого)
match = re.findall(r"прибыль|обретение|\bдоход\b", text)
match = re.findall(r"\b(?:прибыль|обретение|доход)\b", text)
print(match)

text = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<p align=center>Hello World!</p>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""

# . - не включает символа переноса строки
# ^ - начало строки
# (?=</script>) - до тех пор пока не встретится закрывающий тег </script>
match = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text, re.MULTILINE)
print(match)
# (?<=</script>) - до тех пор пока не встретится закрывающий тег </script> (включая его самого)
match = re.findall(r"^<script.*?>([\w\W]+)(?<=</script>)", text, re.MULTILINE)
print(match)

# выделение всех пар ключ-значение
match = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text, re.MULTILINE)
print(match)

text = "Python, python, PYTHON"
match = re.findall(r"(?im)python", text)
print(match)
