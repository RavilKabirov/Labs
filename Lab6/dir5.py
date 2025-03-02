a = ["1", "2", "3"]

with open ("test1.txt", 'w+') as f:
    for items in a:
        f.write('%s\n' %items)
f.close()