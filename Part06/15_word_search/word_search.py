# Write your solution here
def find_words(search_term: str):
    found = []
    word_list = []
    with open("words.txt") as word_file:
        for word in word_file:
            word = word.replace("\n", "")
            word_list.append(word)
        if search_term.startswith("*") or search_term.endswith("*"):
            found = asterisk(search_term, word_list)
        elif search_term.find(".") != -1:
            found = searchDot(search_term, word_list)
        else:
            found = searchNormal(search_term, word_list)
    return found

def asterisk(search_term, word_list): #search for wildcards
    found = []
    if search_term.startswith("*"):
        for word in word_list:
            if word.endswith(search_term[1:]):
                found.append(word)
        # print(found)
        # found = []
    elif search_term.endswith("*"):
        for word in word_list:
            if word.startswith(search_term[:-1]):
                found.append(word)
    return found

def searchNormal(search_term, word_list):
    found = []
    if search_term in word_list:  # check the wordlist and return search term if no wildcards are given
        found.append(search_term)
    return found

def searchDot(search_term, word_list):
    found = []
    search_termIndex = 0
    matchedword = ""
    for word in word_list:
        if len(search_term) == len(word):
            for char in word:
                if len(matchedword) == len(search_term):  # does the length of matched word = len search term
                    if matchedword == search_term:
                        found.append(word)
                        matchedword = ""
                        search_termIndex = 0
                    matchedword = ""
                    search_termIndex = 0
                    continue
                if char != search_term[search_termIndex]:  # does letter of word match letter of search word
                    matchedword += "."
                    if len(matchedword) == len(search_term):  # does the length of matched word = len search term
                        if matchedword == search_term:
                            found.append(word)
                            matchedword = ""
                            search_termIndex = 0
                        matchedword = ""
                        search_termIndex = 0
                        continue
                    search_termIndex += 1
                    continue
                matchedword += char  # the letters match so we add to the matched word
                search_termIndex += 1
                if len(matchedword) == len(search_term):  # does the length of matched word = len search term
                    if matchedword == search_term:
                        found.append(word)
                        matchedword = ""
                        search_termIndex = 0
                    matchedword = ""
                    search_termIndex = 0
                    continue
    return found

if __name__ == "__main__":
    print(find_words(".a."))