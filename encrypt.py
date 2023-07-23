# imports 
import string 
import random

# variables 
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
msg = ""
index = []
output = ""
keyType = 0
key = 0
entered = False
rand = False

#input message
msg = input("Type message to encrypt > ")

# message as index numbers of chars
for x in msg:
    for y in chars:
        if x == y:
            index.append(chars.index(y))

#create key
while True:
    keyType = int(input("Would you like to (1) use your own key, or (2) generate a random key > "))
    if keyType == 1:
        while True:
            key = int(input("Please enter your key (must be between 0 and 93 inclusive) > "))
            if key > 93 or key < 0:
                print("Invalid key.\n")
                input("Press enter to try again.\n")
            else:
                break
        break
    elif keyType == 2:
        key = random.randint(0, 93)
        rand = True
        break

    else:
        print("Invalid input.\n")
        input("Press enter to try again.\n")

#encrypt message
for x in index:
    if (x + key) >= len(chars):
        wrap = (x + key) - len(chars)
        output += chars[wrap]
    else:
        output += chars[x + key]

#finish 
print("Message encrypted.")
input("Press enter to see encrypted message.")
print("Your encrypted message > " + output)
if rand == True: 
    input("Press enter to view key used.")
    print("Your key > " + str(key))