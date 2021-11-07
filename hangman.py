import random
import os
from typing import ChainMap

menu = """
=======================================================================================================   
=======================================================================================================
     _______                 _______  _        _______  _______  _______  _                _______ 
   |/      |       |\     /|(  ___  )( (    /|(  ____ \(       )(  ___  )( (    /|       |/      |   
   |      (_)      | )   ( || (   ) ||  \  ( || (    \/| () () || (   ) ||  \  ( |       |      (_)
   |      \|/      | (___) || (___) ||   \ | || |      | || || || (___) ||   \ | |       |      \|/ 
   |       |       |  ___  ||  ___  || (\ \) || | ____ | |(_)| ||  ___  || (\ \) |       |       | 
   |      / \      | (   ) || (   ) || | \   || | \_  )| |   | || (   ) || | \   |       |      / \ 
   |               | )   ( || )   ( || )  \  || (___) || )   ( || )   ( || )  \  |       | 
  _|___            |/     \||/     \||/    )_)(_______)|/     \||/     \||/    )_)      _|___ 
    
                                ╔═════════════════════════════════════╗ 
                                  Desarrollado por Carlos Valencia 🦊  
                                ╚═════════════════════════════════════╝ 
=======================================================================================================
=======================================================================================================                                      

Bienvenido al juego del ahorcado!!!
En este juego tendrás que adivinar la palabra que la computadora elegió al azar.
Tendrás 7 intentos para adivinar 🤞🏽
Buena suerte 🍀
"""

IMAGES = [ """ 
____
|/   |
|   
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   /|\
|    |
|   | |
|
|_____
"""]


def word_transformation():
    replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u")
        )
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [i.replace("\n", "") for i in f]
    
    word_selected = random.choice(words)
    for a, b in replacements:
        word_selected = word_selected.replace(a, b)
    return word_selected


def run():
    attemps = 7
    word_selected = word_transformation()
    spaces = ["_"] * len(word_selected)

    while True:
        os.system("clear")
        print(menu)
        for character in spaces: 
            print(character, end=" ")
        print(IMAGES[attemps])
        letter = input("Elige una letra: ").lower()

        found = False
        for idx, character in enumerate(word_selected):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attemps -= 1

        if "_" not in spaces:
            os.system("clear")
            print("Ganaste")
            break
            input()

        if attemps == 0:
            os.system("clear")
            print("Perdiste")
            break
            input()


if __name__ == "__main__":
    run()