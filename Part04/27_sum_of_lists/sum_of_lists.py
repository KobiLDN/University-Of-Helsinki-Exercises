# Write your solution here
def list_sum(a, b):
    newlist = []
    for i in range(len(a)):
        newlist.append(a[i] + b[i])
    return newlist


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))