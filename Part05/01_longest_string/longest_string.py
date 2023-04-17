def longest(strings):
    longest = ""
    for current_word in strings:
        if len(current_word) > len(longest):
            longest = current_word
    return longest


if __name__ == "__main__":
    strings = ["first", "second", "third"]
    print(longest(strings))