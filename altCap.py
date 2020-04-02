import sys

if len(sys.argv) < 2:
    string_input = input("Enter a string: ")
    sys.argv.append(string_input)

sys.argv.pop(0)
args = ' '.join(sys.argv)

lowercase_first = ""
uppercase_first = ""

lower_true_upper_false = True

## This does not count for spaces and will not flip
for char in args:
    if char.isalnum():
        if lower_true_upper_false:
            lowercase_first += char.lower()
            uppercase_first += char.upper()
        else:
            lowercase_first += char.upper()
            uppercase_first += char.lower()
        lower_true_upper_false = not lower_true_upper_false
    else:
        lowercase_first += char
        uppercase_first += char

    ## This counts for spaces and flips the capitalization of whitespace character
    # if i % 2 == 0:
    #     lowercase_first += args[i].lower()
    #     uppercase_first += args[i].upper()
    # else:
    #     lowercase_first += args[i].upper()
    #     uppercase_first += args[i].lower()

print("Lowercase first:", lowercase_first)
print("Uppercase first:", uppercase_first)