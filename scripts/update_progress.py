# scripts/update_progress.py - 중복 추가 및 진행률 계산 오류 수정 버전
import os
import re
import json
from datetime import datetime, date
from collections import defaultdict

# 스터디 멤버 리스트 (실제 이름으로 업데이트)
MEMBERS = ["김강연", "신재혁", "오창민", "송민경", "최재각"]


def find_all_week_folders():
    """모든 주차 폴더 찾기"""
    week_folders = []

    try:
        items = os.listdir(".")
        print(f"📂 루트 디렉토리 내용: {items}")

        for item in items:
            if os.path.isdir(item):
                # 월 + 주차 패턴 확인 (예: 8월3주차, 8월4주차)
                if re.match(r"\d+월\d+주차", item):
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
    """README.md 파일 존재 확인"""
    if not week_folder:
        return None

    readme_path = os.path.join(week_folder, "README.md")

    print(f"🔍 README 파일 경로 확인: {readme_path}")
    print(f"🔍 파일 존재 여부: {os.path.exists(readme_path)}")

    if os.path.exists(readme_path):
        print(f"✅ README 파일 존재: {readme_path}")
        return readme_path

    print(f"❌ README.md 파일을 찾을 수 없습니다: {readme_path}")
    return None


def get_total_problems_from_readme(readme_path):
    """README에서 총 문제 수 파악"""
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 문제 목록 테이블에서 문제 수 계산
        # | 번호 | 문제명 | 난이도 | 분류 | 링크 | 형태의 테이블에서 계산
        pattern = r"\|\s*\d+\s*\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|"
        matches = re.findall(pattern, content)

        total_problems = len(matches)
        print(f"📝 README에서 파악한 총 문제 수: {total_problems}개")

        if total_problems == 0:
            # 백업 방법: BOJ_, PRO_ 등이 포함된 줄 수 세기
            problem_lines = [
                line for line in content.split("\n") if "BOJ" in line or "PRO" in line
            ]
            total_problems = len(
                [line for line in problem_lines if "|" in line and "http" in line]
            )
            print(f"📝 백업 방법으로 파악한 문제 수: {total_problems}개")

        return total_problems

    except Exception as e:
        print(f"❌ README에서 문제 수 파악 실패: {e}")
        return 0


def calculate_member_progress():
    """각 멤버별 진행률 계산 - 수정된 버전"""
    week_folder = get_target_week_folder()

    if not week_folder:
        return {
            member: {"solved": 0, "total": 0, "percentage": 0, "status": "📈"}
            for member in MEMBERS
        }

    # README에서 총 문제 수 파악
    readme_path = ensure_readme_exists(week_folder)
    total_problems = get_total_problems_from_readme(readme_path) if readme_path else 0

    print(f"🎯 이번 주 총 문제 수: {total_problems}개")

    member_stats = defaultdict(lambda: {"solved": 0, "total": total_problems})

    try:
        # 주차 폴더 존재 확인
        if not os.path.exists(week_folder):
            print(f"❌ 주차 폴더가 존재하지 않습니다: {week_folder}")
            return {
                member: {
                    "solved": 0,
                    "total": total_problems,
                    "percentage": 0,
                    "status": "📈",
                }
                for member in MEMBERS
            }

        items = os.listdir(week_folder)
        print(f"📅 {week_folder} 내용: {items}")

        # 날짜 폴더들 확인 (4자리 숫자: 0820, 0821 등)
        date_folders = [item for item in items if item.isdigit() and len(item) == 4]
        print(f"📅 날짜 폴더들: {date_folders}")

        # 각 멤버별 해결한 문제 집합 (중복 제거용)
        member_solved_problems = defaultdict(set)

        for date_folder in date_folders:
            date_path = os.path.join(week_folder, date_folder)

            if os.path.isdir(date_path):
                print(f"📅 날짜 폴더 확인: {date_folder}")

                # 해당 날짜의 문제별 폴더들 찾기
                problem_folders = find_problem_folders(date_path)

                print(f"   📁 문제 폴더들: {problem_folders}")

                # 각 멤버별 해결 현황 계산
                for member in MEMBERS:
                    solved_problems = get_member_solved_problems(
                        date_path, member, problem_folders
                    )
                    member_solved_problems[member].update(solved_problems)

                    print(
                        f"   👤 {member}: {len(solved_problems)}개 해결 ({solved_problems})"
                    )

        # 최종 통계 계산
        for member in MEMBERS:
            solved_count = len(member_solved_problems[member])
            member_stats[member]["solved"] = solved_count
            member_stats[member]["total"] = total_problems

            print(f"🏆 {member} 최종: {solved_count}/{total_problems}개 해결")

    except Exception as e:
        print(f"❌ 진행률 계산 오류: {e}")
        import traceback

        traceback.print_exc()

    # 진행률 계산 및 상태 결정
    progress = {}
    for member in MEMBERS:
        solved = member_stats[member]["solved"]
        total = member_stats[member]["total"]
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
            "solved": solved,
            "total": total,
            "percentage": percentage,
            "status": status,
        }

    return progress


def find_problem_folders(date_path):
    """특정 날짜 경로에서 문제 폴더들 찾기"""
    problem_folders = []

    try:
        if not os.path.exists(date_path):
            return problem_folders

        items = os.listdir(date_path)

        for item in items:
            item_path = os.path.join(date_path, item)
            # 폴더이면서 문제 패턴 (BOJ_, PRO_ 등)에 맞는 것들
            if os.path.isdir(item_path) and (
                item.startswith("BOJ_")
                or item.startswith("PRO_")
                or item.startswith("SWEA_")
            ):
                problem_folders.append(item)

    except Exception as e:
        print(f"⚠️  문제 폴더 찾기 오류: {e}")

    return sorted(problem_folders)


