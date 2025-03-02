import os


path = input()
lst = os.listdir(path)

only_folders = [d for d in lst if os.path.isdir(os.path.join(path, d))]
only_files = [f for f in lst if os.path.isfile(os.path.join(path, f))]
print(only_folders)
print(only_files)
print(lst)