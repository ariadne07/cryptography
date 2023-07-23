# imports 
import string

#variables
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
possibleKey = 0
output = ""

#functions
def tryIt():
    global output
    output = ""
    for x in index:
        output += chars[x - possibleKey]
    return output 

#program 
msg = input("Type message to decrypt > ")
input("Press enter to generate all possibilities. ")

#make msg integer list 
index = []
for x in msg:
    for y in chars:
        if x == y:
            index.append(chars.index(y))

# cylcle through possible keys 
while possibleKey < len(chars):
    print("Key #" + str(possibleKey) + ": " + tryIt())
    possibleKey += 1

