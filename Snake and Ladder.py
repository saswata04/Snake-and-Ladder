import os
import random
import time

lst_A = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], [
    '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
lst_B = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], [
    '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]

lst1 = [['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], [
    '___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___']]

num_lst = [['100', '099', '098', '097', '096', '095', '094', '093', '092', '091'], ['081', '082', '083', '084', '085', '086', '087', '088', '089', '090'], ['080', '079', '078', '077', '076', '075', '074', '073', '072', '071'], ['061', '062', '063', '064', '065', '066', '067', '068', '069', '070'], ['060', '059', '058', '057', '056', '055', '054', '053', '052', '051'], [
    '041', '042', '043', '044', '045', '046', '047', '048', '049', '050'], ['040', '039', '038', '037', '036', '035', '034', '033', '032', '031'], ['021', '022', '023', '024', '025', '026', '027', '028', '029', '030'], ['020', '019', '018', '017', '016', '015', '014', '013', '012', '011'], ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010']]

'''slot_A={1:lst_A[9][0],2:lst_A[9][1],3:lst_A[9][2],4:lst_A[9][3],5:lst_A[9][4],6:lst_A[9][5],7:lst_A[9][6],8:lst_A[9][7],9:lst_A[9][8],10:lst_A[9][9],
11:lst_A[8][9],12:lst_A[8][8],13:lst_A[8][7],14:lst_A[8][6],15:lst_A[8][5],16:lst_A[8][4],17:lst_A[8][3],18:lst_A[8][2],19:lst_A[8][1],20:lst_A[8][0],
21:lst_A[7][0],22:lst_A[7][1],23:lst_A[7][2],24:lst_A[7][3],25:lst_A[7][4],26:lst_A[7][5],27:lst_A[7][6],28:lst_A[7][7],29:lst_A[7][8],30:lst_A[7][9],
31:lst_A[6][9],32:lst_A[6][8],33:lst_A[6][7],34:lst_A[6][6],35:lst_A[6][5],36:lst_A[6][4],37:lst_A[6][3],38:lst_A[6][2],39:lst_A[6][1],40:lst_A[6][0],
41:lst_A[5][0],42:lst_A[5][1],43:lst_A[5][2],44:lst_A[5][3],45:lst_A[5][4],46:lst_A[5][5],47:lst_A[5][6],48:lst_A[5][7],49:lst_A[5][8],50:lst_A[5][9],
51:lst_A[4][9],52:lst_A[4][8],53:lst_A[4][7],54:lst_A[4][6],55:lst_A[4][5],56:lst_A[4][4],57:lst_A[4][3],58:lst_A[4][2],59:lst_A[4][1],60:lst_A[4][0],
61:lst_A[3][0],62:lst_A[3][1],63:lst_A[3][2],64:lst_A[3][3],65:lst_A[3][4],66:lst_A[3][5],67:lst_A[3][6],68:lst_A[3][7],69:lst_A[3][8],70:lst_A[3][9],
71:lst_A[2][9],72:lst_A[2][8],73:lst_A[2][7],74:lst_A[2][6],75:lst_A[2][5],76:lst_A[2][4],77:lst_A[2][3],78:lst_A[2][2],79:lst_A[2][1],80:lst_A[2][0],
81:lst_A[1][0],82:lst_A[1][1],83:lst_A[1][2],84:lst_A[1][3],85:lst_A[1][4],86:lst_A[1][5],87:lst_A[1][6],88:lst_A[1][7],89:lst_A[1][8],90:lst_A[1][9],
91:lst_A[0][9],92:lst_A[0][8],93:lst_A[0][7],94:lst_A[0][6],95:lst_A[0][5],96:lst_A[0][4],97:lst_A[0][3],98:lst_A[0][2],99:lst_A[0][1],100:lst_A[0][0]}

slot_B={1:lst_B[9][0],2:lst_B[9][1],3:lst_B[9][2],4:lst_B[9][3],5:lst_B[9][4],6:lst_B[9][5],7:lst_B[9][6],8:lst_B[9][7],9:lst_B[9][8],10:lst_B[9][9],
11:lst_B[8][9],12:lst_B[8][8],13:lst_B[8][7],14:lst_B[8][6],15:lst_B[8][5],16:lst_B[8][4],17:lst_B[8][3],18:lst_B[8][2],19:lst_B[8][1],20:lst_B[8][0],
21:lst_B[7][0],22:lst_B[7][1],23:lst_B[7][2],24:lst_B[7][3],25:lst_B[7][4],26:lst_B[7][5],27:lst_B[7][6],28:lst_B[7][7],29:lst_B[7][8],30:lst_B[7][9],
31:lst_B[6][9],32:lst_B[6][8],33:lst_B[6][7],34:lst_B[6][6],35:lst_B[6][5],36:lst_B[6][4],37:lst_B[6][3],38:lst_B[6][2],39:lst_B[6][1],40:lst_B[6][0],
41:lst_B[5][0],42:lst_B[5][1],43:lst_B[5][2],44:lst_B[5][3],45:lst_B[5][4],46:lst_B[5][5],47:lst_B[5][6],48:lst_B[5][7],49:lst_B[5][8],50:lst_B[5][9],
51:lst_B[4][9],52:lst_B[4][8],53:lst_B[4][7],54:lst_B[4][6],55:lst_B[4][5],56:lst_B[4][4],57:lst_B[4][3],58:lst_B[4][2],59:lst_B[4][1],60:lst_B[4][0],
61:lst_B[3][0],62:lst_B[3][1],63:lst_B[3][2],64:lst_B[3][3],65:lst_B[3][4],66:lst_B[3][5],67:lst_B[3][6],68:lst_B[3][7],69:lst_B[3][8],70:lst_B[3][9],
71:lst_B[2][9],72:lst_B[2][8],73:lst_B[2][7],74:lst_B[2][6],75:lst_B[2][5],76:lst_B[2][4],77:lst_B[2][3],78:lst_B[2][2],79:lst_B[2][1],80:lst_B[2][0],
81:lst_B[1][0],82:lst_B[1][1],83:lst_B[1][2],84:lst_B[1][3],85:lst_B[1][4],86:lst_B[1][5],87:lst_B[1][6],88:lst_B[1][7],89:lst_B[1][8],90:lst_B[1][9],
91:lst_B[0][9],92:lst_B[0][8],93:lst_B[0][7],94:lst_B[0][6],95:lst_B[0][5],96:lst_B[0][4],97:lst_B[0][3],98:lst_B[0][2],99:lst_B[0][1],100:lst_B[0][0]}'''


def board():
    for i in range(10):
        for j in range(10):
            lst_A[i][j] = '_'
            lst_B[i][j] = '_'

    lst1[3][3] = 'Ss1'
    lst1[7][5] = 'Se1'
    lst1[0][1] = 'Ss2'
    lst1[6][3] = 'Se2'
    lst1[0][3] = 'Le1'
    lst1[6][5] = 'Ls1'
    lst1[8][8] = 'Ls2'
    lst1[5][9] = 'Le2'

    for i in range(10):
        for j in range(10):
            print(num_lst[i][j], lst1[i][j]+lst_A[i][j]+lst_B[i][j], end='|')
        print()
    print()


a = 0


def logic_A(x):
    global lst_A
    global lst_B
    for i in range(10):
        for j in range(10):
            lst_A[i][j] = '_'

    global a
    a = a+x
    if a < 6:
        a = 0
    if a >= 1 and a <= 10:
        lst_A[9][a-1] = 'A'
    elif a >= 11 and a <= 20:
        if a == 12:
            lst_A[5][9] = 'A'
            a = 50
        else:
            lst_A[8][20-a] = 'A'
    elif a >= 21 and a <= 30:
        lst_A[7][a-21] = 'A'
    elif a >= 31 and a <= 40:
        if a == 35:
            lst_A[0][3] = 'A'
            a = 97
        else:
            lst_A[6][40-a] = 'A'
    elif a >= 41 and a <= 50:
        lst_A[5][a-41] = 'A'
    elif a >= 51 and a <= 60:
        lst_A[4][60-a] = 'A'
    elif a >= 61 and a <= 70:
        if a == 64:
            lst_A[7][5] = 'A'
            a = 26
        else:
            lst_A[3][a-61] = 'A'
    elif a >= 71 and a <= 80:
        lst_A[2][80-a] = 'A'
    elif a >= 81 and a <= 90:
        lst_A[1][a-81] = 'A'
    elif a >= 91 and a < 100:
        if a == 99:
            lst_A[6][3] = 'A'
            a = 37
        else:
            lst_A[0][100-a] = 'A'
    elif a == 100:
        lst_A[0][0] = 'A'
    elif a > 100:
        a = a-x
        if a >= 91 and a < 100:
            lst_A[0][100-a] = 'A'
        # logic_A(a)

    for i in range(10):
        for j in range(10):
            print(num_lst[i][j], lst1[i][j]+lst_A[i][j]+lst_B[i][j], end='|')
        print()
    print()
    if a == 100:
        print("Player 1 wins")
        os._exit(0)


b = 0


def logic_B(y):
    global lst_A
    global lst_B
    for i in range(10):
        for j in range(10):
            lst_B[i][j] = '_'

    global b
    b = b+y
    if b < 6:
        b = 0
    if b >= 1 and b <= 10:
        lst_B[9][b-1] = 'B'
    elif b >= 11 and b <= 20:
        if b == 12:
            lst_B[5][9] = 'B'
            b = 50
        else:
            lst_B[8][20-b] = 'B'
    elif b >= 21 and b <= 30:
        lst_B[7][b-21] = 'B'
    elif b >= 31 and b <= 40:
        if b == 35:
            lst_B[0][3] = 'B'
            b = 97
        else:
            lst_B[6][40-b] = 'B'
    elif b >= 41 and b <= 50:
        lst_B[5][b-41] = 'B'
    elif b >= 51 and b <= 60:
        lst_B[4][60-b] = 'B'
    elif b >= 61 and b <= 70:
        if b == 64:
            lst_B[7][5] = 'B'
            b = 26
        else:
            lst_B[3][b-61] = 'B'
    elif b >= 71 and b <= 80:
        lst_B[2][80-b] = 'B'
    elif b >= 81 and b <= 90:
        lst_B[1][b-81] = 'B'
    elif b >= 91 and b < 100:
        if b == 99:
            lst_B[6][3] = 'B'
            b = 37
        else:
            lst_B[0][100-b] = 'B'
    elif b == 100:
        lst_B[0][0] = 'B'
    elif b > 100:
        b = b-y
        if a >= 91 and a < 100:
            lst_B[0][100-b] = 'B'
        # logic_B(b)

    for i in range(10):
        for j in range(10):
            print(num_lst[i][j], lst1[i][j]+lst_A[i][j]+lst_B[i][j], end='|')
        print()
    print()
    if b == 100:
        print("Player 2 wins")
        os._exit(0)


def dice():
    players = 0
    choice = 0
    new = 0

    def inputs():
        global players
        players = 2
        logic()

    def choices():
        global choice
        try:
            choice = input("Choice: ")
            if(choice != "r" and choice != "q"):
                raise Exception
        except:
            print("Invalid Input\nTry Again")
            choices()

    def logic():
        global players
        global choice
        global new
        for i in range(1, (players+1)):
            print(">>>>Player", i, "'s turn")
            print("Press 'r' to roll the dice")
            print("Press 'q' to quit")
            choices()
            if(choice == 'r'):
                if(i == players):
                    logic_for_player2()
                else:
                    logic_for_player1()

            else:
                os._exit(0)

    def logic_for_player1():
        print("<<<Rolling the dice>>>")
        time.sleep(2)
        new = random.randint(1, 6)
        print(">>", new, "<<")
        print()
        logic_A(new)

    def logic_for_player2():
        print("<<<Rolling the dice>>>")
        time.sleep(2)
        new = random.randint(1, 6)
        print(">>", new, "<<")
        print()
        logic_B(new)
        logic()
    print("<<<<<<<<<< The Dice >>>>>>>>>>")
    inputs()


play_choice = 0


def option_choosing():
    global play_choice
    try:
        play_choice = int(input("Your Choice: "))
        if play_choice != 1 and play_choice != 2:
            raise Exception
    except:
        print("Invalid Input\nTry Again")
        option_choosing()


def option():
    print("How do you want to play?")
    print("1--> Player1 VS Player2")
    print("2--> Player  VS  Computer")
    option_choosing()
    if play_choice == 1:
        dice()
    else:
        dice_AI()


def dice_AI():
    choice_AI = 0
    new = 0

    def choices_AI():
        global choice_AI
        try:
            choice_AI = input("Choice: ")
            if(choice_AI != "r" and choice_AI != "q"):
                raise Exception
        except:
            print("Invalid Input\nTry Again")
            choices_AI()

    def logic_AI():
        global choice_AI
        for i in range(1, 3):
            if i == 1:
                print(">>>>Your turn")
                print("Press 'r' to roll the dice")
                print("Press 'q' to quit")
                choices_AI()
                if(choice_AI == 'r'):
                    print("<<<Rolling the dice>>>")
                    time.sleep(2)
                    new_AI = random.randint(1, 6)
                    print(">>", new_AI, "<<")
                    print()
                    logic_A(new_AI)
                else:
                    os._exit(0)
            else:
                print(">>>>My turn")
                print("<<<Rolling the dice>>>")
                time.sleep(2)
                new_AI = random.randint(1, 6)
                print(">>", new_AI, "<<")
                print()
                logic_B(new_AI)
                logic_AI()
    print("<<<<<<<<<< The Dice >>>>>>>>>>")
    logic_AI()


print("*****************************************SNAKES AND LADDERS*****************************************")
board()
option()
