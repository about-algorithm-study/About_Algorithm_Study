# Algorithm_Study
# 🚀 About 알고리즘 스터디

# 🚀 5인 알고리즘 스터디


## 🎯 주차별 학습 계획


## 🚨규칙

## ✅ 파일 생성 및 업로드 규칙
1. 매주, 매일 새로운 디렉토리를 생성합니다. ex) 8월3주차/0820, 8월4주차 ...
```bash
mkdir 8월3주차
cd 8월3주차

mkdir 0820
```



2. 디렉토리 안에 문제 디텍토리를 만듭니다. ex) BOJ_1000

```bash
mkdir BOJ_1000
```

3. 문제 디렉토리 안에 해당 주차의 문제들을 `BOJ_1000_홍길동.py`의 형식으로 업로드 합니다.

4. 최종적인 경로는 `8월3주차/BOJ_1000/0820/BOJ_1000_홍길동.py`입니다.

### 📝 커밋 규칙

### 파일명 규칙
```
플랫폼_문제번호_본인이름.py
예시: BOJ_1000_김철수.py, PRO_12345_이영희.py
```

### 커밋 메시지 규칙
```bash
# 새로운 문제 해결시
git commit -m "solve: BOJ_1000_김철수 - A+B 문제해결"

# 코드 수정시
git commit -m "fix: BOJ_1000_김철수 - 시간복잡도 개선"

# 추가 풀이시
git commit -m "add: BOJ_1000_김철수 - 다른 방법으로 재풀이"
```

### 브랜치 규칙
- `master`: 완성된 코드만 올리는 브랜치
- 개인 브랜치: `feature/이름` (예: `feature/김철수`)

## 🔄 Git 사용법 (초보자용)

### 1. 최초 설정 (한 번만)
```bash
# Git 사용자 정보 설정
git config --global user.name "본인이름"
git config --global user.email "본인이메일@example.com"

# 레포지토리 클론
git clone https://github.com/Kimkangyeon-17/Algorithm_Study.git
cd Algorithm_Study

# 원격 저장소 확인
git remote -v
```

### 2. 매일 작업하기 전 (중요!)
```bash
# 항상 최신 버전으로 업데이트
git pull origin master

# 혹시 충돌이 났다면
git stash  # 내 작업 임시 저장
git pull origin master
git stash pop  # 임시 저장한 작업 복원
```

### 3. 문제 풀고 업로드하기
```bash
# 1단계: 파일 추가 확인
git status  # 변경된 파일 확인

# 2단계: 파일 스테이징
git add .  # 모든 변경사항 추가
# 또는
git add 8월3주차/0820/BOJ_1000/BOJ_1000_김철수.py  # 특정 파일만 추가

# 3단계: 커밋
git commit -m "solve: BOJ_1000_김철수 - A+B 문제해결"

# 4단계: 원격 저장소에 업로드
git push origin master
```

### 4. 충돌 해결하기
```bash
# push 실패시 (다른 사람이 먼저 올린 경우)
git pull origin master  # 최신 버전 받기
# 자동 머지가 안되면 수동으로 파일 수정
git add .
git commit -m "fix: 충돌 해결"
git push origin master
```

### 5. 실수했을 때
```bash
# 마지막 커밋 취소 (파일은 유지)
git reset --soft HEAD~1

# 파일까지 모두 되돌리기 (위험!)
git reset --hard HEAD~1

# 특정 파일만 되돌리기
git checkout HEAD -- 파일명.py
```

## ⚠️ 주의사항

### DO ✅
- 매일 `git pull`을 먼저 실행하기
- 커밋 메시지는 명확하게 작성하기
- 자신의 폴더에만 파일 업로드하기
- 문제 풀이 전 다른 사람 코드 보지 않기
- 막히면 팀원들과 상의하기

### DON'T ❌
- 다른 사람 파일 수정하지 않기
- `git push --force` 절대 사용하지 않기
- 대용량 파일(이미지, 동영상) 업로드하지 않기
- 개인정보가 담긴 파일 업로드하지 않기
- 커밋 없이 `git pull` 하지 않기

## 📚 코딩 컨벤션

---
**"꾸준함이 실력이다! 함께 성장하는 알고리즘 스터디! 🚀"**