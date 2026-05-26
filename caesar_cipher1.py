def kamala(text,shift):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet=alphabet[shift:]+alphabet[:shift]
    translation_table=str.maketrans(alphabet+alphabet.upper(),shifted_alphabet+shifted_alphabet.upper())
    #text='Hello guys'
    encrypted_text=text.translate(translation_table)
    print(text)
    return encrypted_text
print(kamala('Rajabu',5))