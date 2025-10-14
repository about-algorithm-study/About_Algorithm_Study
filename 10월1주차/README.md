# 10월 1주차

## 📅 기간: 2025.10.06 ~ 2025.10.12

## 🎯 주제: 삼성 SW 역량 테스트 실전 대비 (IM + A형)

---

## 📝 문제 목록

### 🔰 IM 수준 문제 (6개)

| 번호 | 문제명 | 난이도 | 분류 | 추천 이유 | 링크 |
|------|---------|--------|------|-----------|------|
| SWEA_1966 | 숫자를 정렬하자 | D2 | 정렬 | 기본 정렬 알고리즘 복습 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq) |
| SWEA_1945 | 간단한 소인수분해 | D2 | 수학/구현 | 소인수분해 구현 연습 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq) |
| SWEA_1926 | 간단한 369게임 | D2 | 구현/문자열 | 문자열 처리 및 조건문 연습 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq) |
| SWEA_1204 | 최빈수 구하기 | D2 | 구현/해시 | 딕셔너리/해시맵 활용 연습 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13vbx6AJ0CFAYD) |
| SWEA_1285 | 아름이의 돌 던지기 | D2 | 구현/완전탐색 | 최솟값 찾기 및 카운팅 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN) |
| SWEA_1217 | 거듭 제곱 | D3 | 재귀/수학 | 재귀 함수 구현 연습 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14dUIaAAUCFAYD) |

### 🏆 A형 수준 문제 (3개)

| 번호 | 문제명 | 난이도 | 분류 | 추천 이유 | 링크 |
|------|---------|--------|------|-----------|------|
| SWEA_2112 | 보호 필름 | D4 | DFS/백트래킹 | 백트래킹 + 시뮬레이션 종합 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu) |
| SWEA_4014 | 활주로 건설 | D4 | 시뮬레이션 | 2차원 배열 탐색 및 조건 처리 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH) |
| SWEA_5644 | 무선 충전 | D4 | 시뮬레이션/완전탐색 | 복잡한 시뮬레이션 구현 능력 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo) |

---

## 📊 진행 현황

| 멤버 | 진행률 | 풀이 문제 수 | 비고 |
|------|--------|-------------|------|
| 김강연 | 33.3% 🟩🟩🟩⬜⬜⬜⬜⬜⬜ | 3/9 | ⏳ |
| 신재혁 | 33.3% 🟩🟩🟩⬜⬜⬜⬜⬜⬜ | 3/9 | ⏳ |
| 오창민 | 0.0% ⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0/9 | ⏳ |
| 송민경 | 0.0% ⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0/9 | ⏳ |
| 최재각 | 33.3% 🟩🟩🟩⬜⬜⬜⬜⬜⬜ | 3/9 | ⏳ |

**마지막 업데이트**: 2025-10-14 12:53

## 💡 학습 포인트

### 📚 IM 수준 문제 공략법

#### 1. SWEA_1966 - 숫자를 정렬하자 (D2)
- **핵심**: Python 내장 정렬 함수 활용
- **시간 복잡도**: O(N log N)
- **주의사항**: 입력 형식 정확히 파악하기
```python
# 기본 접근
arr.sort()  # 오름차순
# 또는
sorted_arr = sorted(arr)
```

#### 2. SWEA_1945 - 간단한 소인수분해 (D2)
- **핵심**: 2, 3, 5, 7, 11로 나누어 떨어지는 횟수 구하기
- **팁**: while 반복문으로 각 소인수로 나누기
```python
primes = [2, 3, 5, 7, 11]
for p in primes:
    count = 0
    while N % p == 0:
        count += 1
        N //= p
```

#### 3. SWEA_1926 - 간단한 369게임 (D2)
- **핵심**: 숫자를 문자열로 변환 후 '3', '6', '9' 개수 세기
- **팁**: `str.count()` 활용
```python
count = str(num).count('3') + str(num).count('6') + str(num).count('9')
if count > 0:
    print('-' * count)
else:
    print(num)
```

#### 4. SWEA_1204 - 최빈수 구하기 (D2)
- **핵심**: 딕셔너리로 빈도수 카운팅
- **주의**: 최빈수가 여러 개일 때 가장 큰 숫자 출력
```python
from collections import Counter
counter = Counter(scores)
max_count = max(counter.values())
result = max([k for k, v in counter.items() if v == max_count])
```

