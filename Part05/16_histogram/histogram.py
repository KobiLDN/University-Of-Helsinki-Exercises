# Write your solution here
def histogram(word):
    dict = {}
    for char in word:
        if char not in dict:
           dict[char] = 0
        dict[char] += 1
    for key, value in dict.items():
        print(f"{key} {'*' * value}")

if __name__ == "__main__":
    histogram("abba")

