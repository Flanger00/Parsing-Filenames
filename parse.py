import os

path = 'files\\'

print('scanning..\n')
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)

print('\ndone')
os.system('pause')