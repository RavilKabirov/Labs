import os
path = input()
print(os.path.exists(path))
if (os.path.exists(path)):
    print(os.path.basename(path))
    print(os.path.dirname(path))
