# imports
import string

# variables
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
msg = ""
key = 0
index = []
output = ""

# user input
msg = input("Type message to decrypt > ")
key = int(input("Type key > "))

# message as index numbers of chars
for x in msg:
    for y in chars:
        if x == y:
            index.append(chars.index(y))

# decrypt
for x in index:
    output += chars[x - key]

# finish 
print("Message decrypted.")
input("Press enter to see decrypted message. ")
print("Your message > " + output)
