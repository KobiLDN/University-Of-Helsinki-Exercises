# Write your solution here
def spruce(size):
    end = size
    print("a spruce!")
    length = size - 1
    height = size + 1
    stars = 1
    white = size - 1
    i = 1
    while i < height:
        i += 1
        print(" " * white + stars * "*")
        white -= 1
        stars += 2
        length += 2
    print(" " * (end-1)+"*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)


#ww*
#w***
#*****
#ww*