def get_member_solved_problems(date_path, member, problem_folders):
    """특정 멤버가 해결한 문제 목록 반환 (중복 제거용)"""
    solved_problems = set()

    try:
        for problem_folder in problem_folders:
            problem_path = os.path.join(date_path, problem_folder)

            if os.path.isdir(problem_path):
                # 문제 폴더 안의 파일들 확인
                files = os.listdir(problem_path)

                # 해당 멤버의 파일이 있는지 확인
                member_files = [f for f in files if member in f and f.endswith(".py")]

                if member_files:
                    # 문제 번호 추출 (BOJ_2447 -> 2447)
                    problem_num = (
                        problem_folder.split("_")[1]
                        if "_" in problem_folder
                        else problem_folder
                    )
                    solved_problems.add(problem_num)
                    print(
                        f"     ✅ {member}: {problem_folder} 해결 ({member_files[0]})"
                    )

    except Exception as e:
        print(f"⚠️  {member} 해결 문제 계산 오류: {e}")

    return solved_problems


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
    total_solved = sum(data["solved"] for data in progress.values())
    avg_percentage = (
        round(sum(data["percentage"] for data in progress.values()) / len(progress), 1)
        if progress
        else 0
    )

    lines.append("")
    lines.append("### 📈 전체 통계")
    lines.append(f"- **총 해결 문제**: {total_solved}개")
    lines.append(f"- **평균 진행률**: {avg_percentage}%")
    lines.append(f"- **업데이트 시간**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    return "\n".join(lines)


def update_readme_with_progress(progress):
    """README 파일 업데이트 - 중복 추가 방지 개선"""
    week_folder = get_target_week_folder()

    if not week_folder:
        print("❌ 대상 폴더를 찾을 수 없습니다.")
        return False

    readme_path = ensure_readme_exists(week_folder)

    if not readme_path:
        print("❌ README 파일을 찾을 수 없습니다.")
        return False

    try:
        print(f"📖 README 파일 읽기 시도: {readme_path}")

        # 기존 내용 읽기
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        print(f"✅ README 파일 읽기 성공 (길이: {len(content)} 문자)")

        # 새로운 진행률 섹션
        new_progress = generate_progress_section(progress)
        print(f"📊 새로운 진행률 섹션 생성 완료")

        # 기존 진행 현황 섹션을 찾아서 완전히 교체
        # 더 정확한 패턴 매칭
        progress_start = content.find("## 📊 진행 현황")

        if progress_start != -1:
            # 다음 ## 섹션이나 파일 끝까지 찾기
            next_section_start = content.find("\n## ", progress_start + 1)

            if next_section_start != -1:
                # 다음 섹션이 있는 경우
                before_progress = content[:progress_start]
                after_progress = content[next_section_start:]
                new_content = f"{before_progress}## 📊 진행 현황\n\n{new_progress}\n\n{after_progress}"
            else:
                # 마지막 섹션인 경우
                before_progress = content[:progress_start]
                new_content = f"{before_progress}## 📊 진행 현황\n\n{new_progress}\n"

            print("🔄 기존 진행 현황 섹션 교체 완료")
        else:
            # 진행 현황 섹션이 없는 경우 추가
            # 파일 끝에 회고 섹션이 있다면 그 앞에 추가
            retrospect_start = content.find("## 💬 이번 주 회고")

            if retrospect_start != -1:
                before_retrospect = content[:retrospect_start]
                after_retrospect = content[retrospect_start:]
                new_content = f"{before_retrospect}\n## 📊 진행 현황\n\n{new_progress}\n\n{after_retrospect}"
            else:
                # 회고 섹션도 없다면 파일 끝에 추가
                new_content = f"{content}\n\n---\n\n## 📊 진행 현황\n\n{new_progress}\n"

            print("➕ 새로운 진행 현황 섹션 추가")

        print(f"💾 README 파일 저장 시도: {readme_path}")

        # 파일 저장
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)

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
        "date": today,
        "week_folder": get_target_week_folder(),
        "progress": progress,
        "timestamp": datetime.now().isoformat(),
        "file_structure_type": "problem_folder_based",
    }

    log_file = os.path.join(log_dir, f"progress_log_{today}.json")

    try:
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)
        print(f"💾 로그 저장: {log_file}")
    except Exception as e:
        print(f"❌ 로그 저장 실패: {e}")


if __name__ == "__main__":
    print("📈 진행률 업데이트 시작! (수정된 버전)")

    try:
        # 현재 폴더 구조 확인
        print("🔍 현재 작업 디렉토리:", os.getcwd())
        print("🔍 현재 디렉토리 내용:", os.listdir("."))

        week_folders = find_all_week_folders()
        target_folder = get_target_week_folder()

        print(f"🎯 발견된 주차 폴더들: {week_folders}")
        print(f"🎯 대상 폴더: {target_folder}")

        if target_folder:
            progress = calculate_member_progress()

            print("📊 계산된 진행률:")
            for member, data in progress.items():
                print(
                    f"  {data['status']} {member}: {data['solved']}/{data['total']} ({data['percentage']}%)"
                )

            # README 업데이트
            if update_readme_with_progress(progress):
                save_progress_log(progress)
                print("✅ 진행률 업데이트 완료!")
            else:
                print("❌ README 업데이트 실패")
        else:
            print("❌ 대상 폴더를 찾을 수 없습니다.")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback

        traceback.print_exc()
