# 10월 2주차

## 📅 기간: 2025.10.08 ~ 2025.10.12

## 🎯 주제: 삼성 SW 역량 테스트 심화 (IM + A형 고급)

---

## 📝 문제 목록

### 🔰 IM 수준 문제 (6개)

| 번호 | 문제명 | 난이도 | 분류 | 추천 이유 | 링크 |
|------|---------|--------|------|-----------|------|
| SWEA_1928 | Base64 Decoder | D2 | 문자열/인코딩 | 문자열 변환 및 비트 연산 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PR4DKAG0DFAUq) |
| SWEA_1859 | 백만 장자 프로젝트 | D2 | Greedy | 역방향 탐색 전략 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc) |
| SWEA_1940 | 가랏! RC카! | D2 | 시뮬레이션 | 가속도 시뮬레이션 구현 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjMgaALgDFAUq) |
| SWEA_1948 | 날짜 계산기 | D2 | 구현/날짜 | 날짜 간격 계산 로직 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PnnU6AOsDFAUq) |
| SWEA_2805 | 농작물 수확하기 | D3 | 구현/2차원배열 | 다이아몬드 모양 영역 탐색 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB) |
| SWEA_1215 | 회문1 | D3 | 문자열/완전탐색 | 회문 판별 알고리즘 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi) |

### 🏆 A형 수준 문제 (3개)

| 번호 | 문제명 | 난이도 | 분류 | 추천 이유 | 링크 |
|------|---------|--------|------|-----------|------|
| SWEA_1767 | 프로세서 연결하기 | D4 | 백트래킹/DFS | 최적화 백트래킹 심화 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf) |
| SWEA_2117 | 홈 방범 서비스 | D4 | BFS/시뮬레이션 | 다이아몬드 범위 BFS | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu) |
| SWEA_2383 | 점심 식사시간 | D4 | 시뮬레이션/조합 | 복잡한 시뮬레이션 구현 | [링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl) |

---

## 📊 진행 현황

| 멤버 | 진행률 | 풀이 문제 수 | 비고 |
|------|--------|-------------|------|
| 김강연 | 0.0% ⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0/9 | ⏳ |
| 신재혁 | 44.4% 🟩🟩🟩🟩⬜⬜⬜⬜⬜ | 4/9 | ⏳ |
| 오창민 | 44.4% 🟩🟩🟩🟩⬜⬜⬜⬜⬜ | 4/9 | ⏳ |
| 송민경 | 0.0% ⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0/9 | ⏳ |
| 최재각 | 0.0% ⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0/9 | ⏳ |

**마지막 업데이트**: 2025-10-21 08:52

---

## 💡 학습 포인트

### 📚 IM 수준 문제 공략법

#### 1. SWEA_1928 - Base64 Decoder (D2)
- **핵심**: Base64 디코딩 원리 이해
- **Python 활용**: `base64` 라이브러리 사용
- **시간 복잡도**: O(N)

**접근법**:
```python
import base64

encoded = input().strip()
decoded = base64.b64decode(encoded).decode('utf-8')
print(decoded)
```

**수동 구현 (심화)**:
```python
# Base64 문자 테이블
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def decode_base64(s):
    binary = ""
    # 각 문자를 6비트로 변환
    for c in s:
        if c != '=':
            binary += format(table.index(c), '06b')
    
    # 8비트씩 잘라서 문자로 변환
    result = ""
    for i in range(0, len(binary), 8):
        if i + 8 <= len(binary):
            result += chr(int(binary[i:i+8], 2))
    
    return result
```

#### 2. SWEA_1859 - 백만 장자 프로젝트 (D2)
- **핵심**: 뒤에서부터 탐색하며 최대값 갱신
- **시간 복잡도**: O(N)
- **주의**: 앞에서부터 풀면 시간 초과!

**전략**:
```python
# 핵심 아이디어: 뒤에서부터 최대값 추적
prices = [list of prices]
max_price = 0
profit = 0

for i in range(len(prices) - 1, -1, -1):
    if prices[i] > max_price:
        max_price = prices[i]
    else:
        profit += max_price - prices[i]

print(profit)
```

**왜 역방향?**
- 미래의 최고가를 알고 있으면 그때 팔면 됨
- 현재가 < 미래 최고가 → 지금 사서 나중에 팔기
- 현재가 >= 미래 최고가 → 최고가 갱신

#### 3. SWEA_1940 - 가랏! RC카! (D2)
- **핵심**: 속도와 거리 시뮬레이션
- **주의**: 속도가 0 미만이 되지 않도록 처리

**시뮬레이션 로직**:
```python
speed = 0
distance = 0

for command in commands:
    if command == 0:  # 유지
        pass
    elif command == 1:  # 가속
        speed += acceleration
    elif command == 2:  # 감속
        speed = max(0, speed - deceleration)
    
    distance += speed

print(distance)
```

