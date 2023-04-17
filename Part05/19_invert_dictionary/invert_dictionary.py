# Write your solution here
def invert(dict1: dict):
    helper = dict1.copy()
    for key, value in helper.items():
        dict1.pop(key)
        dict1[value] = key

if __name__ == "__main__":
    invert({1: 100})