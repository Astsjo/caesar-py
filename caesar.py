def caesar_encrypt(message, key):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    resultat = ""
    letter=""
    encrypted_message = ""
    space=""

    for letters in range(len(message)):
        try:
            letter = message[letters]
            position = alfabet.index(letter)
            encryption = (position + key) % len(alfabet)
            resultat = alfabet[encryption]
            encrypted_message += resultat
        except ValueError:
            encrypted_message += " "

    return encrypted_message

def caesar_decrypt(message, key):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    resultat = ""
    letter=""
    decrypted_message = ""
    space=""

    for letters in range(len(message)):
        try:
            letter = message[letters]
            position = alfabet.index(letter)
            encryption = (position - key) % len(alfabet)
            resultat = alfabet[encryption]
            decrypted_message += resultat
        except ValueError:
            decrypted_message += " "

    return decrypted_message

user_input = input("Fras: ").lower()
while True:
    keys = input("Nyckel: ")
    try:
        keys = int(keys)
        break
    except ValueError:
        print("Vänligen ange ett tal.")

while True:
    crypt = input("(1) Kryptera eller (2) Avkryptera: ")
    try:
        crypt = int(crypt)
        break
    except ValueError:
        print("Vänligen välj ett alternativ.")

if crypt == 1:
    encrypted_message = caesar_encrypt(user_input, keys)
    print(encrypted_message)
elif crypt == 2:
    decrypted_message = caesar_decrypt(user_input, keys)
    print(decrypted_message)
else:
    print("Du valde inget alternativ. Avslutar...")