# scripts/daily_check.py - 문제별 폴더 구조 대응 버전
import os
import json
from datetime import datetime, date
import glob

# 스터디 멤버 리스트 (실제 이름으로 업데이트)
MEMBERS = ["kky", "sjh", "ocm", "smk", "cjg"]


def get_current_week_folder():
    """현재 주차 폴더명 반환"""
    today = date.today()
    month = today.month

    # 실제 달력 기준으로 주차 계산
    first_day = date(today.year, month, 1)
    week_number = ((today.day - 1) // 7) + 1

    return f"{month}월{week_number}주차"


def get_today_folder():
    """오늘 날짜 폴더명 반환 (MMDD 형식)"""
    return datetime.now().strftime("%m%d")


def find_week_folders():
    """현재 월의 모든 주차 폴더 찾기"""
    current_month = date.today().month
    week_folders = []

    # 현재 디렉토리에서 월 주차 폴더 찾기
    for item in os.listdir("."):
        if os.path.isdir(item) and f"{current_month}월" in item and "주차" in item:
            week_folders.append(item)

    return sorted(week_folders)


def check_today_uploads():
    """오늘 업로드된 파일들 체크 - 문제별 폴더 구조 대응"""
    week_folder = get_current_week_folder()
    today_folder = get_today_folder()

    # 여러 가능한 경로 확인
    possible_paths = [
        f"{week_folder}/{today_folder}",
        f"{week_folder}/0820",  # 고정된 날짜 (임시)
    ]

    # 기존 주차 폴더들도 확인
    week_folders = find_week_folders()
    for wf in week_folders:
        possible_paths.extend([f"{wf}/{today_folder}", f"{wf}/0820"])

    folder_path = None
    for path in possible_paths:
        if os.path.exists(path):
            folder_path = path
            break

    print(f"🔍 체크 경로: {possible_paths}")
    print(f"✅ 사용할 경로: {folder_path}")

    if not folder_path:
        print(f"❌ 오늘 폴더를 찾을 수 없습니다.")
        return {
            member: {"uploaded_count": 0, "files": [], "status": "❌"}
            for member in MEMBERS
        }

    # 각 멤버별 업로드 현황 체크 (문제별 폴더 구조 고려)
    upload_status = {}

    for member in MEMBERS:
        member_files = []

        try:
            # 날짜 폴더 안의 모든 문제 폴더 확인
            if os.path.exists(folder_path):
                items = os.listdir(folder_path)

                # 문제 폴더들 찾기 (BOJ_, PRO_ 등으로 시작하는 폴더)
                problem_folders = [
                    item
                    for item in items
                    if os.path.isdir(os.path.join(folder_path, item))
                    and ("BOJ_" in item or "PRO_" in item or "SWEA_" in item)
                ]

                print(f"📁 {member}의 문제 폴더들: {problem_folders}")

                # 각 문제 폴더에서 해당 멤버의 파일 찾기
                for problem_folder in problem_folders:
                    problem_path = os.path.join(folder_path, problem_folder)

                    if os.path.isdir(problem_path):
                        # 문제 폴더 안의 파일들 확인
                        problem_files = os.listdir(problem_path)

                        # 해당 멤버의 파일 찾기
                        for file in problem_files:
                            if member in file and file.endswith(".py"):
                                member_files.append(f"{problem_folder}/{file}")

        except Exception as e:
            print(f"⚠️  {folder_path} 읽기 오류: {e}")

        upload_status[member] = {
            "uploaded_count": len(member_files),
            "files": member_files,
            "status": "✅" if len(member_files) > 0 else "❌",
        }

    return upload_status


def print_daily_report(upload_status):
    """일일 리포트 출력"""
    today = datetime.now().strftime("%Y-%m-%d")

    print(f"\n📊 알고리즘 스터디 일일 리포트 ({today})")
    print("=" * 50)

    total_uploaded = 0
    total_members = len(MEMBERS)

    for member, status in upload_status.items():
        status_icon = status["status"]
        file_count = status["uploaded_count"]

        print(f"{status_icon} {member}: {file_count}개 문제 업로드")

        if file_count > 0:
            total_uploaded += 1
            for file in status["files"]:
                print(f"   📝 {file}")

    print(
        f"\n📈 전체 현황: {total_uploaded}/{total_members}명 참여 ({(total_uploaded/total_members)*100:.1f}%)"
    )

    # 아직 업로드하지 않은 멤버들
    not_uploaded = [
        member
        for member, status in upload_status.items()
        if status["uploaded_count"] == 0
    ]

    if not_uploaded:
        print(f"\n🔔 아직 업로드하지 않은 멤버:")
        for member in not_uploaded:
            print(f"   ⏰ {member}")
    else:
        print(f"\n🎉 모든 멤버가 오늘 문제를 업로드했습니다!")


def save_daily_log(upload_status):
    """일일 로그를 JSON 파일로 저장"""
    today = datetime.now().strftime("%Y%m%d")
    log_dir = "logs"

    # logs 디렉토리 생성
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        print(f"📁 {log_dir} 디렉토리 생성")

    log_data = {
        "date": today,
        "upload_status": upload_status,
        "timestamp": datetime.now().isoformat(),
        "week_folder": get_current_week_folder(),
        "checked_paths": find_week_folders(),
        "file_structure_type": "problem_folder_based",  # 새로운 구조 표시
    }

    log_file = f"{log_dir}/daily_log_{today}.json"

    try:
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)

        print(f"💾 일일 로그 저장: {log_file}")
    except Exception as e:
        print(f"❌ 로그 저장 실패: {e}")


if __name__ == "__main__":
    print("🚀 일일 알고리즘 스터디 체크 시작! (문제별 폴더 구조)")

    try:
        upload_status = check_today_uploads()
        print_daily_report(upload_status)
        save_daily_log(upload_status)

        print("\n✅ 일일 체크 완료!")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback

        traceback.print_exc()
