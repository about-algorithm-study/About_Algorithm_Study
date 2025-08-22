# scripts/update_cumulative_daily_progress.py - 누적 일별 진행률 시스템
import os
import re
import json
from datetime import datetime, date
from collections import defaultdict

# 스터디 멤버 리스트 (실제 이름으로 업데이트)
MEMBERS = ["김강연", "신재혁", "오창민", "송민경", "최재각"]
MEMBER_MAPPING = {
    "김강연": "kky",
    "신재혁": "sjh", 
    "오창민": "ocm",
    "송민경": "smk",
    "최재각": "cjg"
}

def find_week_folders():
    """모든 주차 폴더 찾기"""
    week_folders = []
    try:
        items = os.listdir(".")
        for item in items:
            if os.path.isdir(item) and re.match(r"\d+월\d+주차", item):
                week_folders.append(item)
    except Exception as e:
        print(f"❌ 폴더 검색 오류: {e}")
    return sorted(week_folders)

def get_target_week_folder():
    """대상 주차 폴더 결정"""
    week_folders = find_week_folders()
    if not week_folders:
        return None
    return week_folders[-1]  # 가장 최근 폴더

def get_all_date_folders(week_folder):
    """주차 폴더 내의 모든 날짜 폴더 찾기"""
    if not os.path.exists(week_folder):
        return []
    
    try:
        items = os.listdir(week_folder)
        # 4자리 숫자 패턴의 날짜 폴더만 추출 (0820, 0821, 0822 등)
        date_folders = [
            item for item in items 
            if item.isdigit() and len(item) == 4 and os.path.isdir(os.path.join(week_folder, item))
        ]
        return sorted(date_folders)
    except Exception as e:
        print(f"❌ 날짜 폴더 찾기 오류: {e}")
        return []

def get_problems_by_date(week_folder, target_date):
    """특정 날짜의 문제 목록 및 개수 가져오기"""
    date_path = os.path.join(week_folder, target_date)
    
    if not os.path.exists(date_path):
        return [], 0
    
    try:
        items = os.listdir(date_path)
        problem_folders = [
            item for item in items 
            if os.path.isdir(os.path.join(date_path, item)) 
            and (item.startswith("BOJ_") or item.startswith("PRO_") or item.startswith("SWEA_"))
        ]
        
        return problem_folders, len(problem_folders)
        
    except Exception as e:
        print(f"❌ {date_path} 읽기 오류: {e}")
        return [], 0

def calculate_daily_progress_for_date(week_folder, target_date):
    """특정 날짜의 일별 진행률 계산"""
    problem_folders, total_problems = get_problems_by_date(week_folder, target_date)
    
    if total_problems == 0:
        return {
            member: {"solved": 0, "total": 0, "percentage": 0.0, "status": "📈"}
            for member in MEMBERS
        }
    
    # 각 멤버별 해결 현황 계산
    progress = {}
    date_path = os.path.join(week_folder, target_date)
    
    for member in MEMBERS:
        solved_count = 0
        member_id = MEMBER_MAPPING[member]
        
        for problem_folder in problem_folders:
            problem_path = os.path.join(date_path, problem_folder)
            
            if os.path.isdir(problem_path):
                try:
                    files = os.listdir(problem_path)
                    # 멤버의 파일이 있는지 확인 (이름 또는 이니셜로)
                    member_files = [
                        f for f in files 
                        if (member in f or member_id in f) and f.endswith(".py")
                    ]
                    
                    if member_files:
                        solved_count += 1
                        
                except Exception as e:
                    print(f"⚠️ {problem_folder} 확인 오류: {e}")
        
        # 진행률 계산
        percentage = round((solved_count / total_problems) * 100, 1) if total_problems > 0 else 0.0
        
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
            "solved": solved_count,
            "total": total_problems,
            "percentage": percentage,
            "status": status
        }
    
    return progress

def calculate_all_daily_progress(week_folder):
    """모든 날짜의 진행률 계산"""
    date_folders = get_all_date_folders(week_folder)
    
    if not date_folders:
        print(f"⚠️ {week_folder}에 날짜 폴더가 없습니다.")
        return {}
    
    print(f"📅 발견된 날짜 폴더들: {date_folders}")
    
    all_progress = {}
    
    for date_folder in date_folders:
        print(f"\n📊 {date_folder} 진행률 계산 중...")
        daily_progress = calculate_daily_progress_for_date(week_folder, date_folder)
        all_progress[date_folder] = daily_progress
        
        # 해당 날짜 요약 출력
        total_solved = sum(data["solved"] for data in daily_progress.values())
        total_problems = daily_progress[MEMBERS[0]]["total"] if daily_progress else 0
        avg_percentage = (
            round(sum(data["percentage"] for data in daily_progress.values()) / len(MEMBERS), 1)
            if daily_progress else 0
        )
        
        print(f"   📈 {date_folder}: 총 {total_solved}/{total_problems * len(MEMBERS)}개 해결, 평균 {avg_percentage}%")
    
    return all_progress

def format_date_korean(date_str):
    """날짜 문자열을 한국어 형식으로 변환 (0820 -> 8월 20일)"""
    try:
        month = int(date_str[:2])
        day = int(date_str[2:])
        return f"{month}월 {day}일"
    except:
        return date_str

