def add_zero(layers):
    renumber = []
    renumber.append([])
    renumber[0].append(f"{layers}")
    return str(renumber[0][0])


def layers(layers):
    if layers <10:
        topRow = layers + (layers - 1)
        one = "1"
        zero = "0"
        index1 = 2
        index0 = 1
        one_zeros = 0
        end = 0
        store = []
        for i in range(layers):
            # prints the top row
            if i == 0:
                start = (topRow * str(layers))
                #letters(str(start))
                #print(start)
                start = int(start)
                sum = start
                for j in range(topRow):
                    store.append(str(layers))
                letters(store)
                store = []
                continue
            # when to end

            if end == start:
                break

            one_zeros = int(one*(topRow-index1)+zero*index0)
            sum -= one_zeros
            #print(str(sum))
            #letters(str(sum))
            for j in str(sum):
                store.append(str(j))
            letters(store)
            store = []
            topRow -= 2
            index0 += 1
            if i == int(layers-1):
                index1 = 0
                for j in range(int(layers-1)):
                    index0 -= 1
                    one_zeros = int(one * (topRow + index1) + zero * index0)
                    sum += one_zeros
                    for j in str(sum):
                        store.append(str(j))
                    letters(store)
                    store = []
                    end = sum
                    topRow += 2
                    #print(str(sum))
                    #letters(str(sum))
    if layers > 9:
        topRow = layers + (layers - 1)
        one = "10"
        zero = "0"
        index1 = 2
        index0 = 1
        one_zeros = 0
        end = 0
        store = []
        layers = add_zero(layers)
        layers = int(layers)
        for i in range(layers):
            # prints the top row
            if i == 0:
                start = (topRow * str(layers))
                #letters(str(start))
                #print(start)
                start = int(start)
                sum = start
                for j in range(topRow):
                    store.append(str(layers))
                lettersOver10(store)
                store = []
                renumber = []
                continue
            # when to end

            if end == start:
                break

            one_zeros = int(one*(topRow-index1)+zero*index0)
            sum -= one_zeros
            sum_str = str(sum)
            i1 = 0
            i2 = 2
            for index3 in range(layers + (layers - 1)):
                store.append(sum_str[i1:i2])
                i1 += 2
                i2 += 2
            lettersOver10(store)
            #print(str(sum))
            #letters(str(sum))
            #letters(store)
            store = []
            topRow -= 2
            index0 += 2
            if i == int(layers-1):
                index1 = 0
                for j in range(int(layers-1)):
                    index0 -= 2
                    one_zeros = int(one * (topRow + index1) + zero * index0)
                    sum += one_zeros
                    sum_str = str(sum)
                    i1 = 0
                    i2 = 2
                    for index3 in range(layers + (layers - 1)):
                        store.append(sum_str[i1:i2])
                        i1 += 2
                        i2 += 2
                    lettersOver10(store)
                    store = []
                    end = sum
                    topRow += 2
                    #print(str(sum))
                    #letters(str(sum))

def letters(convert):
    dictionary = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E",
                  "6": "F", "7": "G", "8": "H", "9": "I", "10": "J",
                  "11": "K", "12": "L", "13": "M", "14": "N", "15": "O",
                  "16": "P","17": "Q", "18": "R","19": "S", "20": "T",
                  "21": "U", "22": "V", "23": "W", "24": "X", "25": "Y", "26": "Z"}
    for i in convert:
        print(dictionary[i], end="")
    print()

def lettersOver10(convert):
    dictionary = {"01": "A", "02": "B", "03": "C", "04": "D", "05": "E",
                  "06": "F", "07": "G", "08": "H", "09": "I", "10": "J",
                  "11": "K", "12": "L", "13": "M", "14": "N", "15": "O",
                  "16": "P","17": "Q", "18": "R","19": "S", "20": "T",
                  "21": "U", "22": "V", "23": "W", "24": "X", "25": "Y", "26": "Z"}
    for i in convert:
        print(dictionary[i], end="")
    print()

inputLayer = int(input("Layers: "))
layers(inputLayer)
#layers(10)


# 4444444 # 4*7
# 4333334 # 4*1, 3*5, 4*1
# 4322234 # 4*1, 3*1, 2*3, 3*1, 4*1
# 4321234 # 4*1, 3*1, 2*1, 3*1, 4*1
# 4322234 # 4*1, 3*1, 2*3, 3*1, 4*1
# 4333334 # 4*1, 3*5, 4*1
# 4444444 # 4*7

# 4444444 # 1111111
# 4333334 #
# 4322234 #
# 4321234 #
# 4322234 #
# 4333334 #
# 4444444 #

# 4*7 4*1 4*1 4*1 4*1 4*1 4*7
#     3*5 3*1 3*1 3*1 3*5
#     4*1 2*3 2*1 2*3 4*1
#         3*1 3*1 3*1
#         4*1 4*1 4*1

# 3 + (3-1) = 5
# 33333 = 11111 =   1*5
# 32223 = 1110  =   1*3     0*1
# 32123 = 100   =   1*1     0*2
# 32223 = 100   =   1*1     0*2
# 33333 = 1110  =   1*3     0*1

# 4+ (4-1) = 7
# 4444444 = 1111111 = 1*7
# 4333334 = 111110  = 1*5   0*1
# 4322234 = 11100   = 1*3   0*2
# 4321234 = 1000    = 1*1   0*3
# 4322234 = 1000    = 1*1   0*3
# 4333334 = 11100   = 1*3   0*2
# 4444444 = 111110  = 1*5   0*1

#	10 + (10-1) = 19
# 10101010101010101010101010101010101010	=	1111111111111111111 = 1*19 
# 10090909090909090909090909090909090910	=	10101010101010101010101010101010100 	10*17 	0*1
# 10090808080808080808080808080808080910	= 	101010101010101010101010101010000 		10*15 	0*3
# 10090807070707070707070707070707080910  = 	1010101010101010101010101000000 		10*13 	0*5
# 10090807060606060606060606060607080910	=	10101010101010101010100000000 			10*11 	0*7
# 10090807060505050505050505050607080910	= 	101010101010101010000000000 			10*9 	0*9 	 
# 10090807060504040404040404050607080910	=	1010101010101000000000000				10*7 	0*11 
# 10090807060504030303030304050607080910	=	10101010100000000000000					10*5 	0*13
# 10090807060504030202020304050607080910  =	101010000000000000000 					10*3 	0*15
# 10090807060504030201020304050607080910	= 	1000000000000000000 					10*1 	0*17
# 10090807060504030202020304050607080910	=  	1000000000000000000 					10*1 	0*17
# 10090807060504030303030304050607080910 	= 	101010000000000000000 					10*3 	0*15
# 10090807060504040404040404050607080910
# 10090807060505050505050505050607080910
# 10090807060606060606060606060607080910
# 10090807070707070707070707070707080910
# 10090808080808080808080808080808080910
# 10090909090909090909090909090909090910
# 10101010101010101010101010101010101010