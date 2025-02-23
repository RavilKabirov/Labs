import re

text = "asasas_asasajkjkjd_as ajksdj _asas_"
pattern3 = r"[a-z]+_[a-z]+"

print(re.findall(pattern3, text))