import os
import pyfiglet
import platform
from modules.colora import cyan, green, red, magenta, yellow

def clear():
    operating_system = platform.system()

    if operating_system == 'Windows':
        os.system('cls')
    elif operating_system == 'Linux':
        os.system('clear')

def banner():
    banner_text = pyfiglet.figlet_format('Caesar Cipher', font='big')

    print(magenta('-')*67)
    print(cyan(banner_text))
    print(red('by Diogo S. Lourenco'))
    print(magenta('-')*67)
    print()

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                if mode == 'encode':
                    result += chr((ord(char) - ord('a') + int(shift)) % 26 + ord('a'))
                elif mode == 'decode':
                    result += chr((ord(char) - ord('a') - int(shift)) % 26 + ord('a'))
            elif char.isupper():
                if mode == 'encode':
                    result += chr((ord(char) - ord('A') + int(shift)) % 26 + ord('A'))
                elif mode == 'decode':
                    result += chr((ord(char) - ord('A') - int(shift)) % 26 + ord('A'))
        else:
            result += char
    return result

def decode_with_specific_shift(text):
    clear()
    banner()
    print(yellow("Original sentence: "), text)
    shift = input(yellow("\nEnter the shift value for decoding: "))
    result = caesar_cipher(text, shift, 'decode')
    clear()
    banner()
    print(yellow(f"ORIGINAL SENTENCE:            {text}"))
    print()
    print(green(f"DECODED SENTENCE WITH SHIFT {red(shift)}: "), result)

    print()
    print(magenta('-')*67)
    print()

    input("\nPress Enter to continue...")

def decode_within_range(text):
    clear()
    banner()
    print(yellow("ORIGINAL SENTENCE: "), text)
    start = int(input(yellow("\nEnter the start value of the range: ")))
    end = int(input(yellow("Enter the end value of the range: ")))
    
    print(yellow("\nDecoding for shift values within range: \n"))
    for value in range(start, end + 1):
        result = caesar_cipher(text, value, 'decode')
        print(green(f"SHIFT VALUE {value}: "), result)
        print()
    
    input("\nPress Enter to continue...")

def decode_all_shifts(text):
    clear()
    banner()
    print(yellow("ORIGINAL SENTENCE: "), text)
    print(yellow("\nDecoding for shift values from 1 to 26: \n"))
    for value in range(1, 26+1):
        result = caesar_cipher(text, value, 'decode')
        print(green(f"SHIFT VALUE {value}: "), result)
        print()

    input("\nPress Enter to continue...")

def menu():
    clear()
    banner()
    print(green('1 - Encode\n2 - Decode\n3 - Exit'))
    print(green("\nChoose an option [1][2][3]: "))
    option = input("$ ")
    return option

def main():
    while True:
        choice = menu()

        if choice == '1':
            clear()
            banner()
            print(yellow("Enter the sentence to encode: "))
            text = input("$ ")
            print()
            print(yellow("Shift value: "))
            shift = input("$ ")
            result = caesar_cipher(text, shift, 'encode')
            clear()
            banner()
            print(yellow("ORIGINAL SENTENCE: "), text)
            print()
            print(green("ENCODED SENTENCE: "), result)
            
            print()
            print(magenta('-')*67)
            print()

            input("Press Enter to continue...")
        elif choice == '2':
            clear()
            banner()
            print(yellow("Enter the sentence to decode: "))
            text = input("$ ")

            print()
            print(magenta('-')*67)

            print(yellow("\nDecoding options:\n"))
            print(yellow('1 - Choose a specific shift value\n2 - Choose a range\n3 - Decode with all shift values from 1 to 26'))
            print(yellow("\nChoose an option [1][2][3]: "))
            decode_option = input("$ ")
            
            if decode_option == '1':
                decode_with_specific_shift(text)
            elif decode_option == '2':
                decode_within_range(text)
            elif decode_option == '3':
                decode_all_shifts(text)
            else:
                print("Invalid option. Please try again.")
        elif choice == '3':
            clear()
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
