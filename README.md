# Algorithm_Study
# 🚀 About 알고리즘 스터디

5명이 함께하는 일일 알고리즘 문제 풀이 스터디입니다!

## 🤖 스터디 멤버

| 이름 | GitHub | 주 언어 |
|------ |-------------|---------|
| 김강연 | [@Kimkangyeon-17](https://github.com/Kimkangyeon-17) | Python |
| 신재혁 | [@Jaehyeok-Seen](https://github.com/Jaehyeok-Seen) | Python |
| 오창민 | [@mm-sj](https://github.com/mm-sj) | Python |
| 송민경 | [@Ssongnya](https://github.com/Ssongnya) | Python |
| 최재각 | [@rerak](https://github.com/rerak) | Python |

## 📋 스터디 진행 방식
- **매일**: 정해진 주제의 문제들을 각자 풀이
- **매주**: 새로운 주제 선정 및 문제 목록 업데이트
- **코드 리뷰**: 서로의 풀이법 공유 및 피드백

---

## 🚨 규칙

### ✅ 디렉토리 및 파일 생성 규칙

#### 1. 주차별 디렉토리 생성
```bash
mkdir 8월3주차
cd 8월3주차
mkdir 0820  # 날짜별 폴더
```

#### 2. 최종 파일 구조
```
Algorithm_Study/
├── 8월3주차/
│   ├── README.md                    # 이번 주 문제 목록
│   └── 0820/                       # 날짜별 폴더
│       ├── BOJ_27433_홍길동.py     # 개인별 풀이
│       ├── BOJ_27433_김철수.py
│       ├── BOJ_10870_홍길동.py
│       └── ...
└── 8월4주차/
    ├── README.md
    └── 0826/
        └── ...
```

#### 3. 파일명 규칙
```
플랫폼_문제번호_본인이름.py
예시: BOJ_1000_김철수.py, PRO_12345_이영희.py
```

### 📝 커밋 규칙

```bash
# 새로운 문제 해결시
git commit -m "solve: BOJ_1000_김철수 - A+B"

# 코드 수정시  
git commit -m "fix: BOJ_1000_김철수 - 시간복잡도 개선"

# 다른 풀이 추가시
git commit -m "add: BOJ_1000_김철수 - 다른 접근법"

# 주차별 README 추가시
git commit -m "docs: 8월3주차 문제 목록 추가"
```

### 🌿 브랜치 전략 (권장)

#### Option 1: 개인 브랜치 사용 (권장)
```bash
# 개인 브랜치 생성 및 이동
git checkout -b feature/김철수

# 작업 후 커밋
git add .
git commit -m "solve: BOJ_1000_김철수 - A+B"

# 개인 브랜치에 푸시
git push origin feature/김철수

# master에 머지 (온라인에서 Pull Request 생성)
```

#### Option 2: Master 브랜치 직접 사용 (초보자용)
- 모든 작업을 master에서 진행
- **반드시** 매번 `git pull` 먼저 실행

---

## 🔄 Git 사용법 (초보자용)

### 📥 최초 설정 (한 번만)
```bash
# 1. Git 사용자 정보 설정
git config --global user.name "본인이름"
git config --global user.email "본인이메일@example.com"

# 2. 레포지토리 클론
git clone https://github.com/Kimkangyeon-17/Algorithm_Study.git
cd Algorithm_Study

# 3. 원격 저장소 확인
git remote -v
```

### 📤 매일 문제 풀이 업로드하기

#### Step 1: 항상 최신 버전으로 업데이트 (중요!)
```bash
git pull origin master
```

#### Step 2: 파일 작성 및 확인
```bash
# 오늘 날짜 폴더에 파일 작성 후
git status  # 변경된 파일 확인 (빨간색으로 표시됨)
```

#### Step 3: 파일 스테이징
```bash
git add .  # 모든 변경사항 추가
# 또는 특정 파일만
git add 8월3주차/0820/BOJ_27433_김철수.py
```

#### Step 4: 커밋
```bash
git commit -m "solve: BOJ_27433_김철수 - 팩토리얼2"
```

#### Step 5: 업로드
```bash
git push origin master
```

### 🚨 충돌 해결하기

#### push가 실패했을 때
```bash
# 에러 메시지: "Updates were rejected because..."
git pull origin master  # 다른 사람의 변경사항 받기

# 자동 머지 성공시
git push origin master

# 충돌 발생시 (Conflict 메시지가 나올 때)
# 1. VS Code나 텍스트 에디터로 충돌 파일 열기
# 2. <<<<<<< , ======= , >>>>>>> 표시 부분 수정
# 3. 수정 후 저장
git add .
git commit -m "fix: 충돌 해결"
git push origin master
```

### 🔙 실수했을 때 되돌리기

```bash
# 마지막 커밋 취소 (파일은 그대로 유지)
git reset --soft HEAD~1

# 스테이징 취소 (commit 전)
git reset HEAD 파일명.py

# 파일 변경사항 취소 (저장하지 않은 변경사항)
git checkout -- 파일명.py

# 특정 커밋으로 되돌리기 (위험! 팀원과 상의 후)
git reset --hard 커밋해시
```

---

## ⚠️ 중요 주의사항

### ✅ 꼭 지켜주세요!
- **매일 작업 전 `git pull origin master` 필수!**
- 자신의 이름으로만 파일 생성하기
- 커밋 메시지는 위 형식 따르기
- 다른 사람 파일은 절대 수정하지 않기
- 막히면 팀원들과 상의하기
- 하루에 한 번은 반드시 업로드하기

### ❌ 절대 하지 마세요!
- `git push --force` 사용 금지
- 다른 사람 파일 삭제/수정 금지
- 대용량 파일 업로드 금지
- 개인정보 포함된 파일 업로드 금지
- 커밋 없이 pull 하지 않기

### 🆘 문제 상황별 해결책

| 상황 | 해결책 |
|------|--------|
| push가 안 돼요 | `git pull origin master` 후 다시 push |
| 파일이 사라졌어요 | `git status`로 확인 후 `git checkout -- 파일명` |
| 잘못 커밋했어요 | `git reset --soft HEAD~1`로 커밋 취소 |
| 충돌이 났어요 | 충돌 파일 수정 후 add → commit → push |
| 실수로 삭제했어요 | 팀원과 상의 후 복구 진행 |

---



**"꾸준함이 실력이다! 함께 성장하는 알고리즘 스터디! 🚀"**