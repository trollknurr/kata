import pprint


def check(x, y, arr):
    l_x, g_x = x - 1, x + 1
    l_y, g_y = y - 1, y + 1
    #
    dis = 0
    #
    if l_x >= 0:
        if arr[y][l_x] == 'X':
            dis += 1
    if g_x < len(arr[y]):
        if arr[y][g_x] == 'X':
            dis += 1
    if l_y >= 0:
        if arr[l_y][x] == 'X':
            dis += 1
    if g_y < len(arr):
        if arr[g_y][x] == 'X':
            dis += 1
    return dis


def land_perimeter(arr):
    p = 0
    l = 0
    while l < len(arr):
        c = 0
        while c < len(arr[l]):
            if arr[l][c] == 'X':
                p += (4 - check(c, l, arr))
            c += 1
        l += 1
    return p



print(land_perimeter(
    ["OXOOOX",
     "OXOXOO",
     "XXOOOX",
     "OXXXOO",
     "OOXOOX",
     "OXOOOO",
     "OOXOOX",
     "OOXOOO",
     "OXOOOO",
     "OXOOXX"]))

print(land_perimeter(
        ['XOOXO',
        'XOOXO',
        'OOOXO',
        'XXOXO',
        'OXOOO']))
