# scripts/update_progress.py - README 자동 생성 버전
import os
import re
import json
from datetime import datetime, date
from collections import defaultdict

# 스터디 멤버 리스트
MEMBERS = [
    "김강연",
    "홍길동", 
    "김철수",
    "이영희",
    "박민수"
]

def find_all_week_folders():
    """모든 주차 폴더 찾기"""
    week_folders = []
    
    try:
        items = os.listdir('.')
        print(f"📂 루트 디렉토리 내용: {items}")
        
        for item in items:
            if os.path.isdir(item):
                # 월 + 주차 패턴 확인 (예: 8월3주차, 8월4주차)
                if re.match(r'\d+월\d+주차', item):
                    week_folders.append(item)
                    print(f"  ✅ 주차 폴더 발견: {item}")
    except Exception as e:
        print(f"❌ 폴더 검색 오류: {e}")
    
    return sorted(week_folders)

def get_target_week_folder():
    """대상 주차 폴더 결정"""
    week_folders = find_all_week_folders()
    
    if not week_folders:
        print("❌ 주차 폴더를 찾을 수 없습니다.")
        return None
    
    # 가장 최근 폴더 사용
    target_folder = week_folders[-1]
    print(f"🎯 대상 폴더: {target_folder}")
    return target_folder

def ensure_readme_exists(week_folder):
    """README.md 파일이 없으면 생성"""
    if not week_folder:
        return None
    
    readme_path = os.path.join(week_folder, 'README.md')
    
    if os.path.exists(readme_path):
        print(f"✅ README 파일 존재: {readme_path}")
        return readme_path
    
    print(f"📝 README.md 파일을 생성합니다: {readme_path}")
    
    # 주차에서 월과 주차 번호 추출
    month_match = re.match(r'(\d+)월(\d+)주차', week_folder)
    if month_match:
        month = month_match.group(1)
        week = month_match.group(2)
        period_start = f"2024.{month.zfill(2)}.20"  # 임시 날짜
        period_end = f"2024.{month.zfill(2)}.26"    # 임시 날짜
    else:
        period_start = "2024.08.20"
        period_end = "2024.08.26"
    
    # 기본 README 내용 생성
    content = f"""# {week_folder}

## 📅 기간: {period_start} ~ {period_end}

## 🎯 주제: 재귀 (Recursion)

---

## 📝 문제 목록

### 8월 20일 (화)
| 번호 | 문제명 | 난이도 | 분류 | 링크 |
|------|---------|--------|------|------|
| 27433 | 팩토리얼2 | Bronze V | 필수 | [링크](https://www.acmicpc.net/problem/27433) |
| 10870 | 피보나치 수 5 | Bronze II | 필수 | [링크](https://www.acmicpc.net/problem/10870) |
| 25501 | 재귀의 귀재 | Silver V | 선택 | [링크](https://www.acmicpc.net/problem/25501) |
| 24060 | 알고리즘 수업-병합 정렬 1 | Silver II | 선택 | [링크](https://www.acmicpc.net/problem/24060) |
| 4779 | 칸토어 집합 | Silver III | 선택 | [링크](https://www.acmicpc.net/problem/4779) |
| 2447 | 별 찍기 - 10 | Gold V | 선택 | [링크](https://www.acmicpc.net/problem/2447) |
| 11729 | 하노이 탑 이동 순서 | Gold V | 선택 | [링크](https://www.acmicpc.net/problem/11729) |

---

## 📊 진행 현황

(자동으로 업데이트됩니다)

---

## 💬 이번 주 회고
(주차 완료 후 작성)

### 어려웠던 점
- 

### 새로 배운 점
- 

### 다음 주 목표
-
"""
    
    try:
        # 주차 폴더가 없으면 생성
        if not os.path.exists(week_folder):
            os.makedirs(week_folder)
            print(f"📁 주차 폴더 생성: {week_folder}")
        
        # README 파일 생성
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ README.md 생성 완료: {readme_path}")
        return readme_path
        
    except Exception as e:
        print(f"❌ README 생성 실패: {e}")
        return None

