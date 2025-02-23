import re
text = "ShoKavoPoch"
res = re.sub(r"(?<!^)(?=[A-Z])", "_", text )
print(res)