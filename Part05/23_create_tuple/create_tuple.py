# Write your solution here
def create_tuple(x: int, y: int, z: int):
    sum = x+y+z
    tups = (x, y, z)
    x = (min(tups))
    y = (max(tups))
    return x, y, sum

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))