# 🌿 충돌 방지를 위한 브랜치 전략 완벽 가이드

## 🎯 전략 개요

각자 **개인 브랜치**에서 작업하고, **Pull Request**를 통해 master에 병합하는 방식으로 충돌을 완전히 방지!

```
master (메인)
├── feature/김강연 (김강연 전용)
├── feature/신재혁 (신재혁 전용)  
├── feature/오창민 (오창민 전용)
├── feature/송민경 (송민경 전용)
└── feature/최재각 (최재각 전용)
```

---

## 🚀 1단계: 초기 설정 (각자 한 번만)

### 1-1. 개인 브랜치 생성
```bash
# 최신 master로 업데이트
git checkout master
git pull origin master

# 개인 브랜치 생성 및 이동
git checkout -b feature/본인이름
# 예: git checkout -b feature/김강연

# 개인 브랜치를 원격에 푸시
git push -u origin feature/본인이름
```

### 1-2. 브랜치 확인
```bash
# 현재 브랜치 확인
git branch
# * feature/김강연  ← 현재 브랜치
#   master

# 원격 브랜치 확인
git branch -r
# origin/feature/김강연
# origin/master
```

---

## 📝 2단계: 일상적인 문제 풀이 워크플로우

### 2-1. 작업 시작 전 (매일 습관화!)
```bash
# 1) 개인 브랜치에 있는지 확인
git branch
# * feature/김강연  ← 확인!

# 2) master의 최신 변경사항 가져오기
git checkout master
git pull origin master

# 3) 개인 브랜치로 돌아가서 master 변경사항 병합
git checkout feature/본인이름
git merge master
# 또는 git rebase master (더 깔끔한 히스토리)
```

### 2-2. 문제 풀이 및 커밋
```bash
# 문제 폴더 생성 및 파일 작성
cd 8월3주차/0820
mkdir BOJ_10870  # 아직 없다면
cd BOJ_10870

# 본인 파일 작성
# BOJ_10870_김강연.py 파일 생성하고 문제 풀이

# 커밋
git add .
git commit -m "solve: BOJ_10870_김강연 - 피보나치 수 5"
```

### 2-3. 개인 브랜치에 푸시
```bash
# 개인 브랜치에 푸시 (충돌 위험 0%)
git push origin feature/본인이름
```

### 2-4. Pull Request 생성
1. GitHub 웹사이트 접속
2. "Compare & pull request" 버튼 클릭
3. 제목: `solve: BOJ_10870_김강연 - 피보나치 수 5`
4. "Create pull request" 클릭

### 2-5. 자동 병합 또는 관리자 병합
- 충돌이 없으면 → "Merge pull request" 클릭
- 병합 완료!

---

## 🛡️ 3단계: 충돌 방지 규칙

### ✅ 절대 안전한 작업들
```bash
# 1. 본인 파일만 생성/수정
8월3주차/0820/BOJ_10870/BOJ_10870_김강연.py  ← 안전!

# 2. 개인 브랜치에서만 작업
git checkout feature/김강연  ← 안전!

# 3. 개인 브랜치에만 푸시
git push origin feature/김강연  ← 안전!
```

### ❌ 절대 하면 안 되는 것들
```bash
# 1. 다른 사람 파일 수정 금지
BOJ_10870_신재혁.py  ← 절대 건드리지 말기!

# 2. master 브랜치에 직접 푸시 금지
git push origin master  ← 금지!

# 3. 다른 사람 브랜치에 푸시 금지
git push origin feature/신재혁  ← 금지!
```

---

## 🔄 4단계: 고급 시나리오 대처법

### 시나리오 1: 같은 문제를 동시에 풀 때
```
상황: 김강연과 신재혁이 동시에 BOJ_10870 문제를 풀고 있음

해결책:
1. 각자 개인 브랜치에서 작업
2. 각자 BOJ_10870 폴더 안에 본인 파일만 생성
   - BOJ_10870_김강연.py
   - BOJ_10870_신재혁.py
3. 각자 PR 생성 → 순서대로 병합
4. 결과: 충돌 없이 두 파일 모두 master에 존재!
```

