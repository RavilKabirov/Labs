import re
text = "Abbbbb abbbb ab abbbbb abb abbb"
text1 = "abb"
pattern2 = r"ab{2,3}"
print(re.findall(pattern2, text))
print(re.findall(pattern2, text1))