from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) > 11:
        return False
    check_Century = checkCentury(pic)
    check_Dob = checkDob(pic)
    check_Control = checkControl(pic)

    if check_Century and check_Dob and check_Control:
        return True
    else:
        return False

def checkCentury(dob: bool):
    if dob[6] == "+" or dob[6] == "-" or dob[6] == "A":
        century = True
    else:
        century = False
    return century

def checkDob(pic):
    if not checkCentury(pic):
        return False
    day = int(pic[0:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    try:
        if datetime(year+int(centuryCalc(pic)), month, day):
            return True
    except:
        return False

def checkControl(pic):
    controlDataset = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    dob = pic[0:6]
    finnishPIC = pic[7:10]
    for number in finnishPIC:
        dob += number
    dob = int(dob) % 31
    controlChar = pic[-1]
    #print(controlDataset[dob])
    if controlDataset[dob] == controlChar:
        return True
    else:
        return False

def centuryCalc(pic):
    if pic[6] == "+":
        century = 1800
    elif pic[6] == "-":
        century = 1900
    elif pic[6] == "A":
        century = 2000
    else:
        return 0
    return century

if __name__ == "__main__":
    pics = ["080842-720N"]
    for i in pics:
        print(is_it_valid(i))
