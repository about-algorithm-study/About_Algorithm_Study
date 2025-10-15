def check_col(column, K):
    count = 1

    for i in range(1, len(column)):
        if column[i] == column[i - 1]: # 연속된 숫자가 K개 이상인지 확인
            count += 1
            if count >= K : # 연속된 숫자인 count가 K 이상이면 true 반환
                return True
        else:
            count = 1

    return count >= K

def check_pass(film, D, W, K):
    for col in range(W): # 각 열마다 검사
        column = [film[row][col] for row in range(D)] # 현재 열의 데이터 추출

        if not check_col(column, K):
            return False
    return True # 모든 열이 합격이면 전체 합격

def dfs(depth, count):
    global answer

    if count >= answer: # 가지치기
        return

    if depth == D:
        if check_pass(films, D, W, K):
            answer = min(answer, count)
        return

    dfs(depth + 1, count)

    original = films[depth][:] # A로 변경
    films[depth] = [0] * W
    dfs(depth + 1, count + 1)
    films[depth] = original

    original = films[depth][:] # B로 변경
    films[depth] = [1] * W
    dfs(depth + 1, count + 1)
    films[depth] = original


T = int(input())

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]

    answer = float('inf')

    if check_pass(films, D, W, K):
        answer = 0
    else:
        dfs(0, 0)

    print(f"#{tc} {answer}")