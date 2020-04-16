import time
start_time = time.time()


dict_cell = {}
temp_cell_dict = {}


def backtracking(s, num1):
    lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i_r, r in enumerate(s):
        for i_c, n in enumerate(r):
            if n == 0:
                for num in lis1:
                    if (num not in s[i_r]) and (num not in [x[i_c] for x in s]) and (num not in [y for x in s[(i_r // 3) * 3:(i_r // 3) * 3 + 3] for y in x[(i_c // 3 * 3):(i_c // 3 * 3) + 3]]) and num > num1:
                        s[i_r][i_c] = num
                        return [s, 0]
                    elif num == 9:
                        s[i_r][i_c] = 0
                        id = rr = cc = 0
                        for id, i in enumerate(dict_cell.keys()):
                            lis = list(map(int, i.split(', ')))
                            if lis[0] == i_r and lis[1] == i_c:
                                if id != 0:
                                    id = id - 1
                                break
                        for idj, j in enumerate(dict_cell.keys()):
                            if idj == id:
                                lis = list(map(int, j.split(', ')))
                                rr = lis[0]
                                cc = lis[1]
                                break
                        num1 = s[rr][cc]
                        s[rr][cc] = 0
                        return backtracking(s, num1)


def fill_good_values(s):
    del_list = []
    for i in dict_cell:
        if len(dict_cell[i]) == 1:
            lis = list(map(int, i.split(', ')))
            s[lis[0]][lis[1]] = dict_cell[i][0]
            del_list.append(i)
    for i in del_list:
        del dict_cell[i]
    return s


def find_values_for_cell(s, f):
    if 0 not in [x for y in s for x in y]:
        return False
    list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for r, id_r in enumerate(s):
        for c, id_c in enumerate(id_r):
            list_possible = []
            num = s[r][c]
            if num == 0:
                column_list = [x[c] for x in s]
                box_list = [y for x in s[(r // 3) * 3:(r // 3) * 3 + 3] for y in x[(c // 3 * 3):(c // 3 * 3) + 3]]
                for n in list_num:
                    if n not in s[r] and n not in column_list and n not in box_list:
                        list_possible.append(n)
                    list_possible.append(0)
                if f:
                    dict_cell[f'{r}, {c}'] = list_possible
                else:
                    temp_cell_dict[f'{r}, {c}'] = list_possible


def print_board(sud):
    for r in sud:
        print(r)


s = [[5, 0, 0, 0, 1, 0, 0, 0, 4],
     [2, 7, 4, 0, 0, 0, 6, 0, 0],
     [0, 8, 0, 9, 0, 4, 0, 0, 0],
     [8, 1, 0, 4, 6, 0, 3, 0, 2],
     [0, 0, 2, 0, 3, 0, 1, 0, 0],
     [7, 0, 6, 0, 9, 1, 0, 5, 8],
     [0, 0, 0, 5, 0, 3, 0, 1, 0],
     [0, 0, 5, 0, 0, 0, 9, 2, 7],
     [1, 0, 0, 0, 2, 0, 0, 0, 3]]

s_not = s
while True:
    find_values_for_cell(s, 1)
    s = fill_good_values(s)
    if s == s_not:
        break
    s_not = s
    dict_cell.clear()

s_dash = [[y for y in x] for x in s]
num = 0
while True:
    [s_dash, num] = backtracking(s_dash, num)
    if 0 not in [x for y in s_dash for x in y]:
        break
print_board(s_dash)
print('\n')
print("--- %s seconds ---" % (time.time() - start_time))