### 시나리오 2: README 수정이 필요할 때
```
상황: README.md 파일을 수정해야 함

해결책:
1. 관리자(김강연)만 README 수정 권한
2. 다른 멤버들은 README 건드리지 않기
3. 또는 README 수정용 별도 브랜치 생성
```

### 시나리오 3: 새로운 주차 폴더 생성
```
상황: 8월4주차 폴더를 만들어야 함

해결책:
1. 관리자가 master에서 새 주차 폴더 생성
2. 다른 멤버들은 최신 master를 pull 받아서 동기화
3. 각자 개인 브랜치에 master 내용 병합
```

---

## 📋 5단계: 브랜치별 상태 관리

### 브랜치 상태 확인 명령어
```bash
# 모든 브랜치 목록
git branch -a

# 각 브랜치의 최신 커밋
git log --oneline --graph --all

# 개인 브랜치와 master 차이점 확인
git log master..feature/본인이름

# 현재 브랜치 상태
git status
```

### 정기적인 동기화 (권장: 주 2-3회)
```bash
# 1. master 최신화
git checkout master
git pull origin master

# 2. 개인 브랜치에 master 변경사항 반영
git checkout feature/본인이름
git merge master

# 3. 개인 브랜치 푸시
git push origin feature/본인이름
```

---

## 🆘 6단계: 문제 상황별 해결책

### 문제 1: "Your branch is behind" 메시지
```bash
# 해결책: master의 최신 변경사항 가져오기
git checkout master
git pull origin master
git checkout feature/본인이름
git merge master
```

### 문제 2: "Merge conflict" 발생
```bash
# 해결책: 충돌 파일 수정
1. VS Code로 충돌 파일 열기
2. <<<<<<< HEAD와 >>>>>>> 표시 부분 수정
3. git add 파일명
4. git commit -m "fix: 충돌 해결"
```

### 문제 3: 잘못된 브랜치에서 작업
```bash
# 해결책: 커밋을 올바른 브랜치로 이동
git log --oneline  # 커밋 해시 확인
git checkout feature/본인이름
git cherry-pick 커밋해시
```

### 문제 4: 개인 브랜치 삭제하고 다시 시작
```bash
# 로컬 브랜치 삭제
git checkout master
git branch -D feature/본인이름

# 원격 브랜치 삭제
git push origin --delete feature/본인이름

# 새로 시작
git checkout -b feature/본인이름
git push -u origin feature/본인이름
```

---

## 🎯 7단계: 팀 규칙 제안

### 파일 생성 규칙 (충돌 방지)
```
✅ 허용: 본인 이름이 포함된 파일만
BOJ_10870_김강연.py  ← OK
BOJ_10870_신재혁.py  ← OK

❌ 금지: 공통 파일 수정
README.md  ← 관리자만
.gitignore ← 관리자만
```

### PR 제목 규칙
```
solve: BOJ_10870_김강연 - 피보나치 수 5
fix: BOJ_10870_김강연 - 시간복잡도 개선
add: BOJ_10870_김강연 - 다른 접근법 추가
```

### 커밋 주기
```
권장: 문제 1개 풀 때마다 커밋 + 푸시 + PR
최대: 하루에 한 번은 반드시 푸시
```

---

## 🚀 8단계: GitHub Actions와의 연동

### 자동화 유지
```
master 브랜치: GitHub Actions 자동 실행 (일일 체크)
개인 브랜치: 자동화 실행 안 함 (불필요한 리소스 절약)
```

### PR 병합 후 자동 실행
```
1. 개인 브랜치에서 PR 생성
2. master에 병합
3. GitHub Actions 자동 실행
4. README 진행률 자동 업데이트
```

---

## ✨ 결론: 완벽한 충돌 방지!

이 전략을 따르면:
- ✅ **충돌 위험 0%**: 각자 본인 파일만 수정
- ✅ **안전한 협업**: PR을 통한 체계적 병합  
- ✅ **자동화 유지**: GitHub Actions 정상 작동
- ✅ **코드 리뷰 가능**: PR에서 서로 코드 확인
- ✅ **히스토리 깔끔**: 체계적인 커밋 관리

**"각자의 영역에서 안전하게 작업하고, 체계적으로 합치자!" 🎯**