#### 5. SWEA_1285 - 아름이의 돌 던지기 (D2)
- **핵심**: 절댓값 최솟값 찾기 및 개수 세기
- **팁**: `min()`, `abs()` 활용
```python
min_dist = min(abs(x) for x in distances)
count = sum(1 for x in distances if abs(x) == min_dist)
```

#### 6. SWEA_1217 - 거듭 제곱 (D3)
- **핵심**: 재귀 함수로 N^M 구현
- **팁**: Base case와 재귀 호출 명확히 하기
```python
def power(n, m):
    if m == 0:
        return 1
    return n * power(n, m - 1)
```

---

### 🚀 A형 수준 문제 공략법

#### 1. SWEA_2112 - 보호 필름 (D4)
- **난이도**: ★★★★☆
- **핵심 알고리즘**: DFS + 백트래킹
- **전략**:
  1. 각 행에 대해 약품을 투입하지 않음 / A 투입 / B 투입 3가지 선택
  2. 백트래킹으로 최소 투입 횟수 찾기
  3. 성능 검사 함수 구현 (연속 K개 이상)
- **가지치기**: 현재 투입 횟수가 최솟값보다 크면 중단

**핵심 로직**:
```python
def check(film):
    # 각 열에서 연속 K개 이상 확인
    for col in range(W):
        is_valid = False
        for row in range(D - K + 1):
            if all(film[row + k][col] == film[row][col] for k in range(K)):
                is_valid = True
                break
        if not is_valid:
            return False
    return True

def dfs(depth, count):
    global min_count
    if count >= min_count:  # 가지치기
        return
    if check(film):
        min_count = min(min_count, count)
        return
    if depth == D:
        return
    
    # 약품 투입 안 함
    dfs(depth + 1, count)
    
    # A 투입
    original = film[depth][:]
    film[depth] = [0] * W
    dfs(depth + 1, count + 1)
    
    # B 투입
    film[depth] = [1] * W
    dfs(depth + 1, count + 1)
    
    # 복원
    film[depth] = original
```

#### 2. SWEA_4014 - 활주로 건설 (D4)
- **난이도**: ★★★★☆
- **핵심 알고리즘**: 시뮬레이션
- **전략**:
  1. 가로/세로 각각 확인
  2. 높이 차이가 1일 때만 경사로 설치 가능
  3. 경사로 길이 X만큼 평탄한지 체크
- **주의사항**: 이미 경사로가 설치된 곳 중복 체크

**핵심 로직**:
```python
def check_runway(line):
    installed = [False] * N
    
    for i in range(N - 1):
        if line[i] == line[i + 1]:
            continue
        
        # 높이 차이가 2 이상이면 불가능
        if abs(line[i] - line[i + 1]) > 1:
            return False
        
        # 내려가는 경사로
        if line[i] > line[i + 1]:
            for j in range(i + 1, i + 1 + X):
                if j >= N or line[j] != line[i + 1] or installed[j]:
                    return False
                installed[j] = True
        
        # 올라가는 경사로
        else:
            for j in range(i, i - X, -1):
                if j < 0 or line[j] != line[i] or installed[j]:
                    return False
                installed[j] = True
    
    return True
```

#### 3. SWEA_5644 - 무선 충전 (D4)
- **난이도**: ★★★★☆
- **핵심 알고리즘**: 시뮬레이션 + 완전탐색
- **전략**:
  1. A와 B가 매 시간 이동
  2. 각 위치에서 충전 가능한 BC 찾기 (거리 계산)
  3. A, B가 선택할 수 있는 모든 BC 조합 확인
  4. 최대 충전량 선택
- **핵심**: 같은 BC를 동시에 선택하면 충전량 절반씩

**핵심 로직**:
```python
def get_charge(ax, ay, bx, by):
    # A와 B가 충전 가능한 BC 찾기
    a_bc = []
    b_bc = []
    
    for i, (x, y, c, p) in enumerate(BCs):
        if abs(ax - x) + abs(ay - y) <= c:
            a_bc.append(i)
        if abs(bx - x) + abs(by - y) <= c:
            b_bc.append(i)
    
    # BC가 없으면 0 추가
    if not a_bc:
        a_bc.append(-1)
    if not b_bc:
        b_bc.append(-1)
    
    # 모든 조합 확인
    max_charge = 0
    for a_idx in a_bc:
        for b_idx in b_bc:
            charge = 0
            if a_idx == b_idx and a_idx != -1:
                # 같은 BC 선택시 절반씩
                charge = BCs[a_idx][3]
            else:
                if a_idx != -1:
                    charge += BCs[a_idx][3]
                if b_idx != -1:
                    charge += BCs[b_idx][3]
            max_charge = max(max_charge, charge)
    
    return max_charge
```

