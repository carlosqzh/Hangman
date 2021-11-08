import random
import os
from typing import Type

menu = """
===================================================================================================================================  
===================================================================================================================================
       (/)                                                                                                              (/)
       (/)                                                                                                              (/)
        (/)                                                                                                              (/)
       (/)              7MMF'  `7MMF'                                                                                   (/)
        (/)              MM      MM                                                                                      (/)
       (/)               MM      MM   ,6"Yb.  `7MMpMMMb.   .P"Ybmmm `7MMpMMMb.pMMMb.   ,6"Yb.  `7MMpMMMb.               (/)
       (/))              MMmmmmmmMM  8)   MM    MM    MM  :MI  I8     MM    MM    MM  8)   MM    MM    MM               (/)
      (/)(/)             MM      MM   ,pm9MM    MM    MM   WmmmP"     MM    MM    MM   ,pm9MM    MM    MM              (/)(/) 
     (/)'`(/)            MM      MM  8M   MM    MM    MM  8M          MM    MM    MM  8M   MM    MM    MM             (/)'`(/)
    (/)    (/)          JMML.  .JMML.`Moo9^Yo..JMML  JMML. YMMMMMb  .JMML  JMML  JMML.`Moo9^Yo..JMML  JMML.          (/)    (/)   
    (/)    (/)                                             6'     dP                                                 (/)    (/)
    (/)    (/)                                              Ybmmmd'                                                  (/)    (/)
    (/)    (/)                                                                                                       (/)    (/)
     (/)  (/)                              ╔═════════════════════════════════════╗                                    (/)  (/)
      (/)(/)                                 Desarrollado por Carlos Valencia 🦊                                       (/)(/)
       `""`                                ╚═════════════════════════════════════╝                                       `""`
===================================================================================================================================  
===================================================================================================================================
    Bienvenido al juego del ahorcado!!!
    En este juego tendrás que adivinar una palabra que la computadora elegió al azar.
    Al iniciar el juego contars con 7 vidas ❤️❤️❤️❤️❤️❤️❤️
    Por cada intento fallido perderás una vida, elige con cuidado 👀
    Buena suerte 🍀
"""

IMAGES = [ """
 ____
|/   |
|   (_)
|   /|\\
|    |
|   | |
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
|    
|    
|    
|
|_____
""",
"""
____
|/   |
|   
|    
|    
|    
|
|_____
""",
]

win = """
       .--------.
     .: : :  :___`.                  sSSSSs    .S_SSSs     .S_sSSs     .S_SSSs      sSSs  sdSS_SSSSSSbs    sSSs 
   .'!!:::::  \\_\ `.                d%%%%SP   .SS~SSSSS   .SS~YS%%b   .SS~SSSSS    d%%SP  YSSS~S%SSSSSP   d%%SP 
  /%O!!::::::::\\_\. \               d%S'      S%S   SSSS  S%S   `S%b  S%S   SSSS  d%S'         S%S       d%S' 
 /%%O!!:::::::::  : . \             S%S       S%S    S%S  S%S    S%S  S%S    S%S  S%|          S%S       S%S  
|%%OO!!::::::::::: : . |            S&S       S%S SSSS%S  S%S    S&S  S%S SSSS%S  S&S          S&S       S&S 
|%%OO!!:::::::::::::  :|            S&S       S&S  SSS%S  S&S    S&S  S&S  SSS%S  Y&Ss         S&S       S&S_Ss  
|%%OO!!!::::::::::::: :|            S&S       S&S    S&S  S&S    S&S  S&S    S&S  `S&&S        S&S       S&S~SP  
 \%%OO!!!:::::::::::: :|            S&S sSSs  S&S    S&S  S&S    S&S  S&S    S&S    `S*S       S&S       S&S 
  \%%OO!!!::::::::::::/             S*b `S%%  S*S    S&S  S*S    S*S  S*S    S&S     l*S       S*S       S*b   
   \%OO!!!!::::::::::/              S*S   S%  S*S    S*S  S*S    S*S  S*S    S*S    .S*P       S*S       S*S. 
    ;%%OO!!!!!!:::::'                SS_sSSS  S*S    S*S  S*S    S*S  S*S    S*S  sSS*S        S*S        SSSbs 
     `%%%OO!!!!!!:'                   Y~YSSY  SSS    S*S  S*S    SSS  SSS    S*S  YSS'         S*S         YSSP 
       `%%%OO!%%'                                    SP   SP                 SP                SP  
         `%%%%'                                      Y    Y                  Y                 Y    
          /__\`-.                 =================================================================================
                /                 =================================================================================
               (
                \ 

"""

