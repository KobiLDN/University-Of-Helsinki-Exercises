def readfile():
    open('correct.csv', 'w').close()
    open('incorrect.csv', 'w').close()
    list1 = []
    with open("solutions.csv") as solutions:
        for solution in solutions:
            solution = solution.replace("\n", "")
            parts = solution.split(";")
            list1.append(parts)
    return list1

def filter_solutions():
    file = readfile()
    for name, maths1, result in file:
        if "-" in maths1:
            e = maths1.split("-")
            res = int(e[0]) - int(e[1])
        if "+" in maths1:
            e = maths1.split("+")
            res = int(e[0]) + int(e[1])
        if int(result) == res:
            with open("correct.csv", "a") as correct:
                genius = f"{name};{maths1};{result}"
                correct.write(genius + "\n")
        if int(result) != res:
            with open("incorrect.csv", "a") as incorrect:
                idiot = f"{name};{maths1};{result}"
                incorrect.write(idiot + "\n")

if __name__ == "__main__":
    filter_solutions()
