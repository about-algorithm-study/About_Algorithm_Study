# Algorithm_Study
# 🚀 About 알고리즘 스터디

5명이 함께하는 주간 알고리즘 문제 풀이 스터디입니다!

## 🤖 스터디 멤버

| 이름 | GitHub | 주 언어 |
|------|---------|---------|
| 김강연 | [@Kimkangyeon-17](https://github.com/Kimkangyeon-17) | Python |
| 신재혁 | [@Jaehyeok-Seen](https://github.com/Jaehyeok-Seen) | Python |
| 오창민 | [@mm-sj](https://github.com/mm-sj) | Python |
| 송민경 | [@Ssongnya](https://github.com/Ssongnya) | Python |
| 최재각 | [@rerak](https://github.com/rerak) | Python |

## 📋 스터디 진행 방식
- **매주**: 9문제 풀이 (주차별로 진행)
- **코드 리뷰**: 서로의 풀이법 공유 및 피드백
- **자동화**: GitHub Actions로 주간 진행률 자동 추적

---

## 🚨 규칙

### ✅ 디렉토리 및 파일 생성 규칙

#### 1. 주차별 디렉토리 생성
```bash
mkdir 9월1주차
cd 9월1주차
```

#### 2. 최종 파일 구조 (📁 간소화된 구조)
```
Algorithm_Study/
├── 9월1주차/
│   ├── README.md                    # 이번 주 문제 목록
│   ├── BOJ_27433/                   # 문제별 폴더
│   │   ├── BOJ_27433_kky.py        # 개인별 풀이
│   │   ├── BOJ_27433_sjh.py
│   │   └── BOJ_27433_ocm.py
│   ├── BOJ_10870/                   # 문제별 폴더
│   │   ├── BOJ_10870_kky.py
│   │   ├── BOJ_10870_smk.py
│   │   └── BOJ_10870_cjg.py
│   └── BOJ_2447/                    # 문제별 폴더
│       ├── BOJ_2447_kky.py
│       └── BOJ_2447_sjh.py
└── 9월2주차/
    ├── README.md
    ├── BOJ_1234/
    │   └── BOJ_1234_kky.py
    └── ...
```

#### 3. 파일명 및 폴더 규칙
```bash
# 폴더 구조
주차폴더/문제폴더/문제파일

# 파일명 규칙
플랫폼_문제번호_본인이니셜.py

# 예시
9월1주차/BOJ_27433/BOJ_27433_kky.py
9월1주차/BOJ_10870/BOJ_10870_sjh.py
9월1주차/PRO_12345/PRO_12345_ocm.py
```

#### 4. 폴더 생성 및 파일 작업 순서
```bash
# 1. 주차 폴더로 이동
cd 9월1주차

# 2. 문제별 폴더 생성
mkdir BOJ_27433
mkdir BOJ_10870

# 3. 해당 문제 폴더에 파일 생성
cd BOJ_27433
# 여기에 BOJ_27433_본인이니셜.py 파일 작성

cd ../BOJ_10870
# 여기에 BOJ_10870_본인이니셜.py 파일 작성
```

### 📝 커밋 규칙

```bash
# 새로운 문제 해결시
git commit -m "solve: BOJ_27433_kky"

# 코드 수정시  
git commit -m "fix: BOJ_27433_kky"

# 다른 풀이 추가시
git commit -m "add: BOJ_27433_kky"

# 주차별 README 추가시
git commit -m "docs: 9월1주차 문제 목록 추가"
```

### 🌿 브랜치 전략 (권장)

#### Option 1: 개인 브랜치 사용 (권장)
```bash
# 개인 브랜치 생성 및 이동
git checkout -b feature/본인이니셜
# 예: git checkout -b feature/kky

# 작업 후 커밋
git add .
git commit -m "solve: BOJ_27433_kky"

# 개인 브랜치에 푸시
git push origin feature/본인이니셜
# 예: git push origin feature/kky

# master에 머지 (온라인에서 Pull Request 생성)
```

---

# 🔥Git branch 관련 무조건 지켜야 하는 사항!!!!
- 문제 풀이 전 무조건 [브랜치 관리 가이드](docs/git_branch_file.md) 참고하기!!

## 📝 1단계: 주간 문제 풀이 워크플로우
- 오류 발생 시 [충돌 방지 가이드](docs/confliction_solution.md) 참고

### 2-1. 작업 시작 전 (매주 습관화!)
```bash
# 1) 개인 브랜치에 있는지 확인
git branch
# * feature/kky  ← 확인!

# 2) master의 최신 변경사항 가져오기
git checkout master
git pull origin master

# 3) 개인 브랜치로 돌아가서 master 변경사항 병합
git checkout feature/본인이니셜
# 예: git checkout feature/kky
git merge master
# 또는 git rebase master (더 깔끔한 히스토리)
```

### 2-2. 문제 풀이 및 커밋
```bash
# 문제 폴더 생성 및 파일 작성
cd 9월1주차
mkdir BOJ_10870  # 아직 없다면
cd BOJ_10870

# 본인 파일 작성
# BOJ_10870_kky.py 파일 생성하고 문제 풀이

# 커밋
git add .
git commit -m "solve: BOJ_10870_kky"
```

### 2-3. 개인 브랜치에 푸시
```bash
# 개인 브랜치에 푸시 (충돌 위험 0%)
git push origin feature/본인이니셜
# 예: git push origin feature/kky
```

### 2-4. Pull Request 생성
1. GitHub 웹사이트 접속
2. "Compare & pull request" 버튼 클릭
3. 제목: `solve: BOJ_10870_kky`
4. "Create pull request" 클릭

### 2-5. 자동 병합 또는 관리자 병합
- 충돌이 없으면 → "Merge pull request" 클릭
- 병합 완료!

---

## 🛡️ 3단계: 충돌 방지 규칙

### ✅ 절대 안전한 작업들
```bash
# 1. 본인 파일만 생성/수정
9월1주차/BOJ_10870/BOJ_10870_kky.py  ← 안전!

# 2. 개인 브랜치에서만 작업
git checkout feature/kky  ← 안전!

# 3. 개인 브랜치에만 푸시
git push origin feature/kky  ← 안전!
```

### ❌ 절대 하면 안 되는 것들
```bash
# 1. 다른 사람 파일 수정 금지
BOJ_10870_sjh.py  ← 절대 건드리지 말기!

# 2. master 브랜치에 직접 푸시 금지
git push origin master  ← 금지!

# 3. 다른 사람 브랜치에 푸시 금지
git push origin feature/sjh  ← 금지!
```

---

## 🔄 Git 사용법 (초보자용)

### 📥 최초 설정 (한 번만)
```bash
# 1. Git 사용자 정보 설정
git config --global user.name "본인이름"
git config --global user.email "본인이메일@example.com"

# 2. 레포지토리 클론
git clone https://github.com/about-algorithm-study/About_Algorithm_Study.git
cd Algorithm_Study

# 3. 원격 저장소 확인
git remote -v
```

### 📤 문제 풀이 업로드하기

#### Step 1: 항상 최신 버전으로 업데이트 (중요!)
```bash
git pull origin master
```

#### Step 2: 파일 작성 및 확인
```bash
# 문제별 폴더에 파일 작성 후
git status  # 변경된 파일 확인 (빨간색으로 표시됨)
```

#### Step 3: 파일 스테이징
```bash
git add .  # 모든 변경사항 추가
# 또는 특정 파일만
git add 9월1주차/BOJ_27433/BOJ_27433_본인이니셜.py
```

#### Step 4: 커밋
```bash
git commit -m "solve: BOJ_27433_본인이니셜"
```

#### Step 5: 업로드
```bash
git push origin feature/본인이니셜
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
- **매주 작업 전 `git pull origin master` 필수!**
- **문제별 폴더를 만들고 그 안에 파일 생성하기**
- 자신의 이니셜로만 파일 생성하기
- 커밋 메시지는 위 형식 따르기
- 다른 사람 파일은 절대 수정하지 않기
- 막히면 팀원들과 상의하기
- 주당 9문제 목표 달성!

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
| 폴더 구조가 헷갈려요 | 위의 파일 구조 예시 참고 |

---

## 📁 파일 구조의 장점

### 🎯 간소화된 구조의 장점
1. **단순함**: 주차별로만 관리해서 구조가 명확
2. **체계적 관리**: 문제별로 모든 풀이를 한 곳에 모음
3. **비교 용이**: 같은 문제의 다른 풀이법을 쉽게 비교
4. **확장 가능**: 추후 테스트 케이스, 설명 파일 등 추가 가능
5. **검색 편의**: 특정 문제의 모든 풀이를 빠르게 찾기 가능

### 📋 실제 작업 예시
```bash
# 이번 주 팩토리얼2 문제 풀기
cd Algorithm_Study/9월1주차
mkdir BOJ_27433                    # 문제 폴더 생성
cd BOJ_27433
# BOJ_27433_kky.py 파일 작성
git add .
git commit -m "solve: BOJ_27433_kky"
git push origin feature/kky
```






## 📈 전체 진행률 (누적)

**업데이트**: 2025-10-21 08:52

- 📅 총 7주차 진행
- 📝 전체 문제: 63개

### 👥 멤버별 누적 통계

| 순위 | 멤버 | 총 풀이 | 주평균 | 참여율 | 진행바 |
|------|------|---------|--------|--------|--------|
| 🥇 | 신재혁 | 7개 | 1.00개 | 11.1% | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| 🥈 | 오창민 | 7개 | 1.00개 | 11.1% | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| 🥉 | 김강연 | 3개 | 0.43개 | 4.8% | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| 4위 | 최재각 | 3개 | 0.43개 | 4.8% | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| 5위 | 송민경 | 0개 | 0.00개 | 0.0% | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |

### 📊 주차별 진행률


#### 10월1주차

| 멤버 | 풀이 수 | 진행률 |
|------|---------|--------|
| 김강연 | 3/9 | 33.3% ⏳ |
| 신재혁 | 3/9 | 33.3% ⏳ |
| 오창민 | 3/9 | 33.3% ⏳ |
| 송민경 | 0/9 | 0.0% ⏳ |
| 최재각 | 3/9 | 33.3% ⏳ |

#### 10월2주차

| 멤버 | 풀이 수 | 진행률 |
|------|---------|--------|
| 김강연 | 0/9 | 0.0% ⏳ |
| 신재혁 | 4/9 | 44.4% ⏳ |
| 오창민 | 4/9 | 44.4% ⏳ |
| 송민경 | 0/9 | 0.0% ⏳ |
| 최재각 | 0/9 | 0.0% ⏳ |

#### 8월3주차

| 멤버 | 풀이 수 | 진행률 |
|------|---------|--------|
| 김강연 | 0/9 | 0.0% ⏳ |
| 신재혁 | 0/9 | 0.0% ⏳ |
| 오창민 | 0/9 | 0.0% ⏳ |
| 송민경 | 0/9 | 0.0% ⏳ |
| 최재각 | 0/9 | 0.0% ⏳ |

#### 8월4주차

| 멤버 | 풀이 수 | 진행률 |
|------|---------|--------|
| 김강연 | 0/9 | 0.0% ⏳ |
| 신재혁 | 0/9 | 0.0% ⏳ |
| 오창민 | 0/9 | 0.0% ⏳ |
| 송민경 | 0/9 | 0.0% ⏳ |
| 최재각 | 0/9 | 0.0% ⏳ |

#### 9월1주차

| 멤버 | 풀이 수 | 진행률 |
|------|---------|--------|
| 김강연 | 0/9 | 0.0% ⏳ |
| 신재혁 | 0/9 | 0.0% ⏳ |
| 오창민 | 0/9 | 0.0% ⏳ |
| 송민경 | 0/9 | 0.0% ⏳ |
| 최재각 | 0/9 | 0.0% ⏳ |

#### 9월2주차

| 멤버 | 풀이 수 | 진행률 |
|------|---------|--------|
| 김강연 | 0/9 | 0.0% ⏳ |
| 신재혁 | 0/9 | 0.0% ⏳ |
| 오창민 | 0/9 | 0.0% ⏳ |
| 송민경 | 0/9 | 0.0% ⏳ |
| 최재각 | 0/9 | 0.0% ⏳ |

#### 9월3주차

| 멤버 | 풀이 수 | 진행률 |
|------|---------|--------|
| 김강연 | 0/9 | 0.0% ⏳ |
| 신재혁 | 0/9 | 0.0% ⏳ |
| 오창민 | 0/9 | 0.0% ⏳ |
| 송민경 | 0/9 | 0.0% ⏳ |
| 최재각 | 0/9 | 0.0% ⏳ |

---
