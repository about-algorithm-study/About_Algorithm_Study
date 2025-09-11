def backtrack(cur, count):
    global min_count
    if count >= min_count:          # 가지치기
        return
    if cur >= N - 1:                # 현재 위치가 마지막 정류장에 도착했으면
        min_count = min(min_count, count)   # min_count 갱신
        return                              # 갈 곳없으니까 종료
    for i in range(1, batteries[cur] + 1):  # batteries[pos]는 지금 위치에서 갈 수 있는 최대 거리
        backtrack(cur + i, count + 1)
 
T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]             # 맨 앞에 수는 리스트의 길이
    batteries = data[1:]        # 맨 앞에꺼 빼고 리스트
    min_count = float('inf')
 
    for i in range(1, batteries[0] + 1):    # 첫 배터리는 교환 횟수에서 제외
        backtrack(i, 0)
 
    print(f"#{tc} {min_count}")