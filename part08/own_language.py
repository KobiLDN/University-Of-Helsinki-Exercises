import string



def run(program):
    variables_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                      'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
                      'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    print_list = []
    operations = ["MOV", "ADD", "SUB", "MUL", "PRINT", "IF", "JUMP"]
    dict_save_slots = {}
    count_saves = 0
    for j in program:
        j = j.split(" ")
        if j[0] not in operations:
            dict_save_slots[j[0][:-1]] = int(count_saves)
        count_saves += 1
    count = 0
    save_slot = 0
    while count < len(program):
        x = program[count]
        x = x.split(" ")
        if x[0] == "JUMP":
            #count = save_slot
            count = dict_save_slots[x[1]]    # checks dictionary key for where to start from
            continue
        if x[0] not in operations :    #save slot
            save_slot = count
            dict_save_slots[x[0][:-1]] = count
            count += 1
            continue
        if x[0] == "IF":
            statment1 = x[0]
            variable1 = x[1]
            operator1 = x[2]
            variable2 = x[3]
            command2 = x[4]
            command3 = x[5]
            if operator1 == "<":
                if variable2 in string.ascii_uppercase:
                    if variables_dict[variable1] < variables_dict[variable2]:
                        count = dict_save_slots[command3]
                        count += 1
                        continue
                    count += 1
                    continue
                elif variables_dict[variable1] < int(variable2):
                    count = dict_save_slots[command3]
                    count += 1
                    continue
                else:
                    count += 1
                    continue
            if operator1 == ">":
                if variable2 in string.ascii_uppercase:
                    if variables_dict[variable1] > variables_dict[variable2]:
                        count = dict_save_slots[command3]
                        count += 1
                        continue
                    count += 1
                    continue
                elif variables_dict[variable1] > int(variable2):
                    count = dict_save_slots[command3]
                    count += 1
                    continue
                else:
                    count += 1
                    continue
            if operator1 == "==":
                if variable2 in string.ascii_uppercase:
                    if variables_dict[variable1] == variables_dict[variable2]:
                        count = dict_save_slots[command3]
                        count +=1
                        continue
                    count += 1
                    continue
                elif variables_dict[variable1] == int(variable2):
                        count = dict_save_slots[command3]
                        count += 1
                        continue
                else:
                    count += 1
                    continue
            if operator1 == "<=":
                if variable2 in string.ascii_uppercase:
                    if variables_dict[variable1] <= variables_dict[variable2]:
                        count = dict_save_slots[command3]
                        continue
                elif variables_dict[variable1] <= int(variable2):
                        count = dict_save_slots[command3]
                        continue
                else:
                    count += 1
                    continue
            if operator1 == ">=":
                if variable2 in string.ascii_uppercase:
                    if variables_dict[variable1] >= variables_dict[variable2]:
                        break
                elif variables_dict[variable1] >= int(variable2):
                        break
                else:
                    count += 1
                    continue
            if operator1 == "!=":
                if variable2 in string.ascii_uppercase:
                    if variables_dict[variable1] != variables_dict[variable2]:
                        count = [dict_save_slots[command3]]
                        count += 1
                        continue
                elif variables_dict[variable1] != int(variable2):
                    count = dict_save_slots[command3]
                    count += 1
                    continue
                else:
                    count += 1
                    continue
        if x[0] == "END":
            break
        if x[0] == "PRINT":
            if x[1] in string.ascii_uppercase:
                variable = x[1]
                print_list.append(variables_dict[variable])
            else:
                variable = x[1]
                print_list.append(int(variable))
                count += 1
                continue
            count += 1
            continue
        command = x[0]
        variable = x[1]
        value = x[2]
        if command == "MOV":
            if value in string.ascii_uppercase:
                variables_dict[variable] = variables_dict[value]
                count += 1
                continue
            else:
                variables_dict[variable] = int(value)
                count += 1
                continue
        if command == "ADD":
            if value in string.ascii_uppercase:
                variables_dict[variable] += variables_dict[value]
                count += 1
                continue
            else:
                variables_dict[variable] += int(value)
                count += 1
                continue
        if command == "SUB":
            if value in string.ascii_uppercase:
                variables_dict[variable] -= variables_dict[value]
            else:
                variables_dict[variable] -= int(value)
        if command == "MUL":
            if value in string.ascii_uppercase:
                variables_dict[variable] *= variables_dict[value]
            else:
                variables_dict[variable] *= int(value)
        count += 1
    return print_list
if __name__ == "__main__":
    program3 = ['MOV A 1', 'MOV B 1', 'start:', 'MUL A 2', 'ADD B 1', 'IF B != 101 JUMP start', 'PRINT A']
    result = run(program3)
    print(result)