import sys
import random

if len(sys.argv) < 2:
    string_input = input("Enter a string: ")
    sys.argv.append(string_input)

sys.argv.pop(0)
args = ' '.join(sys.argv)

def randCap(args):
    randCap = ""

    for char in args:
        if char.isalnum():
            if random.randint(0,1) < 0.5:
                randCap += char.upper()
            else:
                randCap += char.lower()
        else:
            randCap += char
    return randCap


for i in range(5):
    print("Randomized capitalization ", i, ": ", randCap(args), sep="")