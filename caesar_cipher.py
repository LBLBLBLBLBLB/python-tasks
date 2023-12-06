letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt, 'decode' to decrypt: \n")
text = input("type your message: \n").lower()
shift = int(input("type the shift number: \n"))


def caesar(plain_text, shift_amount, cipher_direction):
    final_text = ""
    for i in plain_text:
        position = letters.index(i)

        if cipher_direction == 'encode':
            new_position = position + shift_amount
        else:
            new_position = position - shift_amount

        new_letter = letters[new_position]
        final_text += new_letter
    print(f"the {cipher_direction}d text is {final_text}")


caesar(text,shift,direction)
