def factorials(n):
    dic = {}
    start = 1
    for i in range(1, n+1):
        start *= i
        dic[i] = start
    return dic

if __name__ == "__main__":

    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[4])
    print(k[5])

#1 - 1x1 = 1 - 1            - 1/1
#2 - 2x1 = 2 - 1            - 2/2
#3 - 3x2x1 = 6 - 2          - 6/3
#4 - 4x3x2x1 = 24 - 6       - 24/4
#5 - 5x4x3x2x1 = 120 - 24   - 120/5

# number i fact
#n =  i *
#2 = 1 * 1
#3 = 2 * 3
#4 = 3 * 8
#5 = 4 * 24
#6 = 5 * 120