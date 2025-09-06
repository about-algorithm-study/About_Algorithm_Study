T= int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    student_lst =[list(map(int, input().split())) for _ in range(N)]
 
    # print(student_lst)
 
    grade = N//10
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
 
    score = []
 
    for i in range(N):
        mid, final, project = student_lst[i]
        zumsu = mid * 0.35 + final * 0.45 + project * 0.2
        score.append(zumsu)
    # print(score)
    cnt = score[K-1]
 
    ans = 1
    score_sorted = sorted(score, reverse=True)
    for a in range(N):
        if score_sorted[a] > cnt:
            ans += 1
    # print(ans)
 
    grade_idx = (ans - 1) // grade
    # ans는 K번째 학생의 순위 ex) K번째 학생보다 점수 높은 학생이 3명이면, ans = 4 -> K번째 학생은 전체4등
    # grade는 한 등급에 들어가는 학생의 수를 나타내고
    # 순위를 0등부터 계산하고 있어서 ans-1 을 해줌
    # 1등 -> 0// A+
    # 2등 -> 1// A+
    # 3등 -> 2// A0
    print(f'#{tc} {grades[grade_idx]}')
    # grades는 등급이 들어있는 리스트이고
    # grade_idx의 인덱스 위치를 출력하면 그 등급이 나오게 됨.