#### 4. SWEA_1948 - 날짜 계산기 (D2)
- **핵심**: 월별 일수를 고려한 날짜 계산
- **팁**: 리스트로 각 월의 일수 저장

**접근법**:
```python
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def count_days(m1, d1, m2, d2):
    total = 0
    
    # 같은 월인 경우
    if m1 == m2:
        return d2 - d1 + 1
    
    # 첫 달의 남은 날
    total += days_in_month[m1] - d1 + 1
    
    # 중간 달들
    for m in range(m1 + 1, m2):
        total += days_in_month[m]
    
    # 마지막 달
    total += d2
    
    return total
```

#### 5. SWEA_2805 - 농작물 수확하기 (D3)
- **핵심**: 다이아몬드(마름모) 영역 탐색
- **전략**: 중앙을 기준으로 거리 계산

**다이아몬드 영역 탐색**:
```python
N = int(input())
farm = [list(map(int, input())) for _ in range(N)]

center = N // 2
total = 0

for i in range(N):
    # 중앙으로부터의 거리
    distance = abs(i - center)
    
    # 각 행에서 수확 가능한 범위
    start = center - (center - distance)
    end = center + (center - distance)
    
    for j in range(start, end + 1):
        total += farm[i][j]

print(total)
```

**패턴 이해**:
```
N=5, center=2일 때:
행0: distance=2, 범위=[2,2] (1개)
행1: distance=1, 범위=[1,3] (3개)
행2: distance=0, 범위=[0,4] (5개)
행3: distance=1, 범위=[1,3] (3개)
행4: distance=2, 범위=[2,2] (1개)
```

#### 6. SWEA_1215 - 회문1 (D3)
- **핵심**: 가로/세로 모든 부분 문자열 회문 검사
- **시간 복잡도**: O(N² × M) (N: 배열 크기, M: 회문 길이)

**회문 검사 최적화**:
```python
def is_palindrome(s):
    return s == s[::-1]

def count_palindromes(board, length):
    count = 0
    N = len(board)
    
    # 가로 검사
    for i in range(N):
        for j in range(N - length + 1):
            word = ''.join(board[i][j:j+length])
            if is_palindrome(word):
                count += 1
    
    # 세로 검사
    for i in range(N - length + 1):
        for j in range(N):
            word = ''.join(board[i+k][j] for k in range(length))
            if is_palindrome(word):
                count += 1
    
    return count
```

---

### 🚀 A형 수준 문제 공략법

#### 1. SWEA_1767 - 프로세서 연결하기 (D4)
- **난이도**: ★★★★★
- **핵심 알고리즘**: 백트래킹 + 최적화
- **목표**: 최대한 많은 프로세서를 연결하되, 전선 길이는 최소화

**전략**:
1. 가장자리에 있는 프로세서는 이미 연결됨 (제외)
2. 각 프로세서마다 4방향 + 연결 안 함 (5가지 선택)
3. 백트래킹으로 모든 경우 탐색
4. 가지치기: 연결된 프로세서 수가 현재 최대보다 적으면 중단

**핵심 로직**:
```python
def can_connect(x, y, direction):
    """해당 방향으로 연결 가능한지 확인"""
    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy
    
    while 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] != 0:
            return False, []
        nx += dx
        ny += dy
    
    # 연결 가능한 좌표 리스트 반환
    path = []
    nx, ny = x + dx, y + dy
    while 0 <= nx < N and 0 <= ny < N:
        path.append((nx, ny))
        nx += dx
        ny += dy
    
    return True, path

def dfs(idx, connected, wire_length):
    global max_connected, min_wire
    
    # 모든 프로세서 처리 완료
    if idx == len(processors):
        if connected > max_connected:
            max_connected = connected
            min_wire = wire_length
        elif connected == max_connected:
            min_wire = min(min_wire, wire_length)
        return
    
    # 가지치기: 남은 프로세서 모두 연결해도 최대값 못 넘으면 중단
    if connected + (len(processors) - idx) < max_connected:
        return
    
    x, y = processors[idx]
    
    # 각 방향 시도
    for direction in range(4):
        possible, path = can_connect(x, y, direction)
        
        if possible:
            # 전선 설치
            for px, py in path:
                board[px][py] = 2
            
            # 재귀 호출
            dfs(idx + 1, connected + 1, wire_length + len(path))
            
            # 전선 제거 (백트래킹)
            for px, py in path:
                board[px][py] = 0
    
    # 연결 안 하는 경우
    dfs(idx + 1, connected, wire_length)
```

**최적화 팁**:
- 가장자리 프로세서 먼저 제외
- 불가능한 프로세서 파악 (4방향 모두 막힌 경우)
- 가지치기 강화 (남은 프로세서로 최대값 도달 불가능하면 중단)

