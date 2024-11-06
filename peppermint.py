# Peppermint Encryption Method #

import os
import time

def text2list(text):
    #Turns the user's text and puts it into a list, seperated by each character
    text_list = []
    for char in text:
        text_list.append(ord(char))
    return text_list

def seperate_under_127(x):
    #Seperates a long character string into pieces that are ord() 127 or below
    result = []
    i = 0

    while i < len(x):
        number = 0
        for j in range(i, len(x)):
            next_number = int(x[i:j+1])
            if next_number <= 127:
                number = next_number
            else:
                break
        result.append(number)

        i += len(str(number))
    
    return result
    
def peppermintEncrypt():
    # Prepares the terminal for Encrypting!
    os.system('cls')
    print("PeppermintEncrypt Chosen")
    
    # Obtains cleartext from user & converting the time into a 6-digit code

    user_cleartext = input("Enter Cleartext: ")
    timenow = int(time.time())
    time_hour = timenow // 3600
    time_hour_split = []
    for num in str(time_hour):
        time_hour_split.append(num)

    # Creates a new list where the two lists (cleartext & 6-digit time code) will be combined, 
    # via alternating and the shorter list being repeated when there are insufficient characters
    combined_list = []

    TextInList = text2list(user_cleartext)

    longer_list = TextInList if len(TextInList) >= len(time_hour_split) else time_hour_split
    shorter_list = time_hour_split if len(TextInList) >= len(time_hour_split) else TextInList

    for i in range(len(longer_list)):
            combined_list.append(longer_list[i])
            combined_list.append(shorter_list[i % len(shorter_list)])

    combined_list_str = []

    for i in combined_list:
        combined_list_str.append(str(i))

    single_element = ''.join(combined_list_str)

    peppermint_encoded_list = seperate_under_127(single_element)

    # Turns the new string values into ASCII text

    ciphertext_str = [chr(num) for num in peppermint_encoded_list]

    ciphertext = ''.join(ciphertext_str)

    print(f"Save the code: {time_hour}")
    print(f"Your Ciphertext: \n {ciphertext}")
    print("""Thank you for using Peppermint
          🦌⋆꙳•❅*• •*❆ ₊⋆✮⋆˙""")

def peppermintDecrypt():
    # Prepares the terminal for Peppermint Decryption!
    os.system('cls')
    print("PeppermintDecrypt Chosen")

    user_ciphertext_list_ord = []

    user_ciphertext = (input("Please enter the ciphertext: \n"))

    user_code = (input("Please enter code: \n"))

    # Seperates the characters in the encoded text

    for char in user_ciphertext:
        user_ciphertext_list_ord.append(ord(char))

    print(user_ciphertext_list_ord) 
    print(user_code) 

    #print("""PeppermintDecrypt not integrated yet, sorry
          #🦌⋆꙳•❅*• •*❆ ₊⋆✮⋆˙""")

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
