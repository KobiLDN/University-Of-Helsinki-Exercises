# Write your solution here

def first_word(sentence):
    fw_space2 = sentence.find(" ")
    sentence = " " + sentence
    fw_space1 = sentence.find(" ")
    # print(fw_space")
    #print(fw_space2)
    return sentence[fw_space1+1:fw_space2+1]

def second_word(sentence):
    sw_space1 = sentence.find(" ")
    sentence = sentence[sw_space1 + 1:]
    if sentence.find(" ") == -1:
        return sentence
    else:
        sw_space2 = sentence.find(" ")
        return sentence[:sw_space2]


def last_word(sentence):
    index = 0
    text = ""

    #check if sentence has only two words
    check = sentence[sentence.find(" ")+1:]

    if check.find(" ") == -1:
        return check
    else:
        for i in sentence:
            index += -1
            text += sentence[index]
            if sentence[index] == " ":
                len(text)
                text = text[0:-1]
                return text[::-1]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))