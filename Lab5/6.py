import re
with open(r"d:\PP2\Python\Lab5\row.txt", "r", encoding="utf-8") as f:
    text = f.read()
pattern6 = r"[ .,]"
repl = ":"
print(re.sub(pattern6, repl, text))