def generate_cumulative_progress_section(all_progress):
    """누적 일별 진행률 섹션 생성"""
    if not all_progress:
        return "## 📊 진행 현황\n\n⚠️ 아직 진행된 날짜가 없습니다."
    
    lines = []
    lines.append("## 📊 진행 현황")
    lines.append("")
    
    # 각 날짜별 진행률 표시
    for date_folder in sorted(all_progress.keys()):
        date_korean = format_date_korean(date_folder)
        progress = all_progress[date_folder]
        
        # 해당 날짜의 통계 계산
        total_solved = sum(data["solved"] for data in progress.values())
        total_problems = progress[MEMBERS[0]]["total"] if progress else 0
        avg_percentage = (
            round(sum(data["percentage"] for data in progress.values()) / len(MEMBERS), 1)
            if progress else 0
        )
        
        lines.append(f"### 📅 {date_korean} ({date_folder})")
        
        if total_problems == 0:
            lines.append("⚠️ 이 날짜에는 문제가 없습니다.")
            lines.append("")
            continue
            
        lines.append("| 이름 | 해결 문제 | 진행률 | 상태 |")
        lines.append("|------|-----------|--------|------|")
        
        for member, data in progress.items():
            line = f"| {member} | {data['solved']}/{data['total']} | {data['percentage']}% | {data['status']} |"
            lines.append(line)
        
        lines.append("")
        lines.append(f"**📈 {date_korean} 통계**: 총 해결 {total_solved}개 / 평균 진행률 {avg_percentage}%")
        lines.append("")
    
    # 전체 주차 요약
    lines.append("---")
    lines.append("")
    lines.append("### 📈 주간 전체 통계")
    
    # 전체 통계 계산
    total_days = len(all_progress)
    all_solved = sum(
        sum(data["solved"] for data in day_progress.values())
        for day_progress in all_progress.values()
    )
    all_possible = sum(
        day_progress[MEMBERS[0]]["total"] * len(MEMBERS)
        for day_progress in all_progress.values()
        if day_progress
    )
    overall_avg = round((all_solved / all_possible) * 100, 1) if all_possible > 0 else 0
    
    lines.append(f"- **진행 일수**: {total_days}일")
    lines.append(f"- **전체 해결 문제**: {all_solved}개")
    lines.append(f"- **전체 평균 진행률**: {overall_avg}%")
    lines.append(f"- **업데이트 시간**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    return "\n".join(lines)

def update_readme_with_cumulative_progress(all_progress):
    """README 파일에 누적 일별 진행률 업데이트"""
    week_folder = get_target_week_folder()
    
    if not week_folder:
        print("❌ 대상 폴더를 찾을 수 없습니다.")
        return False
    
    readme_path = os.path.join(week_folder, "README.md")
    
    if not os.path.exists(readme_path):
        print(f"❌ README 파일을 찾을 수 없습니다: {readme_path}")
        return False
    
    try:
        # 기존 내용 읽기
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 새로운 누적 진행률 섹션 생성
        new_progress = generate_cumulative_progress_section(all_progress)
        
        # 기존 진행 현황 섹션 찾기 및 교체
        progress_pattern = r"## 📊 진행 현황.*?(?=\n## |\n---|\Z)"
        
        if re.search(progress_pattern, content, re.DOTALL):
            # 기존 섹션 교체
            new_content = re.sub(
                progress_pattern, 
                new_progress, 
                content, 
                flags=re.DOTALL
            )
            print("🔄 기존 진행 현황 섹션을 누적 진행률로 교체 완료")
        else:
            # 새로운 섹션 추가 (회고 섹션 앞에)
            retrospect_start = content.find("## 💬 이번 주 회고")
            
            if retrospect_start != -1:
                before_retrospect = content[:retrospect_start]
                after_retrospect = content[retrospect_start:]
                new_content = f"{before_retrospect}\n{new_progress}\n\n{after_retrospect}"
            else:
                new_content = f"{content}\n\n---\n\n{new_progress}\n"
            
            print("➕ 새로운 누적 진행률 섹션 추가")
        
        # 파일 저장
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print(f"✅ README 누적 진행률 업데이트 완료: {readme_path}")
        return True
        
    except Exception as e:
        print(f"❌ README 업데이트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False

def save_cumulative_progress_log(all_progress):
    """누적 진행률 로그 저장"""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    today = datetime.now().strftime("%Y%m%d")
    log_data = {
        "date": today,
        "week_folder": get_target_week_folder(),
        "cumulative_daily_progress": all_progress,
        "timestamp": datetime.now().isoformat(),
        "file_structure_type": "cumulative_daily_progress_tracking"
    }
    
    log_file = os.path.join(log_dir, f"cumulative_progress_{today}.json")
    
    try:
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)
        print(f"💾 누적 진행률 로그 저장: {log_file}")
    except Exception as e:
        print(f"❌ 로그 저장 실패: {e}")

def main():
    print("📅 누적 일별 진행률 업데이트 시작!")
    
    try:
        week_folder = get_target_week_folder()
        if not week_folder:
            print("❌ 주차 폴더를 찾을 수 없습니다.")
            return
        
        print(f"🎯 대상 폴더: {week_folder}")
        
        # 모든 날짜의 진행률 계산
        all_progress = calculate_all_daily_progress(week_folder)
        
        if all_progress:
            # README 업데이트
            if update_readme_with_cumulative_progress(all_progress):
                save_cumulative_progress_log(all_progress)
                print("✅ 누적 일별 진행률 업데이트 완료!")
                
                # 최종 요약 출력
                print(f"\n📋 최종 요약:")
                print(f"   📅 총 진행 일수: {len(all_progress)}일")
                for date_folder in sorted(all_progress.keys()):
                    date_korean = format_date_korean(date_folder)
                    progress = all_progress[date_folder]
                    total_solved = sum(data["solved"] for data in progress.values())
                    total_problems = progress[MEMBERS[0]]["total"] if progress else 0
                    print(f"   📊 {date_korean}: {total_solved}/{total_problems * len(MEMBERS)}개 해결")
            else:
                print("❌ README 업데이트 실패")
        else:
            print(f"⚠️ {week_folder}에 진행률 데이터가 없습니다.")
            
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()