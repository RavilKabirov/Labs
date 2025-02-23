import re
text = "ajdshflkshkjfsdklnjjb adsahdjkhdjkhjkahjk"
pattern5 = r"a.*b"
print(re.findall(pattern5, text))