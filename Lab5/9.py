import re
with open(r"d:\PP2\Python\Lab5\row.txt", "r", encoding="utf-8") as f:
    text = f.read()
res = re.sub(r"(?<!^)(?=[A-Z])", " ", text )
print(res)