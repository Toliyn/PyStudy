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



def check_sudoku(lst):
    matrix_size = len(lst)
    digit = 1
    while digit < matrix_size:
        i = 0
        while i < matrix_size:
            row_count = 0
            col_count = 0
            j = 0
            while j < matrix_size:
                if lst[i][j] == digit:
                    row_count = row_count+1
                if lst[j][i] == digit:
                   col_count = col_count + 1
                j = j + 1
            if row_count !=1 or col_count !=1:
                return False
            i = i+1
        digit = digit +1
    return True



print(check_sudoku(incorrect))
# >>> False

print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False
