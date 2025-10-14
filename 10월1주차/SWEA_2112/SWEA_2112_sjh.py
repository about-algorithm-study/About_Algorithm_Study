import sys
sys.stdin = open('sample_input.txt')

def test():
    if K == 1:
        return True
    for j in range(W):
        flag = False
        cnt =1
        for i in range(1,D):
            if arr[i][j] == arr[i-1][j]:
                cnt += 1
                if cnt == K:
                    flag = True
                    break
            else:
                cnt = 1
        if not flag:
            return False
    return True

def DFS(index, injection_cnt):
    global answer
    if injection_cnt >= answer:
        return
    if test():
        answer = min(answer,injection_cnt)
        return
    if index == D:
        return

    #원본을 바꾸니까 백업
    origin = arr[index][:]
    DFS(index+1, injection_cnt)

    arr[index] = [0] * W
    DFS(index+1, injection_cnt +1)

    arr[index] = [1] * W
    DFS(index + 1, injection_cnt + 1)

    arr[index] = origin



T=int(input())
for tc in range(1,T+1):
    D,W,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(D)]

    answer = D #행렬만큼 주입하기 전에 K를 충족할 수 밖에
    DFS(0,0)

    print(f'#{tc} {answer}')