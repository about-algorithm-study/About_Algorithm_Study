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

def get_current_week_folder():
    """현재 주차 폴더명 반환"""
    today = date.today()
    month = today.month
    
    if today.day <= 7:
        week = 1
    elif today.day <= 14:
        week = 2
    elif today.day <= 21:
        week = 3
    else:
        week = 4
    
    return f"{month}월{week}주차"

def count_total_problems():
    """이번 주 전체 문제 수 계산"""
    week_folder = get_current_week_folder()
    
    if not os.path.exists(week_folder):
        return 0
    
    total_problems = 0
    
    # 각 날짜 폴더를 확인하여 문제 수 계산
    for item in os.listdir(week_folder):
        item_path = os.path.join(week_folder, item)
        
        # 날짜 폴더인지 확인 (MMDD 형식)
        if os.path.isdir(item_path) and item.isdigit() and len(item) == 4:
            # 해당 날짜의 README에서 문제 수 확인하거나
            # 실제 업로드된 파일 중 첫 번째 멤버의 파일 수로 계산
            day_problems = count_problems_for_day(item_path)
            total_problems += day_problems
    
    return total_problems

def count_problems_for_day(day_path):
    """특정 날짜의 문제 수 계산"""
    # 방법 1: 첫 번째 멤버가 올린 파일 수로 계산
    for member in MEMBERS:
        member_files = [f for f in os.listdir(day_path) if member in f and f.endswith('.py')]
        if member_files:
            return len(member_files)
    
    # 방법 2: 고유한 문제 번호 계산
    problem_numbers = set()
    for file in os.listdir(day_path):
        if file.endswith('.py'):
            # BOJ_27433_김강연.py 에서 27433 추출
            match = re.search(r'BOJ_(\d+)_', file)
            if match:
                problem_numbers.add(match.group(1))
    
    return len(problem_numbers) if problem_numbers else 3  # 기본값

def calculate_member_progress():
    """각 멤버별 진행률 계산"""
    week_folder = get_current_week_folder()
    
    if not os.path.exists(week_folder):
        print(f"❌ 주차 폴더가 존재하지 않습니다: {week_folder}")
        return {}
    
    member_stats = defaultdict(lambda: {'solved': 0, 'total': 0})
    
    # 각 날짜 폴더 확인
    for item in os.listdir(week_folder):
        item_path = os.path.join(week_folder, item)
        
        if os.path.isdir(item_path) and item.isdigit() and len(item) == 4:
            day_problems = count_problems_for_day(item_path)
            
            # 각 멤버별 해당 날짜 문제 해결 현황 확인
            for member in MEMBERS:
                member_files = [f for f in os.listdir(item_path) if member in f and f.endswith('.py')]
                
                member_stats[member]['solved'] += len(member_files)
                member_stats[member]['total'] += day_problems
    
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
    avg_percentage = round(sum(data['percentage'] for data in progress.values()) / len(progress), 1)
    
    table_lines.append("")
    table_lines.append("### 📈 전체 통계")
    table_lines.append(f"- **총 해결 문제**: {total_solved}개")
    table_lines.append(f"- **평균 진행률**: {avg_percentage}%")
    table_lines.append(f"- **업데이트 시간**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    return "\n".join(table_lines)

def update_readme_progress(progress):
    """README의 진행률 부분 업데이트"""
    week_folder = get_current_week_folder()
    readme_path = os.path.join(week_folder, "README.md")
    
    if not os.path.exists(readme_path):
        print(f"❌ README.md 파일이 존재하지 않습니다: {readme_path}")
        return False
    
    # 기존 README 읽기
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 새로운 진행률 테이블 생성
    new_progress_section = generate_progress_table(progress)
    
    # 기존 진행률 섹션 찾아서 교체
    # "### 📊 참여자별 현황" 부터 다음 "###" 섹션 전까지 교체
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
    
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)
    
    print(f"💾 진행률 로그 저장: {log_file}")

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