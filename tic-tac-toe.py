d={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}

def display_row(d,row_number):
    print("       "," | ","  "," | ","  ")
    print("     ",d[1+3*(row_number-1)]," | ",d[2+3*(row_number-1)],"  | ",d[3+3*(row_number-1)],"  ")
    print("       "," | ","  "," | ","  ")

# display_row(d,1)

def display_col(n):
    for j in range(n):
        for i in range(14):
            print("=",end=" ")
        print(" ")

# display_col(2)

def display_board(d):

    for i in range(1,4):
        display_row(d,i)
        if i<3:
            display_col(1)

display_board(d)

def player_name():
    player1=input("enter name of player 1: ")
    print("hii! player",player1)
    player1_char=input("enter your character(x,o): ")
    while player1_char!='x' and  player1_char!='o':
        print("please enter valid character")
        player1_char=input("enter your character(x,o: )")
    player2=input("enter name of player 2: ")
    if player1_char=='x':
        player2_char='o'
    else:
        player2_char='x'
    print("character of player 2 is ",player2_char)
player_name()

def row_check(d):

    if d[1]==d[2]==d[3] and d[1]!=" ":
        return True
    
    elif d[4]==d[5]==d[6] and d[4]!=" ":
        return True
    
    elif d[7]==d[8]==d[9] and d[7]!=" ":
        return True
    
    else:
        return False
    
def col_check(d):
    if d[1]==d[4]==d[7] and d[1]!=" ":
        return True
    
    elif d[2]==d[5]==d[8] and d[4]!=" ":
        return True
    
    elif d[3]==d[6]==d[9] and d[7]!=" ":
        return True
    
    else:
        return False

def diagonal_check(d):
    if d[1]==d[5]==d[9] and d[1]!=" ":
        return True
    
    elif d[3]==d[5]==d[7] and d[4]!=" ":
        return True
    
    else:
        return False
    
    
ref={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
print("starting tick tack toe!!")
display_board(ref)