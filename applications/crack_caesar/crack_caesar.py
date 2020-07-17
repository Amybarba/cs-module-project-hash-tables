# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

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

