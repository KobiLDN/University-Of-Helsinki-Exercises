from random import shuffle

def words(n: int, beginning: str):
    list1 = []
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n", "")
            list1.append(word)
    matchedWord = []


    for word in list1:
        if word.startswith(beginning):
            matchedWord.append(word)
    shuffle(matchedWord)
    if len(matchedWord) < n:
        raise ValueError("not enough words")
    newlist = []
    for wordz in matchedWord:
        newlist.append(wordz)
        if len(newlist) == n:
            break
    return newlist
if __name__ == "__main__":
    word_list = words(99993, "ca")
    for word in word_list:
        print(word)