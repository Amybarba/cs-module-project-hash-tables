# Your code here
"""
with open("/Users/lambda_school_loaner_110/programming/cs-module-project-hash-tables/applications/histo/robin.txt") as f:
    words = f.read()
    word_split = words.split()

cache = {}

for word in word_split:
    if word not in cache:
        cache[word] = '#'
    else:
        cache[word] += '#'
items = list(cache.items())

items.sort(key=lambda x: x[1], reverse=True)

for key, value in items:
    print(f'{key:<18} {value}')
"""


def word_count(s):
    tr = str.maketrans("", "", '":;,.-+=/\\|[]{}()*^&')
    s = s.translate(tr).lower()

    words = s.split()
    count = {}

    for w in words:
        if w not in count:
            count[w] = 1
        else:
            count[w] += 1

    return count


# Connect the file
with open(
        "/Users/lambda_school_loaner_110/programming/cs-module-project-hash-tables/applications/histo/robin.txt") as f:
    d = f.read()

# Find all the items to count
count = list(word_count(d).items())

# Find the longest word
max_len = 0
for c in count:
    ln = len(c[0])
    if ln > max_len:
        max_len = ln

# Length first, then alpha
count.sort(key=lambda e: (-e[1], e[0]))

for c in count:
    print(f"{c[0]:{max_len}}  ", end="")

    for _ in range(c[1]):
        print(f"#", end="")

    print()
