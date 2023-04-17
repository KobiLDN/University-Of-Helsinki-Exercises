# Copy here code of line function from previous exercise and use it in your solution
def line(size1, character, size2, character2):
    start = 0
    end = 1
    if character == "":
        character = "*"
    tri = character[0] * size1
    while end <= size1:
        print(tri[start:end])
        end += 1
    for i in range(size2):
        print(character2[0] * size1)

def shape(size1, character, size2, character2):
# You should call function line here with proper parameters
    line(size1, character, size2, character2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")