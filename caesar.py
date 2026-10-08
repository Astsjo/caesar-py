alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
resultat = ""
letter=""
encrypted_message = ""
space=""
message="hej"
key = 1

for letters in range(len(message)):
    try:
        letter = message[letters]
        position = alfabet.index(letter)
        encryption = (position + key) % len(alfabet)
        resultat = alfabet[encryption]
        encrypted_message += resultat
    except ValueError:
        encrypted_message += " "

print(encrypted_message)