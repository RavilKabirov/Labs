import re
with open(r"d:\PP2\Python\Lab5\row.txt", "r", encoding="utf-8") as f:
    text = f.read()

res = re.sub(r'_([a-z])', lambda match: match.group(1).upper(),text)
print(res)