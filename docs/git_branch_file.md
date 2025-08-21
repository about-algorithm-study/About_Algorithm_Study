# 🌿 팀원용 브랜치 사용 가이드

## 🎯 브랜치가 이미 준비되어 있습니다!

팀장이 미리 각자의 전용 브랜치를 만들어두었습니다. 이제 각자 본인 브랜치에서만 작업하면 됩니다!

## 📥 처음 설정 (한 번만 하면 됨)

### 1단계: 원격 브랜치 정보 가져오기
```bash
git fetch origin
```

### 2단계: 본인 브랜치로 이동
```bash
# 본인 이름으로 된 브랜치로 이동
git checkout feature/kky  # 김강연의 경우
git checkout feature/sjh  # 신재혁의 경우
git checkout feature/ocm  # 오창민의 경우
git checkout feature/smk  # 송민경의 경우
git checkout feature/cjg  # 최재각의 경우
```

### 3단계: 브랜치 확인
```bash
git branch
# * feature/본인이니셜  ← 이렇게 나와야 함!
#   master
```

## 📝 매일 문제 풀이 방법

### ✅ 작업 시작 전 (매일 필수!)
```bash
# 1. 본인 브랜치에 있는지 확인
git branch
# * feature/본인이니셜  ← 확인!

# 2. master의 최신 변경사항 가져오기
git pull origin master

# 또는 더 안전한 방법:
git fetch origin
git merge origin/master
```

### ✅ 문제 풀이 및 업로드
```bash
# 1. 문제 풀이 (파일 생성/수정)
# 예: 8월3주차/0820/BOJ_10870/BOJ_10870_본인이니셜.py

# 2. 변경사항 확인
git status

# 3. 파일 추가
git add .

# 4. 커밋
git commit -m "solve: BOJ_10870_본인이니셜 - 피보나치 수 5"

# 5. 본인 브랜치에 푸시 (절대 안전!)
git push origin feature/본인이니셜
```

### ✅ Pull Request 생성
1. GitHub 웹사이트 접속
2. "Compare & pull request" 버튼 클릭
3. 제목: `solve: BOJ_10870_본인이니셜 - 피보나치 수 5`
4. "Create pull request" 클릭
5. 팀장이 병합해줄 때까지 대기

## 🛡️ 절대 안전한 이유

### ✅ 여러분이 할 수 있는 것들 (100% 안전)
- ✅ 본인 브랜치에서 작업
- ✅ 본인 이니셜이 포함된 파일만 생성/수정
- ✅ 본인 브랜치에 푸시
- ✅ Pull Request 생성

### ❌ 절대 하면 안 되는 것들
- ❌ master 브랜치에 직접 푸시
- ❌ 다른 사람 파일 수정
- ❌ 다른 사람 브랜치에 푸시

## 🆘 문제 상황 해결법

### "브랜치를 찾을 수 없어요"
```bash
# 원격 브랜치 정보 다시 가져오기
git fetch origin
git checkout feature/본인이니셜
```

### "충돌이 났어요"
```bash
# 충돌 파일을 VS Code로 열고 수정 후:
git add .
git commit -m "fix: 충돌 해결"
git push origin feature/본인이니셜
```

### "잘못된 브랜치에서 작업했어요"
```bash
# 팀장에게 문의하거나, 커밋을 올바른 브랜치로 이동
git log --oneline  # 커밋 해시 확인
git checkout feature/본인이니셜
git cherry-pick 커밋해시
```

## 📊 현재 상태 확인 명령어

```bash
# 현재 브랜치 확인
git branch

# 현재 상태 확인
git status

# 최근 커밋 히스토리 확인
git log --oneline -5

# 원격과의 동기화 상태 확인
git fetch origin
git status
```

## 🎉 장점

1. **충돌 위험 0%**: 각자 본인 브랜치에서만 작업
2. **실수 방지**: master에 직접 푸시할 수 없음
3. **안전한 실험**: 본인 브랜치에서 자유롭게 실험
4. **체계적 관리**: Pull Request를 통한 코드 리뷰
5. **쉬운 복구**: 실수해도 본인 브랜치만 영향

## 📞 도움이 필요할 때

- Git 명령어가 헷갈릴 때: 팀장에게 문의
- 브랜치 관련 문제: 팀장이 해결해 드립니다
- 막혔을 때: 주저하지 말고 물어보세요!

**🎯 핵심: 본인 브랜치에서만 작업하고, Pull Request로 공유하기!**