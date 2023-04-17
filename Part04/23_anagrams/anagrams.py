# Write your solution here
def anagrams(string1: str, string2: str):
    # print(sorted(word1))
    # print(sorted(word2))
    return sorted(string1) == sorted(string2)        

if __name__ == "__main__":
    anagrams("tame", "meta")