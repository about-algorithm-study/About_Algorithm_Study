T = int(input())

for t in range(1, T + 1):
    N = int(input())

    omok = [list(input().strip()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]


    delta = [(0, 1), (1, 0), (1, 1), (-1, 1) ]

    found = False
    for r in range(N):
        if found:
            break
        for c in range(N):
            if omok[r][c] != 'o':
                continue    

            for dx, dy in delta:
                pr, pc = r - dx, c - dy
                if 0 <= pr < N and 0 <= pc <N and omok[pr][pc] == 'o':
                    continue
                
                count = 0
                nr, nc = r, c
                
                while 0 <= nr < N and 0 <= nc < N and omok[nr][nc] == 'o':

                    count += 1
                    if count >= 5:
                        found = True
                        break
                
                    nr += dx
                    nc += dy

        if found :
                    break
    
    print(f"#{t} {'YES' if found else 'NO'}")