def caesar_encrypt(message, key):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    resultat = ""
    letter=""
    encrypted_message = ""
    space=""

    for letters in range(len(message)):
        letter = message[letters]
        position = alfabet.index(letter)
        encryption = (position + key) % len(alfabet)
        resultat = alfabet[encryption]
        encrypted_message += resultat

    print(encrypted_message)

caesar_encrypt("hej", 1)