lose = """
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;                                 .S_sSSs      sSSs   .S_sSSs     .S_sSSs     .S    sSSs  sdSS_SSSSSSbs    sSSs 
        ;:::::;     ;.                               .SS~YS%%b    d%%SP  .SS~YS%%b   .SS~YS%%b   .SS   d%%SP  YSSS~S%SSSSSP   d%%SP
       ,:::::'       ;           OOO                 S%S   `S%b  d%S'    S%S   `S%b  S%S   `S%b  S%S  d%S'         S%S       d%S'  
       ::::::;       ;          OOOOO                S%S    S%S  S%S     S%S    S%S  S%S    S%S  S%S  S%|          S%S       S%S 
       ;:::::;       ;         OOOOOOOO              S%S    d*S  S&S     S%S    d*S  S%S    S&S  S&S  S&S          S&S       S&S 
      ,;::::::;     ;'         / OOOOOOO             S&S   .S*S  S&S_Ss  S&S   .S*S  S&S    S&S  S&S  Y&Ss         S&S       S&S_Ss 
    ;:::::::::`. ,,,;.        /  / DOOOOOO           S&S_sdSSS   S&S~SP  S&S_sdSSS   S&S    S&S  S&S  `S&&S        S&S       S&S~SP
  .';:::::::::::::::::;,     /  /     DOOOO          S&S~YSSY    S&S     S&S~YSY%b   S&S    S&S  S&S    `S*S       S&S       S&S    
 ,::::::;::::::;;;;::::;,   /  /        DOOO         S*S         S*b     S*S   `S%b  S*S    d*S  S*S     l*S       S*S       S*b     
;`::::::`'::::::;;;::::: ,#/  /          DOOO        S*S         S*S.    S*S    S%S  S*S   .S*S  S*S    .S*P       S*S       S*S.    
:`:::::::`;::::::;;::: ;::#  /            DOOO       S*S          SSSbs  S*S    S&S  S*S_sdSSS   S*S  sSS*S        S*S        SSSbs 
::`:::::::`;:::::::: ;::::# /              DOO       S*S           YSSP  S*S    SSS  SSS~YSSY    S*S  YSS'         S*S         YSSP 
`:`:::::::`;:::::: ;::::::#/               DOO       SP                  SP                      SP                SP 
 :::`:::::::`;; ;:::::::::##                OO       Y                   Y                       Y                 Y    
 ::::`:::::::`;::::::::;:::#                OO       =================================================================================
 `:::::`::::::::::::;'`:;::#                O        =================================================================================
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#                                                                                
"""


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
        print("Te quedan", attemps, "vidas ❤️")
        try:
            letter = input("Ingresa una letra y presiona Enter: ").lower()
            assert letter.isalpha(), input("¡Solo se puede ingresar letras! 👀, Presiona la tecla Enter para volver a ingresar un valor.")
            assert len(letter) == 1, input("¡Solo se puede ingresar una letra a la vez! 👀, Presiona la tecla Enter para volver a ingresar un valor.")
        except AssertionError as ae:
            print(ae)
            continue  

        found = False
        for idx, character in enumerate(word_selected):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attemps -= 1

        if "_" not in spaces:
            os.system("clear")
            print(win)
            print("Felicidades!!! encontraste la palabra 🦊", word_selected, "🦊")
            break
            input()

        if attemps == 0:
            os.system("clear")
            print(lose)
            print("Oh oh!!! la palabra que debías adivinar era 😲", word_selected, "😲")
            break
            input()


if __name__ == "__main__":
    run()