#### 2. SWEA_2117 - 홈 방범 서비스 (D4)
- **난이도**: ★★★★☆
- **핵심 알고리즘**: BFS + 다이아몬드 범위
- **목표**: 손해를 보지 않으면서 최대 서비스 집 수

**전략**:
1. 모든 위치에서 서비스 영역 K를 1부터 증가시키며 확인
2. 각 K에 대해 다이아몬드 범위 내 집 개수 계산
3. 비용 계산: K² + (K-1)²
4. 수익 >= 비용인 경우만 카운트

**다이아몬드 범위 계산**:
```python
def get_houses_in_range(cx, cy, k):
    """중심 (cx, cy)에서 거리 K 이내 집 개수"""
    count = 0
    
    for i in range(N):
        for j in range(N):
            # 맨해튼 거리 계산
            distance = abs(i - cx) + abs(j - cy)
            
            if distance < k and city[i][j] == 1:
                count += 1
    
    return count

def solve():
    max_houses = 0
    
    # 모든 위치에서 시도
    for i in range(N):
        for j in range(N):
            # K를 1부터 최대까지 증가
            for k in range(1, N + 2):
                # 운영 비용
                cost = k * k + (k - 1) * (k - 1)
                
                # 서비스 가능한 집 수
                houses = get_houses_in_range(i, j, k)
                
                # 수익
                profit = houses * M
                
                # 손해를 보지 않으면서 최대 집 수
                if profit >= cost:
                    max_houses = max(max_houses, houses)
    
    return max_houses
```

**최적화**:
- BFS로 거리별 집 개수 누적 계산
- K의 최댓값 제한 (N+2면 충분)
- 손해 보는 순간 해당 위치의 K 증가 중단

#### 3. SWEA_2383 - 점심 식사시간 (D4)
- **난이도**: ★★★★★
- **핵심 알고리즘**: 조합 + 시뮬레이션
- **목표**: 모든 사람이 계단을 내려가는 최소 시간

**전략**:
1. 사람들을 두 계단으로 나누는 모든 경우의 수 (2^N)
2. 각 경우마다 시뮬레이션 실행
3. 계단 규칙:
   - 계단 입구까지 이동 시간 = 맨해튼 거리
   - 계단 입구 도착 후 1분 대기
   - 계단 내려가는 시간 = 계단 길이
   - 계단에는 최대 3명까지만

**시뮬레이션 로직**:
```python
def simulate(people, stairs, assignment):
    """
    assignment[i] = 0 or 1 (어느 계단으로 갈지)
    """
    stair_info = [
        {'pos': stairs[0], 'length': stairs[0][2], 'using': []},
        {'pos': stairs[1], 'length': stairs[1][2], 'using': []}
    ]
    
    # 각 사람의 계단 도착 시간 계산
    arrivals = [[] for _ in range(2)]
    for i, person in enumerate(people):
        stair_idx = assignment[i]
        sx, sy = stair_info[stair_idx]['pos'][:2]
        px, py = person
        
        # 이동 시간 + 1분 대기
        arrival_time = abs(px - sx) + abs(py - sy) + 1
        arrivals[stair_idx].append(arrival_time)
    
    # 각 계단별로 시뮬레이션
    max_time = 0
    for stair_idx in range(2):
        if not arrivals[stair_idx]:
            continue
        
        arrivals[stair_idx].sort()
        length = stair_info[stair_idx]['length']
        
        # 계단 사용 중인 사람들 (종료 시간 저장)
        using = []
        
        for arrival in arrivals[stair_idx]:
            # 계단이 비어있으면 바로 사용
            if len(using) < 3:
                using.append(arrival + length)
            else:
                # 가장 빨리 끝나는 사람 찾기
                using.sort()
                earliest_finish = using[0]
                
                # 도착 시간과 계단 비는 시간 중 늦은 시간부터 시작
                start_time = max(arrival, earliest_finish)
                using[0] = start_time + length
            
            max_time = max(max_time, max(using))
    
    return max_time

def solve():
    min_time = float('inf')
    
    # 사람들을 두 계단으로 나누는 모든 경우
    for mask in range(1 << len(people)):
        assignment = []
        for i in range(len(people)):
            assignment.append((mask >> i) & 1)
        
        time = simulate(people, stairs, assignment)
        min_time = min(min_time, time)
    
    return min_time
```

---

## 🎯 주차별 목표

### Day 1-2: IM 기초 (문자열/구현)
- SWEA_1928, 1859, 1940 해결
- Base64, Greedy, 시뮬레이션 연습
- **목표 시간**: 각 30분

### Day 3-4: IM 심화 (배열/탐색)
- SWEA_1948, 2805, 1215 해결
- 2차원 배열 탐색 마스터
- **목표 시간**: 각 40-50분

