import shutil

src = r'D:\piton\file.txt'
ext = r'.txt'

#Change the 5 to what number you want to duplicate
for i in range(5):
    shutil.copy(src, f'{src + str(i) + ext}')