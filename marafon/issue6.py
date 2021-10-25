def harry(list2d: list) -> int:
    if list2d == [[]]:
        return -1
    n_rows = len(list2d)
    letters_in_row = len(list2d[0])
    for i_row in range(n_rows):
        for i_letter in range(letters_in_row):
            if not i_row and i_letter:
                list2d[i_row][i_letter] += list2d[i_row][i_letter - 1]
            elif i_row and not i_letter:
                list2d[i_row][i_letter] += list2d[i_row - 1][i_letter]
            elif i_row and i_letter:
                way1 = list2d[i_row][i_letter] + list2d[i_row][i_letter - 1]
                way2 = list2d[i_row][i_letter] + list2d[i_row - 1][i_letter]
                if way1 >= way2:
                    list2d[i_row][i_letter] = way1
                else:
                    list2d[i_row][i_letter] = way2
    return list2d[-1][-1]


if __name__ == '__main__':
    print(harry([[]]))
    print(harry([[5, 2], [5, 2]]))
    print(harry([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]))
