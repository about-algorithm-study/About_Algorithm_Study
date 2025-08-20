# scripts/update_progress.py
import os
import re
import json
from datetime import datetime, date
from collections import defaultdict

# 스터디 멤버 리스트 (daily_check.py와 동일하게)
MEMBERS = [
    "김강연",  # 실제 이름으로 변경
    "홍길동",  # 실제 이름으로 변경  
    "김철수",  # 실제 이름으로 변경
    "이영희",  # 실제 이름으로 변경
    "박민수"   # 실제 이름으로 변경
]

def find_week_folders():
    """현재 월의 모든 주차 폴더 찾기"""
    current_month = date.today().month
    week_folders = []
    
    for item in os.listdir('.'):
        if os.path.isdir(item) and f"{current_month}월" in item and "주차" in item:
            week_folders.append(item)
    
    return sorted(week_folders)

def get_current_week_folder():
    """현재 주차 폴더명 반환"""
    week_folders = find_week_folders()
    if week_folders:
        # 가장 최근 주차 반환
        return week_folders[-1]
    
    # 폴백: 계산된 주차
    today = date.today()
    month = today.month
    week_number = ((today.day - 1) // 7) + 1
    return f"{month}월{week_number}주차"

def count_problems_for_day(day_path):
    """특정 날짜의 문제 수 계산 - 개선된 버전"""
    if not os.path.exists(day_path):
        return 0
    
    try:
        files = os.listdir(day_path)
    except PermissionError:
        print(f"⚠️  {day_path} 접근 권한 없음")
        return 0
    
    # 방법 1: 첫 번째 멤버가 올린 파일 수로 계산
    for member in MEMBERS:
        member_files = [f for f in files if member in f and f.endswith('.py')]
        if member_files:
            return len(member_files)
    
    # 방법 2: 고유한 문제 번호 계산
    problem_numbers = set()
    for file in files:
        if file.endswith('.py'):
            # BOJ_27433_김강연.py 에서 27433 추출
            match = re.search(r'BOJ_(\d+)_', file)
            if match:
                problem_numbers.add(match.group(1))
    
    return len(problem_numbers) if problem_numbers else 3  # 기본값

def calculate_member_progress():
    """각 멤버별 진행률 계산 - 개선된 버전"""
    week_folder = get_current_week_folder()
    
    print(f"📁 대상 주차 폴더: {week_folder}")
    
    if not os.path.exists(week_folder):
        print(f"❌ 주차 폴더가 존재하지 않습니다: {week_folder}")
        # 빈 진행률 반환
        return {member: {'solved': 0, 'total': 0, 'percentage': 0, 'status': '📈'} for member in MEMBERS}
    
    member_stats = defaultdict(lambda: {'solved': 0, 'total': 0})
    
    try:
        items = os.listdir(week_folder)
        print(f"📂 폴더 내용: {items}")
    except Exception as e:
        print(f"❌ 폴더 읽기 오류: {e}")
        return {member: {'solved': 0, 'total': 0, 'percentage': 0, 'status': '📈'} for member in MEMBERS}
    
    # 각 날짜 폴더 확인
    for item in items:
        item_path = os.path.join(week_folder, item)
        
        if os.path.isdir(item_path) and (item.isdigit() and len(item) == 4):
            print(f"📅 날짜 폴더 확인: {item}")
            day_problems = count_problems_for_day(item_path)
            print(f"   문제 수: {day_problems}")
            
            # 각 멤버별 해당 날짜 문제 해결 현황 확인
            for member in MEMBERS:
                try:
                    member_files = [f for f in os.listdir(item_path) if member in f and f.endswith('.py')]
                    member_stats[member]['solved'] += len(member_files)
                    member_stats[member]['total'] += day_problems
                    print(f"   {member}: {len(member_files)}개 해결")
                except Exception as e:
                    print(f"   ⚠️  {member} 파일 확인 오류: {e}")
    
    # 진행률 계산
    progress = {}
    for member in MEMBERS:
        solved = member_stats[member]['solved']
        total = member_stats[member]['total']
        percentage = round((solved / total) * 100, 1) if total > 0 else 0
        
        # 상태 아이콘 결정
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

def generate_progress_table(progress):
    """진행률 테이블 생성"""
    table_lines = []
    table_lines.append("### 📊 참여자별 현황")
    table_lines.append("| 이름 | 해결 문제 | 진행률 | 상태 |")
    table_lines.append("|------|-----------|--------|------|")
    
    for member, data in progress.items():
        line = f"| {member} | {data['solved']}/{data['total']} | {data['percentage']}% | {data['status']} |"
        table_lines.append(line)
    
    # 전체 통계 추가
    total_solved = sum(data['solved'] for data in progress.values())
    total_problems = sum(data['total'] for data in progress.values())
    avg_percentage = round(sum(data['percentage'] for data in progress.values()) / len(progress), 1) if progress else 0
    
    table_lines.append("")
    table_lines.append("### 📈 전체 통계")
    table_lines.append(f"- **총 해결 문제**: {total_solved}개")
    table_lines.append(f"- **평균 진행률**: {avg_percentage}%")
    table_lines.append(f"- **업데이트 시간**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    return "\n".join(table_lines)

def update_readme_progress(progress):
    """README의 진행률 부분 업데이트 - 개선된 버전"""
    week_folder = get_current_week_folder()
    readme_path = os.path.join(week_folder, "README.md")
    
    print(f"📄 README 경로: {readme_path}")
    
    if not os.path.exists(readme_path):
        print(f"❌ README.md 파일이 존재하지 않습니다: {readme_path}")
        
        # README 파일이 없으면 생성
        try:
            create_initial_readme(week_folder)
            print(f"✅ 새 README.md 파일 생성: {readme_path}")
        except Exception as e:
            print(f"❌ README 생성 실패: {e}")
            return False
    
    try:
        # 기존 README 읽기
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 새로운 진행률 테이블 생성
        new_progress_section = generate_progress_table(progress)
        
        # 기존 진행률 섹션 찾아서 교체
        pattern = r'### 📊 참여자별 현황.*?(?=###|\Z)'
        
        if re.search(pattern, content, re.DOTALL):
            # 기존 섹션이 있으면 교체
            content = re.sub(pattern, new_progress_section, content, flags=re.DOTALL)
        else:
            # 기존 섹션이 없으면 끝에 추가
            content += f"\n\n---\n\n{new_progress_section}\n"
        
        # 파일에 다시 쓰기
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ README 업데이트 완료: {readme_path}")
        return True
        
    except Exception as e:
        print(f"❌ README 업데이트 실패: {e}")
        return False

def create_initial_readme(week_folder):
    """기본 README.md 파일 생성"""
    readme_path = os.path.join(week_folder, "README.md")
    
    content = f"""# {week_folder}

## 📅 기간: {datetime.now().strftime('%Y.%m.%d')} ~ 

## 🎯 주제: 알고리즘 문제 풀이

---

## 📝 문제 목록

(문제 목록을 여기에 추가하세요)

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
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

def save_progress_log(progress):
    """진행률 로그 저장"""
    today = datetime.now().strftime("%Y%m%d")
    log_dir = "logs"
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_data = {
        'date': today,
        'week_folder': get_current_week_folder(),
        'progress': progress,
        'timestamp': datetime.now().isoformat()
    }
    
    log_file = f"{log_dir}/progress_log_{today}.json"
    
    try:
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)
        
        print(f"💾 진행률 로그 저장: {log_file}")
    except Exception as e:
        print(f"❌ 진행률 로그 저장 실패: {e}")

if __name__ == "__main__":
    print("📈 진행률 업데이트 시작!")
    
    try:
        progress = calculate_member_progress()
        
        if progress:
            print("📊 계산된 진행률:")
            for member, data in progress.items():
                print(f"  {data['status']} {member}: {data['solved']}/{data['total']} ({data['percentage']}%)")
            
            # README 업데이트
            if update_readme_progress(progress):
                save_progress_log(progress)
                print("✅ 진행률 업데이트 완료!")
            else:
                print("❌ README 업데이트 실패")
        else:
            print("❌ 진행률 계산 실패")
            
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()