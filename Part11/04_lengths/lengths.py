# WRITE YOUR SOLUTION HERE:
# stringx = [str(number) for number in numbers]
# [<expression> for <item> in <series>]

def lengths(lists: list):
    return [len(list) for list in lists]

    # for list in lists:
    #     print(len(list))

if __name__ == "__main__":

    lists = [[1, 2, 3, 4, 5], [324, -1, 31, 7], []]
    print(lengths(lists))