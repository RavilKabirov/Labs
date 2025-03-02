import os
fil = input()
if os.path.exists(fil):
  os.remove(fil)
else:
  print("The file does not exist") 