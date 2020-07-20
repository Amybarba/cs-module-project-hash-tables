
# python does not accept \| so add \
ignore_each = (":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\"")


def word_count(s):
    # Your code here
    for each in ignore_each:
        s = s.replace(each, "")
    s = s.lower().split()
    word_list = {}
    if len(s) == 1 and s[0] == "":
        return {}
    for word in s:
        if word not in word_list:
            word_list[word] = 1
        else:
            word_list[word] += 1
    return word_list


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))