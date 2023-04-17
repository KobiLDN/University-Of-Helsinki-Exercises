def filter_incorrect():
    with open("lottery_numbers.csv") as file:
        lotto = []
        index = 0
        error = False
        for data in file:
            data = data.replace("\n", "")
            parts = data.split(";")
            weekNumber = parts[0][4:]
            lottoNums = parts[1].split(",")
            weeks = parts[0]

            #check the numbers are correct

            if len(lottoNums) != 7:                                  # check Too few numbers:
                #error = True
                continue
            try:
                for numbers in lottoNums:                                # One or more numbers are not correct:
                    if not int(numbers):
                        error = True
                        break
                    if int(numbers) < 0 or int(numbers) > 39:                # The numbers are too small or large:
                        error = True
                        break
                copy = lottoNums[:]
                for number in lottoNums:                               #The same number appears twice:
                    copy.remove(number)
                    if number in copy:
                        error = True
                        break
                if int(weekNumber):
                    if error:
                        error = False
                        continue                            # The week number is incorrect:
                    lotto.append([weeks])
                    for number in lottoNums:
                        lotto[index].append(number)
                index += 1
            except:
                pass
    print(lotto)
    with open("correct_numbers.csv", "w") as correct_file:
        for weeklynumbers in lotto:
            correct_file.write(weeklynumbers[0]+";"+','.join(weeklynumbers[1:]))
            correct_file.write("\n")


if __name__ == "__main__":
    filter_incorrect()