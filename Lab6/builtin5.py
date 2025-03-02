a = ("sda", 1, 5, True, "bba")
flag = True
for i in a:
    if bool(i) == False:
        flag = False
if(flag):
    print("True")
else: 
    print("False")