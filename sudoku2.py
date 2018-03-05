import sys
import os


#os.system('cls')

grid = []
squares = []
lines= []
cols = []
lines_mis = []
cols_mis = []
squares_mis = []

total_nr = 9*9
known_nr = 0
unknown_nr = total_nr - known_nr

sq_pos = [[0,3,0,3],
          [0,3,3,6],
          [0,3,6,9],
          [3,6,0,3],
          [3,6,3,6],
          [3,6,6,9],
          [6,9,0,3],
          [6,9,3,6],
          [6,9,6,9]]

box = {}

for line in range(0, 9):
    squares.append([])
    lines.append([])
    cols.append([])
    lines_mis.append([])
    cols_mis.append([])
    squares_mis.append([])

for line in range (0, 9):
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

grid[0][2] = 2
grid[1][2] = 3
grid[1][4] = 1
grid[1][8] = 6
grid[2][1] = 4
grid[2][4] = 2
grid[2][7] = 3

grid[3][0] = 1
grid[3][5] = 3
grid[3][8] = 9
grid[4][2] = 5
grid[4][6] = 4
grid[5][0] = 2
grid[5][3] = 6
grid[5][8] = 8

grid[6][1] = 9
grid[6][4] = 7
grid[6][7] = 4
grid[7][0] = 7
grid[7][4] = 8
grid[7][6] = 5
grid[8][6] = 3


def reinit():
    global lines_mis, cols_mis, squares_mis, squares, lines, cols, box
    squares = []
    lines= []
    cols = []
    lines_mis = []
    cols_mis = []
    squares_mis = []
    box.update({}.fromkeys(box, []))
    
    for line in range(0, 9):
        squares.append([])
        lines.append([])
        cols.append([])
        lines_mis.append([])
        cols_mis.append([])
        squares_mis.append([])
        

def lists_compl(limit, el_nr):
    for line in range(limit[0],limit[1]):
        for col in range(limit[2],limit[3]):
            if grid[line][col] > 0:
                el_nr.append(grid[line][col])

    print el_nr

def get_known_nr(nr):
    for line in range(0, 9):
        for col in range(0, 9):
            if grid[line][col] > 0:
                nr += 1
    return nr

print 'numere cunoscute initial', get_known_nr(known_nr)

def update_known():
    global lines, cols, squares
    for line_nr in range(0, 9):
        lists_compl([0 + line_nr, 1 + line_nr, 0, 9], lines[line_nr])

    for col_nr in range(0, 9):
        lists_compl([0, 9, 0 + col_nr, 1 + col_nr], cols[col_nr])

    for sq_nr in range(0,9):
        lists_compl(sq_pos[sq_nr], squares[sq_nr])

def verify_square(line, col, nr):
    for sq in range(0, 9):
        if line in range(sq_pos[sq][0], sq_pos[sq][1]) and col in range(sq_pos[sq][2], sq_pos[sq][3]):
            if nr not in squares[sq]:
                box[(line, col)].append(nr)


def each_box_posib():
    for line in range(0, 9):
        for col in range(0, 9):
            #print 'colona update', col
            box[(line, col)] = []
            if grid[line][col] == 0:
                for nr in range(1, 10):
                    if nr not in lines[line] and nr not in cols[col]:
                        verify_square(line, col, nr)

                    else:
                        pass
                        #print 'nr ', nr, ' in line sau coloana', line, col
            else:
                pass
                #print 'nr dif de 0', nr


def one_per_box():
    global grid
    for line in range(0, 9):
        for col in range(0, 9):
            if len(box[(line, col)]) == 1:
                grid[line][col] = box[(line, col)][0]
                box[(line, col)] = []
    
def one_per_line():
    global grid
    for line in range(0, 9):  
        for col in range(0, 9):
            lines_mis[line].extend(box[(line, col)])
    for line in range(0, 9):
        for elem in lines_mis[line]:
            # i is the line number
            if lines_mis[line].count(elem) == 1:
                for col in range(0, 9):
                    if elem in box[(line, col)]:
                        grid[line][col] = elem
                        box[(line, col)] = []


def one_per_col():
    global grid
    for line in range(0, 9):
        for col in range(0, 9):
            cols_mis[col].extend(box[(line, col)])
            
    for col in range(0, 9):
        for elem in cols_mis[col]:
            # i is the col number
            if cols_mis[col].count(elem) == 1:
                for line in range(0, 9):
                    if elem in box[(line, col)]:
                        grid[line][col] = elem
                        box[(line, col)] = []


def one_per_sq():
    global grid
    for sq in range(0, 9):
        for line in range(sq_pos[sq][0], sq_pos[sq][1]):
            for col in range(sq_pos[sq][2], sq_pos[sq][3]):
                squares_mis[sq].extend(box[(line, col)])

    for sq in range(0, 9):
        for elem in squares_mis[sq]:
            # i is the sq number
            if squares_mis[sq].count(elem) == 1:
                for line in range(sq_pos[sq][0], sq_pos[sq][1]):
                    for col in range(sq_pos[sq][2], sq_pos[sq][3]):
                        if elem in box[(line, col)]:
                            grid[line][col] = elem
                            box[(line, col)] = []


#while get_known_nr(known_nr) < 50:
n=0
print 'sudoku grid'
while get_known_nr(known_nr) < 81:
    
    update_known()
    print lines[0]
    each_box_posib()
    one_per_box()
    reinit()

    update_known()
    print lines[0]
    each_box_posib()
    one_per_line()
    reinit()

    update_known()
    print lines[0]
    each_box_posib()
    one_per_col()
    reinit()

    update_known()
    print lines[0]
    each_box_posib()
    one_per_sq()
    reinit()
    
    print 'numere cunoscute', get_known_nr(known_nr)
    n += 1

for line in range(0, 9):
    print grid[line]
print n





    
        
