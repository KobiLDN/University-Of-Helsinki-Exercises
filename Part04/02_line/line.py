# Write your solution here
def line(number, text):
    index = 0
    if text == "":
        print("*" * number)    
    elif index < number:
        for i in range(number):
            print(text[index], end="")
    




# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "%")