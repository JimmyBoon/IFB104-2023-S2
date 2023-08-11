# Caesar Cipher walk through:
#
# Write a program that can encode and decode, using the Caesar Cipher method.
# https://en.wikipedia.org/wiki/Caesar_cipher

# Basically we encode a string by changing its position be a certain value
# and decode it by moving back by that value.

# For example: "my house" adjusted by 1, will be "nz ipvtf"

# Hard to read right?

# Plan for the program:
# A: Encoding:
# 1. Convert the letters to numbers
# 2. Add a adjustment value to the number
# 3. Turn the number back into text.

# B: Decoding
# 1. Convert the letters to numbers
# 2. Minus a adjustment value to the number
# 3. Turn the number back into text.

# Variables:
text_to_be_encoded = "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, \
    Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. \
    It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter \
    some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be \
    replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it \
    in his private correspondence."


# # 1.
# # convert the letters into numbers, so we can add the ajustment:
# # print(ord('a'))

# text_to_numbers = []

# for character in text_to_be_encoded:
#     text_to_numbers.append(ord(character))


# # 2. Add a adjustment value to the number
# adjustment = 1

# for index in range(len(text_to_numbers)):
#     text_to_numbers[index] = text_to_numbers[index] + adjustment


# # 3. Turn the number back into text.
# encoded_text_list = []

# for number in text_to_numbers:
#     encoded_text_list.append(chr(number))


# encoded_text = "".join(encoded_text_list)

# print("\n\n")
# print(encoded_text)
# print("\n\n")

def encoder(text_to_encode_arg, adjustment):
    # # 1.
    # convert the letters into numbers, so we can add the ajustment:

    text_to_numbers = []

    for character in text_to_encode_arg:
        text_to_numbers.append(ord(character))


    # 2. Add a adjustment value to the number

    for index in range(len(text_to_numbers)):
        text_to_numbers[index] = text_to_numbers[index] + adjustment


    # 3. Turn the number back into text.
    encoded_text_list = []

    for number in text_to_numbers:
        encoded_text_list.append(chr(number))


    encoded_text = "".join(encoded_text_list)

    return encoded_text

def decoder(text_to_decode_arg, adjustment):
    decode_adjustment = -adjustment
    decoded_text = encoder(text_to_decode_arg, decode_adjustment)
    return decoded_text



print("\n\n")
encoded = encoder(text_to_be_encoded, 1)

print(encoded)

print("\n\n")
decoded = decoder(encoded, 1)

print(decoded)






