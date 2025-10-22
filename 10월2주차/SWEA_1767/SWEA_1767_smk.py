
T = int(input())
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def find_core(arr):
    core_list = []
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                core_list.append((i, j))
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    connected[i][j] = True
    return core_list


def can_connect(x, y, d):
    nx, ny = x + delta[d][0], y + delta[d][1]
    line = []

    while 0 <= nx < N and 0 <= ny < N:
        if cells[nx][ny] != 0:
            return False, []
        line.append((nx, ny))
        nx += delta[d][0]
        ny += delta[d][1]
    
    return True, line

def line(index, cnt, hap):
    global min_hap, max_core

    if index == len(core_lst):
        if cnt > max_core:
            max_core = cnt
            min_hap = hap
        elif cnt == max_core and hap < min_hap:
            min_hap = hap
        return
    
    if cnt + (len(core_lst) - index) < max_core:
        return  # 앞으로 다 연결해도 최대 갱신 불가능


    x, y = core_lst[index]

    for d in range(4):
        ispossible, line_lst = can_connect(x, y, d)
        if ispossible:
            for nx, ny in line_lst:
                cells[nx][ny] = 2
            
            line(index + 1, cnt + 1, hap + len(line_lst))

            for nx, ny in line_lst:
                cells[nx][ny] = 0
        
    line(index + 1, cnt, hap)



for t in range(1, T + 1):
    N = int(input())
    cells = [list(map(int, input().split())) for _ in range(N)]
    connected = [[False]*N for _ in range(N)]

    max_core = 0
    min_hap = float('inf')

    core_lst = find_core(cells)

    line(0, 0, 0)

    print(f"#{t} {min_hap}")