import difflib

def wordlist():
    words = []
    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())
    return words

words = wordlist()
sentence = input("Write text: ")

incorrectWordsList = {}
for word in sentence.split(' '):
    if word.lower() in words:
        print(word + " ", end="")
    else:
        incorrectWordsList[word] = {}
        print("*" + word + "* ", end="")
        suggestions = difflib.get_close_matches(word, possibilities=words)
        incorrectWordsList[word] = suggestions
print()
print("suggestions:")
for word, suggestions in incorrectWordsList.items():
    print(word+":", ", ".join(suggestions))
wordlist()