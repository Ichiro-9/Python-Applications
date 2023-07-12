from requests import get;from bs4 import BeautifulSoup
from os import chdir;from sys import exit;from tqdm import tqdm
from pyfiglet import figlet_format

print('-'*70)
print(figlet_format('I  m  a  g  e \nd o w n l o a d e r!'))
print("-"*70)

url = input('Enter the URL: ')
dir = input('Enter the dir:')
page = get(url)
soup_obj =  BeautifulSoup(page.text,'html.parser')
images = soup_obj.findAll('img')
print(f'{len(images)} images found in the website')
if len(images) == 0:
    exit()
chdir(dir)

count=0
index=0
print(f'downloading images from {url} into {dir}\ndonwload started:')
for index in tqdm(range(len(images))):
    image = images[index]
    # searching for image source in different ways
    try:source = image["data-srcset"]
    except:
        try:source = image["data-src"]
        except:
            try:source = image["data-fallback-src"]
            except:
                try:source = image["src"]
                except:pass

    try:
        r = get(source).content
        try:
            # possibility of decode
            r = str(r, 'utf-8')
        except:
            # After checking above condition, Image Download start
            with open(f"images{index + 1}.jpeg", "wb+") as f:
                f.write(r)
            # counting number of image downloaded
            count += 1
    except:
        pass
else:
    print(count,'files downloaded')
    if count!= len(images):
        print('The other',len(images)-count,'images request failed')

