import re

text = "Python is an amazing programming language."
pattern = ""

match = re.search(pattern, text)
if match:
    print("Совпадение найдено:", match.group(), len(pattern))
else:
    print("Совпадение не найдено")