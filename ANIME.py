import AnilistPython as apy
import pyfiglet
import dot_art
import pygame.mixer as mixer

mixer.init()
mixer.music.load('red swan.mp3')
mixer.music.play(-1)
from random import choice
ap = apy.Anilist()

print('-'*69)
print(pyfiglet.figlet_format("An im e \n     n e r d", font = "alligator" ))
print("-"*69)
print(dot_art.anime)

print("\n"*3)

print(choice([dot_art.vegeta,dot_art.kakashi,dot_art.luffy,dot_art.ezra,dot_art.light]))
while 1:

    print("_" * 90)
    print("""
    anime(1)
    character(2)
    manga(3)
    """)

    i1= input("Enter func_: ").strip().lower()
    i2 = input("Enter the name_: ").strip().lower()
    try:
        if i1 == "1":
            ap.print_anime_info(i2)  # prints all information regarding the anime Madoka Magica
        if i1 == "2":
            ap.print_character_info(i2)
        if i1 == "3":
            ap.print_manga_info(i2)
    except Exception as e:
        print(f"Error occured({e}), please try again")
        continue
