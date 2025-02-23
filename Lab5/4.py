import re
with open(r"d:\PP2\Python\Lab5\row.txt", "r", encoding="utf-8") as f:
    text = f.read()
pattern4 = r"[A-Z][a-z]+"
print(re.findall(pattern4, text))