---

## 🎯 주차별 목표

### Day 1-2: IM 기본 다지기
- SWEA_1966, 1945, 1926 해결
- 기본 구현 + 정렬 복습
- **목표 시간**: 각 20-30분

### Day 3-4: IM 심화
- SWEA_1204, 1285, 1217 해결
- 해시맵 + 재귀 마스터
- **목표 시간**: 각 30-40분

### Day 5-7: A형 도전
- SWEA_2112, 4014, 5644 해결
- 백트래킹 + 시뮬레이션 종합 연습
- **목표 시간**: 각 1.5-2시간

---

## 📊 예상 소요 시간

| 난이도 | 문제 수 | 예상 시간/문제 | 총 소요 시간 |
|--------|---------|---------------|-------------|
| D2 (IM) | 5개 | 20-30분 | 2-2.5시간 |
| D3 (IM) | 1개 | 40-60분 | 1시간 |
| D4 (A형) | 3개 | 1.5-2시간 | 5-6시간 |

**주간 총 예상 시간**: 8-9.5시간

---

## 🔥 추천 학습 순서

### 초급자 (IM 집중)
```
1. SWEA_1966 → 2. SWEA_1926 → 3. SWEA_1945 
→ 4. SWEA_1204 → 5. SWEA_1285 → 6. SWEA_1217
→ 7. SWEA_4014 (도전)
```

### 중급자 (균형)
```
1. SWEA_1966 → 2. SWEA_1204 → 3. SWEA_1217 
→ 4. SWEA_4014 → 5. SWEA_2112 
→ 나머지 IM 문제들 빠르게 해결
```

### 고급자 (A형 집중)
```
1. IM 문제 6개 빠르게 해결 (3-4시간)
→ 2. SWEA_2112 → 3. SWEA_4014 → 4. SWEA_5644
→ 코드 최적화 및 리팩토링
```

---

## ✨ 이번 주 특징

### 🆕 새로운 점
- **모든 문제가 새로운 문제**: 지금까지 풀지 않았던 문제들로 구성
- **IM 실전 감각**: 빠른 구현 능력 향상
- **A형 핵심 유형**: 백트래킹 + 시뮬레이션 집중 연습

### 🎯 학습 효과
1. **IM 대비**: 기본 구현/정렬/재귀 완벽 마스터
2. **A형 대비**: 복잡한 시뮬레이션 문제 해결 능력 향상
3. **실전 감각**: 제한 시간 내 빠른 구현 연습

---

## 💪 성공 전략

### ✅ 해야 할 것
- IM 문제는 30분 안에 해결하기
- A형 문제는 충분한 시간 투자 (2시간 이상 OK)
- 틀려도 괜찮으니 스스로 디버깅해보기
- 다른 멤버 코드와 비교하며 학습
- 코드 리뷰 적극 참여하기

### ❌ 하지 말아야 할 것
- IM 문제에 너무 오래 고민하지 않기
- A형 문제를 포기하지 않기
- 문제를 대충 읽고 바로 코딩하지 않기
- 같은 방법만 고집하지 않기

---

## 📚 필수 알고리즘 템플릿

### 백트래킹 기본 템플릿
```python
def backtrack(depth, state):
    global answer
    
    # 가지치기
    if is_pruning_condition(state):
        return
    
    # 목표 달성
    if is_goal(state):
        answer = update_answer(answer, state)
        return
    
    # 종료 조건
    if depth == MAX_DEPTH:
        return
    
    # 선택 시도
    for choice in get_choices(state):
        # 선택 적용
        apply_choice(state, choice)
        
        # 재귀 호출
        backtrack(depth + 1, state)
        
        # 선택 취소 (백트래킹)
        undo_choice(state, choice)
```

### 시뮬레이션 기본 템플릿
```python
# 2차원 배열 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0 <= nx < N and 0 <= ny < M:
                # 처리 로직
                pass
```

---

## 💬 이번 주 회고
(주차 완료 후 작성)

### 어려웠던 점
- 

### 새로 배운 점
- 

### 다음 주 목표
-

---

**"새로운 문제로 실력을 한 단계 업그레이드하자! 🚀"**