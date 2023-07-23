type = 0
decryptType = 0

print("Hello. This program will encrypt or decrypt a message for you.")
while True:
    type = int(input("Would you like to (1) encrypt a message, or (2) decrypt a message > "))
    if type == 1:
        with open("encrypt.py") as f:
            exec(f.read())
        break
    elif type == 2:
        while True:
            decryptType = int(input("Would you like to (1) decrypt a message with a known key, or (2) generate all possible decrypts for your key > "))
            if decryptType == 1:
                with open("decryptKnownKey.py") as f:
                    exec(f.read())
                break
            elif decryptType == 2:
                with open("decryptAllPossible.py") as f:
                    exec(f.read())
                break
            else: 
                input("Invalid input.\nPress enter to continue. ")
        break
    else:
        input("Invalid input.\nPress enter to continue. ")