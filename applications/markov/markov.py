"""import random

# Read in all the words in one go
with open(
        "/Users/lambda_school_loaner_110/programming/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read()
    pick = words.split()


# TODO: analyze which words can follow other words
# Your code here
def make_follow(list):
    for i in range(len(list) - 1):
        yield list[i], list[i + 1]


pairs = make_follow(pick)
word_list = {}

for first_word, second_word in pairs:
    if first_word in word_list.keys():
        word_list[first_word].append(second_word)
    else:
        word_list[first_word] = [second_word]

f_word = random.choice(pick)
s_word = random.choice(pick)

while f_word.islower() and f_word[0] != '"':
    f_word = random.choice(pick)

while s_word[-1] not in ['.', '!', '?']:
    s_word = random.choice(pick)

# TODO: construct 5 random sentences
# Your code here

first = [f_word]
second = [s_word]

word_count = 150

for i in range(word_count):
    first.append(random.choice(word_list[first[-1]]))

    print(''.join(first + second))
    """
import random

with open(
        "/Users/lambda_school_loaner_110/programming/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read()
    list = words.split()
    second_words = {}

prev = None

for end in list:
    if prev is not None:

        if prev not in second_words:
            second_words[prev] = []
        second_words[prev].append(end)

    prev = end

new_sentence = lambda x: x[0].isupper() or len(x) > 1 and x[1].isupper()
first_word = [end for end in second_words.keys() if new_sentence(end)]

for _ in range(5):
    end = random.choice(first_word)

    stopped = False
    punctuation_marks = ".!?"  # Stop on any of these punctuation marks

    while not stopped:
        print(end, end=" ")
        if end[-1] in punctuation_marks or len(end) > 1 and end[-2] in punctuation_marks:
            stopped = True
        else:
            # Follow to the next word in the chain
            next_words = second_words[end]
            end = random.choice(next_words)

    print("\n")
