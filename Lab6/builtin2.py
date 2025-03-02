a = "fadfsAAdfFDCVqegop,wpmb"
b = sorted(a)

low = 0
up = 0

for i in b:
    if(i.islower()):
        low += 1
    elif(i.isupper()):
        up += 1

print(f"Заглавных: {up} строчных: {low}")