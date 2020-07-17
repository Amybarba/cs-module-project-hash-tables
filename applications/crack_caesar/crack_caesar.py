# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
"""
import string

alphabet = [
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
]

# Analyze frequency

freq = {}
total_chars = 0
ciphertext = ""

# Count all the characters
with open("/Users/lambda_school_loaner_110/programming/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt"
          , "r") as f:
    for line in f:
        for char in line:
            # check for uppercase and add those to freq memoization dictionary
            if char in string.ascii_uppercase:
                if char not in freq:
                    freq[char] = 0
                # add one to frequency numeric counter for each time that char appears and then increase total # of chars seen
                freq[char] += 1
                total_chars += 1
        # add to ciphertext string sequence for next step
        ciphertext += line  # Save for decoding later

# Sort by descending frequency
freq_items = list(freq.items())
# This will allow freq_items to be sorted from highest to lowest frequency
freq_items.sort(key=lambda e: e[1], reverse=True)

print("FREQ ITEMS holding frequency list of tuples!!", freq_items, end="\n\n\n")

# Make the key
decode_key = {}
# decode_key will equate first value (freq_items) to the alphabet
for i in range(26):
    decode_key[freq_items[i][0]] = alphabet[i]

# Print the key
print("Decode KEY!", decode_key, end="\n\n\n")

# Decode the text
for c in ciphertext:
    if c in decode_key:
        # this will loop through ciphertext and if the key is in the decode key dictionary, print the value held at that key -- de...ciphering
        print(decode_key[c], end="")
    else:  # print punctuation and spaces etc
        print(c, end="")
        """


def crack_caesar(file):
    c_letters = {}
    letter_freq = {}

    # using https://www.dcode.fr/frequency-analysis with the contents of ciphertext.txt
    letter_freq["E"] = 11.53
    letter_freq["T"] = 9.75
    letter_freq["A"] = 8.46
    letter_freq["O"] = 8.08
    letter_freq["H"] = 7.71
    letter_freq["N"] = 6.73
    letter_freq["R"] = 6.29
    letter_freq["I"] = 5.84
    letter_freq["S"] = 5.56
    letter_freq["D"] = 4.74
    letter_freq["L"] = 3.92
    letter_freq["W"] = 3.08
    letter_freq["U"] = 2.59
    letter_freq["G"] = 2.48
    letter_freq["F"] = 2.42
    letter_freq["B"] = 2.19
    letter_freq["M"] = 2.18
    letter_freq["Y"] = 2.02
    letter_freq["C"] = 1.58
    letter_freq["P"] = 1.08
    letter_freq["K"] = 0.84
    letter_freq["V"] = 0.59
    letter_freq["Q"] = 0.17
    letter_freq["J"] = 0.07
    letter_freq["X"] = 0.07
    letter_freq["Z"] = 0.03

    with open(file) as f:
        data = f.read()
    total_no_of_letters = 0

    for c in data:
        if c.isalpha() and c in c_letters:
            c_letters[c] += 1
            total_no_of_letters += 1
        elif c.isalpha():
            c_letters[c] = 1
            total_no_of_letters += 1

    for letter in c_letters:
        c_letters[letter] = round(
            ((c_letters[letter] / total_no_of_letters) * 100), 2)

    encrypted_letter_freq = list(c_letters.items())
    provided_letter_freq = list(letter_freq.items())

    encrypted_letter_freq.sort(key=lambda x: x[1], reverse=True)
    provided_letter_freq.sort(key=lambda x: x[1], reverse=True)

    encrpt_array = []
    provided_array = []
    for i, (x, z) in enumerate(encrypted_letter_freq):
        encrpt_array.append(x)

    for i, (x, z) in enumerate(provided_letter_freq):
        provided_array.append(x)

    dict_map = dict(zip(encrpt_array, provided_array))

    content = ''

    for i in range(len(data)):
        if data[i].isalpha() and data[i] in dict_map:
            content += dict_map[data[i]]
        else:
            content += data[i]
    print(content)


print(crack_caesar("/Users/lambda_school_loaner_110/programming/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt"))
