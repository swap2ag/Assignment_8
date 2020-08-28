'''
### ==================================================================== ###
###                      Import Libraries                                ###
### ==================================================================== ###
import math
'''

### ==================================================================== ###
###                      Function Definitions                            ###
### ==================================================================== ###
def prompt(turn):
    print ("Player "+ str(turn) +"\'s chance: ")
    print("Enter the position and number to be entered: ")
    pos = int(input())
    num = int(input())
    return pos, num


def convertPosToXY(pos, ncols):
    pos = pos - 1 # subtract one from pos
    x = pos // ncols
    y = pos - ncols * x
    return x,y
    
def validateNum(num, turn, n,l):
    # check if num has been already used for this user
    if num in l:
        msg = "Error: Number already present on board!!\n"
        return False,msg
    if (turn == 1):
        if (num % 2 != 0):
            if (num > n*n):
                msg = "Error: You have entered the number greater than " + str(n*n)
                return False, msg
        else:
            msg = "Error: You have entered an even no!!\n"
            return False, msg
    elif turn == 2:
        if (num % 2 == 0):
            if(num > n*n):
                return False, msg
        else:
            msg = "Error: You have entered odd no.!!\n"
            return False, msg
    msg = ""
    return True, msg

### ==================================================================== ###
###                 Execution starts here                                ###
### ==================================================================== ###
if __name__ == "__main__":
    print("Welcome to the Game!")
    over = False
    turn = 0
    cnt = 0
    # Create 2D array and initialize its elements to 0
    nrows,ncols = 3,3
    arr = [[0]*ncols]*nrows
    l = []
    while(over == False):
        pos, num = prompt(turn+1)
        flag, msg = validateNum(num, turn+1, nrows, l)

        if (flag == False):
            print(msg)
            continue

        x,y = convertPosToXY(pos, ncols)
        if (arr[x][y] != 0):
            print("Invalid entry!! element already present at this location!!\n")
            continue
        l.append(num)
        arr[x][y] = num
        turn = (turn + 1) % 2
        print(pos, num)
        cnt += 1
        if (cnt == 9):
            over = True
        for i in arr:
            for item in i:
                print(item,end=' ')
            print()