def calculate_member_progress():
    """각 멤버별 진행률 계산"""
    week_folder = get_target_week_folder()
    
    if not week_folder:
        # 빈 진행률 반환
        return {member: {'solved': 0, 'total': 0, 'percentage': 0, 'status': '📈'} for member in MEMBERS}
    
    member_stats = defaultdict(lambda: {'solved': 0, 'total': 0})
    
    try:
        # 주차 폴더가 없으면 생성
        if not os.path.exists(week_folder):
            os.makedirs(week_folder)
            print(f"📁 주차 폴더 생성: {week_folder}")
        
        items = os.listdir(week_folder)
        print(f"📅 {week_folder} 내용: {items}")
        
        # 날짜 폴더들 확인 (4자리 숫자: 0820, 0821 등)
        date_folders = [item for item in items if item.isdigit() and len(item) == 4]
        print(f"📅 날짜 폴더들: {date_folders}")
        
        # 날짜 폴더가 없으면 기본 폴더 생성
        if not date_folders:
            default_date = "0820"
            date_path = os.path.join(week_folder, default_date)
            if not os.path.exists(date_path):
                os.makedirs(date_path)
                print(f"📁 기본 날짜 폴더 생성: {default_date}")
            date_folders = [default_date]
        
        for date_folder in date_folders:
            date_path = os.path.join(week_folder, date_folder)
            
            if os.path.isdir(date_path):
                print(f"📅 날짜 폴더 확인: {date_folder}")
                
                # 해당 날짜의 문제 수 계산
                day_problems = count_problems_for_day(date_path)
                print(f"   📝 문제 수: {day_problems}")
                
                # 각 멤버별 해결 현황
                for member in MEMBERS:
                    try:
                        files = os.listdir(date_path)
                        member_files = [f for f in files if member in f and f.endswith('.py')]
                        solved_count = len(member_files)
                        
                        member_stats[member]['solved'] += solved_count
                        member_stats[member]['total'] += day_problems
                        
                        print(f"   👤 {member}: {solved_count}개 해결")
                        
                    except Exception as e:
                        print(f"   ⚠️  {member} 확인 오류: {e}")
                        
    except Exception as e:
        print(f"❌ 진행률 계산 오류: {e}")
    
    # 진행률 계산 및 상태 결정
    progress = {}
    for member in MEMBERS:
        solved = member_stats[member]['solved']
        total = member_stats[member]['total']
        percentage = round((solved / total) * 100, 1) if total > 0 else 0
        
        # 상태 아이콘
        if percentage >= 90:
            status = "🔥"
        elif percentage >= 70:
            status = "⚡"
        elif percentage >= 50:
            status = "💪"
        else:
            status = "📈"
        
        progress[member] = {
            'solved': solved,
            'total': total,
            'percentage': percentage,
            'status': status
        }
    
    return progress

def count_problems_for_day(date_path):
    """특정 날짜의 문제 수 계산"""
    if not os.path.exists(date_path):
        return 3  # 기본값
    
    try:
        files = os.listdir(date_path)
        
        # 파일이 없으면 기본값 반환
        if not files:
            return 3
        
        # 첫 번째 멤버의 파일 수로 계산
        for member in MEMBERS:
            member_files = [f for f in files if member in f and f.endswith('.py')]
            if member_files:
                return len(member_files)
        
        # 고유 문제 번호로 계산
        problem_numbers = set()
        for file in files:
            if file.endswith('.py'):
                match = re.search(r'BOJ_(\d+)_', file)
                if match:
                    problem_numbers.add(match.group(1))
        
        return len(problem_numbers) if problem_numbers else 3  # 기본값
        
    except Exception as e:
        print(f"⚠️  {date_path} 문제 수 계산 오류: {e}")
        return 3  # 기본값

