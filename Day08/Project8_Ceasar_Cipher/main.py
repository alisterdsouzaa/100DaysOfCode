# This project will encode and decode your text with the shifting number chosen

'''
    +-------------------------------------------------------------+
    |    Author : Alister D'souza                                 |
    |    Date   : 12/07/2023                                      |
    |    Contact: @alisterdsouzaa                                 |
    |    .py   : Small project on ceasar cipher  				  |
    +-------------------------------------------------------------+
'''
import sys

from logo import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
while direction != "encode" and direction != "decode":
    print("invalid direction, try again")
    sys.exit()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(plain_text, shift_amount, direction):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
            # print(f"{cipher_text} is the encoded text")
        elif direction == "decode":
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
            # print(f"{cipher_text} is the decoded text")

    print(f"{cipher_text} is the decoded text")


ceasar(plain_text=text, shift_amount=shift, direction=direction)

#  Encoding function
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"{cipher_text} is the encoded text")
#
#
# # Decrypting logic
# def decrypt(encoded_message, shift_amount):
#     de_cipher_text = ""
#     for letter in encoded_message:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         de_cipher_text += new_letter
#     print(f"The decoded text is {de_cipher_text}")