### Day 5-7: A형 고급 (백트래킹/시뮬레이션)
- SWEA_1767, 2117, 2383 해결
- 복잡한 최적화 문제 해결
- **목표 시간**: 각 2-3시간

---

## 📊 예상 소요 시간

| 난이도 | 문제 수 | 예상 시간/문제 | 총 소요 시간 |
|--------|---------|---------------|-------------|
| D2 (IM) | 4개 | 30-40분 | 2-2.5시간 |
| D3 (IM) | 2개 | 50-60분 | 2시간 |
| D4 (A형) | 3개 | 2-3시간 | 7-9시간 |

**주간 총 예상 시간**: 11-13.5시간

---

## 🔥 추천 학습 순서

### 초급자 (IM 집중)
```
1. SWEA_1940 → 2. SWEA_1948 → 3. SWEA_1928 
→ 4. SWEA_1859 → 5. SWEA_2805 → 6. SWEA_1215
→ 7. SWEA_2117 (도전)
```

### 중급자 (균형)
```
1. SWEA_1859 → 2. SWEA_2805 → 3. SWEA_1215 
→ 4. SWEA_2117 → 5. SWEA_1767
→ 나머지 IM 문제들 빠르게 해결
```

### 고급자 (A형 집중)
```
1. IM 문제 6개 빠르게 해결 (3-4시간)
→ 2. SWEA_1767 → 3. SWEA_2383 → 4. SWEA_2117
→ 코드 최적화 및 다양한 풀이 시도
```

---

## ✨ 이번 주 특징

### 🆕 핵심 포인트
- **Greedy 전략**: 역방향 탐색 기법 (백만 장자)
- **다이아몬드 범위**: 맨해튼 거리 기반 영역 탐색
- **복잡한 시뮬레이션**: 다중 객체 상태 관리
- **최적화 백트래킹**: 가지치기 전략 심화

### 🎯 학습 효과
1. **IM 실전**: 다양한 알고리즘 유형 경험
2. **A형 심화**: 실전급 난이도 문제 도전
3. **최적화 능력**: 시간/공간 복잡도 개선 연습

---

## 💪 성공 전략

### ✅ 이번 주 집중 사항
- **역방향 사고**: 뒤에서부터 탐색하는 전략
- **범위 계산**: 다이아몬드 영역 정확히 파악
- **시뮬레이션 구현**: 복잡한 조건 체계적으로 처리
- **백트래킹 최적화**: 불필요한 탐색 줄이기

### ❌ 주의사항
- **시간 초과 주의**: 특히 백만 장자 문제
- **범위 계산 실수**: 다이아몬드 영역 정확히
- **시뮬레이션 버그**: 엣지 케이스 꼼꼼히 확인
- **백트래킹 복원**: 상태 되돌리기 빠뜨리지 않기

---

## 📚 핵심 알고리즘 템플릿

### 역방향 Greedy 템플릿
```python
def reverse_greedy(arr):
    """뒤에서부터 최적값 찾기"""
    result = 0
    max_value = arr[-1]
    
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= max_value:
            max_value = arr[i]
        else:
            result += max_value - arr[i]
    
    return result
```

### 다이아몬드 범위 탐색 템플릿
```python
def diamond_range(cx, cy, k):
    """중심 (cx, cy)에서 거리 k 이내 좌표들"""
    result = []
    
    for i in range(N):
        for j in range(M):
            # 맨해튼 거리
            distance = abs(i - cx) + abs(j - cy)
            if distance < k:
                result.append((i, j))
    
    return result
```

### 최적화 백트래킹 템플릿
```python
def optimized_backtrack(idx, current, best):
    """가지치기 강화 백트래킹"""
    global answer
    
    # 가지치기: 현재까지 결과가 최선보다 나쁘면 중단
    if current < best:
        return
    
    # 가지치기: 남은 선택으로 최선 달성 불가능하면 중단
    if current + remaining_potential(idx) < answer:
        return
    
    # 목표 달성
    if idx == target:
        answer = max(answer, current)
        return
    
    # 선택 시도
    for choice in get_choices(idx):
        apply(choice)
        optimized_backtrack(idx + 1, new_current, best)
        undo(choice)
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

## 🔍 참고 자료

### 다이아몬드 범위 시각화
```
K=3인 경우:
    2
  1 1 1
0 0 0 0 0
  1 1 1
    2

맨해튼 거리 < 3인 모든 점
```

### 시뮬레이션 디버깅 팁
1. 각 시간대별 상태 출력
2. 작은 테스트 케이스로 검증
3. 경계 조건 꼼꼼히 확인
4. 상태 복원 정확히 구현

---

**"한 단계 더 깊이 파고들어 실력을 완성하자! 💪"**