def generate_progress_section(progress):
    """진행률 섹션 생성"""
    lines = []
    lines.append("### 📊 참여자별 현황")
    lines.append("| 이름 | 해결 문제 | 진행률 | 상태 |")
    lines.append("|------|-----------|--------|------|")
    
    for member, data in progress.items():
        line = f"| {member} | {data['solved']}/{data['total']} | {data['percentage']}% | {data['status']} |"
        lines.append(line)
    
    # 전체 통계
    total_solved = sum(data['solved'] for data in progress.values())
    total_problems = sum(data['total'] for data in progress.values())
    avg_percentage = round(sum(data['percentage'] for data in progress.values()) / len(progress), 1) if progress else 0
    
    lines.append("")
    lines.append("### 📈 전체 통계")
    lines.append(f"- **총 해결 문제**: {total_solved}개")
    lines.append(f"- **평균 진행률**: {avg_percentage}%")
    lines.append(f"- **업데이트 시간**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    return "\n".join(lines)

def update_readme_with_progress(progress):
    """README 파일 업데이트"""
    week_folder = get_target_week_folder()
    
    if not week_folder:
        print("❌ 대상 폴더를 찾을 수 없습니다.")
        return False
    
    # README 파일 존재 확인 및 생성
    readme_path = ensure_readme_exists(week_folder)
    
    if not readme_path:
        print("❌ README 파일을 생성할 수 없습니다.")
        return False
    
    try:
        # 기존 내용 읽기
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 새로운 진행률 섹션
        new_progress = generate_progress_section(progress)
        
        # 기존 진행률 섹션 찾기 및 교체
        pattern = r'### 📊 참여자별 현황.*?(?=###|---|\Z)'
        
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, new_progress, content, flags=re.DOTALL)
            print("🔄 기존 진행률 섹션 업데이트")
        else:
            # "## 📊 진행 현황" 섹션 찾아서 교체
            progress_pattern = r'## 📊 진행 현황.*?(?=##|---|\Z)'
            if re.search(progress_pattern, content, re.DOTALL):
                replacement = f"## 📊 진행 현황\n\n{new_progress}\n"
                content = re.sub(progress_pattern, replacement, content, flags=re.DOTALL)
                print("🔄 진행 현황 섹션 업데이트")
            else:
                content += f"\n\n---\n\n## 📊 진행 현황\n\n{new_progress}\n"
                print("➕ 새로운 진행률 섹션 추가")
        
        # 파일 저장
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ README 업데이트 완료: {readme_path}")
        return True
        
    except Exception as e:
        print(f"❌ README 업데이트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False

def save_progress_log(progress):
    """진행률 로그 저장"""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    today = datetime.now().strftime("%Y%m%d")
    log_data = {
        'date': today,
        'week_folder': get_target_week_folder(),
        'progress': progress,
        'timestamp': datetime.now().isoformat()
    }
    
    log_file = f"{log_dir}/progress_log_{today}.json"
    
    try:
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)
        print(f"💾 로그 저장: {log_file}")
    except Exception as e:
        print(f"❌ 로그 저장 실패: {e}")

if __name__ == "__main__":
    print("📈 진행률 업데이트 시작!")
    
    try:
        # 현재 폴더 구조 확인
        week_folders = find_all_week_folders()
        target_folder = get_target_week_folder()
        
        print(f"🎯 발견된 주차 폴더들: {week_folders}")
        print(f"🎯 대상 폴더: {target_folder}")
        
        if target_folder:
            progress = calculate_member_progress()
            
            print("📊 계산된 진행률:")
            for member, data in progress.items():
                print(f"  {data['status']} {member}: {data['solved']}/{data['total']} ({data['percentage']}%)")
            
            # README 업데이트
            if update_readme_with_progress(progress):
                save_progress_log(progress)
                print("✅ 진행률 업데이트 완료!")
            else:
                print("❌ README 업데이트 실패")
        else:
            print("❌ 대상 폴더를 찾을 수 없습니다.")
            # 기본 폴더 생성 시도
            default_week = "8월3주차"
            print(f"📁 기본 폴더 생성 시도: {default_week}")
            
            if not os.path.exists(default_week):
                os.makedirs(default_week)
                print(f"✅ 기본 폴더 생성: {default_week}")
            
            # 기본 진행률로 README 생성
            default_progress = {member: {'solved': 0, 'total': 3, 'percentage': 0, 'status': '📈'} for member in MEMBERS}
            readme_path = ensure_readme_exists(default_week)
            
            if readme_path and update_readme_with_progress(default_progress):
                save_progress_log(default_progress)
                print("✅ 기본 설정으로 진행률 업데이트 완료!")
            
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()