import time

from PIL import Image as img

print("-"*50)
print("Welcome to Image Converter.....\n")

filename = input("Enter the filename: ")
filetype_old = '.'+filename.replace('.',' ').split()[-1]
filetype = input("Enter the required filetype: ")
print(f'\nUploading the File...')
try:
    file = img.open(filename)
    x = 1
except:
    x=0
    print('ERROR!\nGiven file is not a Image.... Please upload a Image file Only')

if x == 1:
    time.sleep(0.5)
    print(f'Converting the file from {filetype_old[1:]} to {filetype}...')
    file.save(f'{filename.replace(filetype_old,"")}.{filetype}')

    time.sleep(0.5)
    print('File successfully converted and saved!')