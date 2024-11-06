# Peppermint Encryption Method #

import os
import time

def text2dict(text):
    text_dict = []
    for char in text:
        text_dict.append(ord(char))
    return text_dict

def seperate_under_127(x):
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
    os.system('cls')
    print("PeppermintEncrypt Chosen")
    
    user_cleartext = input("Enter Cleartext: ")
    timenow = int(time.time())
    time_hour = timenow // 3600
    time_hour_split = []
    for num in str(time_hour):
        time_hour_split.append(num)

    combined_list = []

    TextInDict = text2dict(user_cleartext)

    longer_list = TextInDict if len(TextInDict) >= len(time_hour_split) else time_hour_split
    shorter_list = time_hour_split if len(TextInDict) >= len(time_hour_split) else TextInDict

    for i in range(len(longer_list)):
            combined_list.append(longer_list[i])
            combined_list.append(shorter_list[i % len(shorter_list)])

    combined_list_str = []

    for i in combined_list:
        combined_list_str.append(str(i))

    single_element = ''.join(combined_list_str)

    peppermint_encoded_list = seperate_under_127(single_element)

    ciphertext_str = [chr(num) for num in peppermint_encoded_list]

    ciphertext = ''.join(ciphertext_str)

    print(f"Save the code: {time_hour}")
    print(f"Your Ciphertext: \n {ciphertext}")

def peppermintDecrypt():
    
    os.system('cls')
    print("PeppermintDecrypt Chosen")

    user_ciphertext_list_ord = []

    user_ciphertext = (input("Please enter the ciphertext: \n"))

    user_code = (input("Please enter code: \n"))

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
