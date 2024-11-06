# Peppermint Encryption Method #

import os
import time

def text2list(text):
    #Turns the user's text and puts it into a list, seperated by each character
    text_list = []
    for char in text:
        text_list.append(ord(char))
    return text_list

def decode_separate_32_127(x):
    
    #Figure out how to decode
    pass

def seperate_32_127(x):
    #Seperates a long character string into pieces that are ord() 127 or below but above 32
    result = []
    i = 0
    
    # Loop through the string and extract valid ASCII numbers (32-127)
    while i < len(x):
        # Try extracting 1, 2, or 3 digit numbers from the string
        for length in range(1, 4):  # ASCII codes are 1-3 digits long
            if i + length <= len(x):
                # Try extracting the substring as a number
                num_str = x[i:i+length]
                try:
                    num = int(num_str)
                    if 32 <= num <= 127:
                        result.append(num)
                        i += length  # Move past the current valid number
                        break
                except ValueError:
                    continue
        else:
            i += 1  # If no valid number found, skip by 1

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

    peppermint_encoded_list = seperate_32_127(single_element)

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

    ciphertext = (input("Please enter the ciphertext: \n"))

    time_code = (input("Please enter code: \n"))

    ascii_values = [ord(char) for char in ciphertext]

    combined_list = []
    time_code_split = [int(num) for num in time_code]
    
    longer_list = ascii_values if len(ascii_values) >= len(time_code_split) else time_code_split
    shorter_list = time_code_split if len(ascii_values) >= len(time_code_split) else ascii_values

    # Rebuild the combined list by alternating the values
    for i in range(len(longer_list)):
        combined_list.append(longer_list[i])
        combined_list.append(shorter_list[i % len(shorter_list)])

    combined_list_str = ''.join(str(i) for i in combined_list)

    decoded_ascii = decode_separate_32_127(combined_list_str)
    
    # Convert the list of ASCII values back into characters
    decrypted_text = ''.join(chr(num) for num in decoded_ascii)

    # Output the decrypted text
    print(f"Decrypted Text: \n{decrypted_text}")
    print("""Thank you for using Peppermint
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
