# Peppermint Encryption Method #

import os
import time

def text2dict(text):
    text_dict = []
    for char in text:
        text_dict.append(ord(char))
    return text_dict 

def peppermintEncrypt():
    os.system('cls')
    print("PeppermintEncrypt Chosen")
    
    user_cleartext = input("Enter Cleartext: ")
    timenow = int(time.time())
    time_hour = timenow // 3600

    print(text2dict(user_cleartext))
    print(time_hour)

def peppermintDecrypt():
    print("""PeppermintDecrypt not integrated yet, sorry
          🦌⋆꙳•❅*• •*❆ ₊⋆✮⋆˙""")

def peppermint(*x):
    os.system('cls')
    print(*x)
    print("Running Peppermint")
    print("""
⠀⠀⠀⠀⠀⢀⣠⡴⠶⠟⠛⠛⠛⢿⣶⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠛⠛⠶⢦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣴⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣇⠀⠀⠀⠀⠉⠹⣿⣷⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣎⠉⠙⠛⠶⢦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⡇⣀⣠⣀⣀⠀⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡀⠀⠀⠀⠀⠈⢻⣿⣿⣷⡶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠋⠁⠀⠀⠀⠈⠙⠻⣿⠋⠉⠉⠉⠛⠻⠿⣿⣿⣁⡀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⡀⠈⠉⠛⠻⠶⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠶⢦⣤⣄⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠳⠶⣤⣤⣀⡀⠀
⢸⡇⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⣧⣤⣀⡀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣧⠀⠀⠈⠉⢻⡆
⠀⢿⡄⠀⠀⠀⢀⣴⣿⣿⣿⣿⡇⠀⠈⠉⠛⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠶⢶⣼⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠈⡇
⠀⠈⢻⣄⢀⣴⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠶⣦⣤⣀⡀⠀⠀⣼⣿⣿⣿⣿⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠶⢿⣿⣿⣿⡏⠀⠀⠀⢠⡟⠀
⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣁⡀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠳⠶⠶⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠶⢦⣴⠟
1 = Encrpyt
2 = Decrypt
          """)

    user_choice = input("Choice: ")

    if user_choice == "1":
        peppermintEncrypt()
    
    elif user_choice == "2":
        peppermintDecrypt()

    else:
        return peppermint("Invalid Input")
    
if __name__ == "__main__":
    peppermint()
