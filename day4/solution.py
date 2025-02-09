import numpy as np;

def search(lines, row, col, letter, direction):
    next_letter_pos = (row+direction[0], col+direction[1]);
    # check bounds
    if ((next_letter_pos[0] < 0 or next_letter_pos[0] >= len(lines)) or
        (next_letter_pos[1] < 0 or next_letter_pos[1] >= len(lines[next_letter_pos[0]]))):
        return False;
    next_letter = lines[next_letter_pos[0]][next_letter_pos[1]];
    return next_letter == letter;

def solution(lines):
    count = 0;
    # when defining directions, x->row, y->col
    #  x+ is toward end of file
    #  y+ is toward end of line
    directions = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]; 
    for row in range(0,len(lines)):
        xind = lines[row].find('X');
        while (xind != -1):
            for direction in directions:
                tmp_row = row;
                tmp_col = xind;
                for letter in ('M', 'A', 'S'):
                    if (search(lines, tmp_row, tmp_col, letter, direction)):
                        tmp_row += direction[0];
                        tmp_col += direction[1];
                        if (letter == 'S'): #we found S, so done
                            count += 1;
                    else:
                        break;
            xind = lines[row].find('X', xind+1);
    return count;

def get_xmas_stencil(lines, pos):
    chars = ["", "", "", ""];
    stencil = [(-1,-1), (-1,1), (1,-1), (1,1)];
    # check room for stencil
    if ((pos[0] > 0 and pos[0] < len(lines)-1) and
        (pos[1] > 0 and pos[1] < len(lines[pos[0]])-1)):
        for i in range(0,len(stencil)):
            chars[i] = lines[pos[0]+stencil[i][0]][pos[1]+stencil[i][1]];
    return chars;

def check_stencil(chars):
    possibilities = [['M', 'M', 'S', 'S'],
                     ['M', 'S', 'M', 'S'],
                     ['S', 'M', 'S', 'M'],
                     ['S', 'S', 'M', 'M']];
    return (chars in possibilities);

def solution_pt2(lines):
    count = 0;
    for row in range(0, len(lines)):
        xind = lines[row].find('A');
        while (xind != -1):
            chars = get_xmas_stencil(lines, (row,xind));
            if (check_stencil(chars)):
                count += 1;
            xind = lines[row].find('A', xind+1);
    return count;

if __name__ == "__main__":
    lines = [];
    with open("input.txt") as fp:
        lines = [line.rstrip() for line in fp];
    print(solution(lines));
    print(solution_pt2(lines));
