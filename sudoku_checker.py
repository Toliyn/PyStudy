correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

lst_example = [1,2,0,3]

def find_hor_sum(lst):
    sum = 0
    for x in lst:
        sum = sum + lst[x]
    return sum


def check_sudoku(lst):
    matrix_min = 0
    matrix_max = len(lst)

print(find_hor_sum(lst_example))
# >>> 6

#print(check_sudoku(incorrect))
# >>> False

#print(check_sudoku(correct))
# >>> True

#print(check_sudoku(incorrect2))
# >>> False

#print(check_sudoku(incorrect3))
# >>> False

#print(check_sudoku(incorrect4))
# >>> False

#print(check_sudoku(incorrect5))
# >>> False