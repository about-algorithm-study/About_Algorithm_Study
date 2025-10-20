#!/usr/bin/env python3
"""
알고리즘 스터디 진행률 자동 업데이트 스크립트
각 주차별 폴더를 스캔하여 멤버별 문제 풀이 수를 카운트하고 README를 업데이트합니다.
"""

import os
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# 멤버 정보 (이니셜: 이름)
MEMBERS = {
    'kky': '김강연',
    'sjh': '신재혁',
    'ocm': '오창민',
    'smk': '송민경',
    'cjg': '최재각'
}

# 멤버 순서 (표에 표시할 순서)
MEMBER_ORDER = ['김강연', '신재혁', '오창민', '송민경', '최재각']

def get_week_folders():
    """주차별 폴더 목록을 반환합니다."""
    root = Path('.')
    week_pattern = re.compile(r'^\d+월\d+주차$')

    week_folders = []
    for folder in root.iterdir():
        if folder.is_dir() and week_pattern.match(folder.name):
            week_folders.append(folder)

    return sorted(week_folders, key=lambda x: x.name)

def count_solutions(week_folder):
    """특정 주차 폴더의 멤버별 풀이 수를 카운트합니다."""
    member_counts = defaultdict(int)

    # 문제 폴더들을 순회
    for problem_folder in week_folder.iterdir():
        if not problem_folder.is_dir():
            continue

        # 각 파일 확인
        for file_path in problem_folder.iterdir():
            if not file_path.is_file():
                continue

            # 파일명 패턴: 플랫폼_문제번호_이니셜.확장자
            # 예: BOJ_10870_kky.py, SWEA_1234_sjh.java
            pattern = r'_([a-z]{2,3})\.(py|java|cpp|js)$'
            match = re.search(pattern, file_path.name)

            if match:
                initial = match.group(1)
                if initial in MEMBERS:
                    member_counts[MEMBERS[initial]] += 1

    return member_counts

def generate_progress_bar(count, total):
    """진행률 바를 생성합니다."""
    filled = int((count / total) * 9)
    bar = '🟩' * filled + '⬜' * (9 - filled)
    return bar

def update_week_readme(week_folder, member_counts, total_problems=9):
    """주차별 README.md를 업데이트합니다."""
    readme_path = week_folder / 'README.md'

    if not readme_path.exists():
        print(f"⚠️  {week_folder.name}/README.md 파일이 없습니다. 건너뜁니다.")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 진행 현황 테이블 생성
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')

    table_lines = [
        '## 📊 진행 현황\n',
        '| 멤버 | 진행률 | 풀이 문제 수 | 비고 |',
        '|------|--------|-------------|------|'
    ]

    for member_name in MEMBER_ORDER:
        count = member_counts.get(member_name, 0)
        percentage = (count / total_problems) * 100
        progress_bar = generate_progress_bar(count, total_problems)
        status = '✅' if count >= total_problems else '⏳'

        table_lines.append(
            f'| {member_name} | {percentage:.1f}% {progress_bar} | {count}/{total_problems} | {status} |'
        )

    table_lines.append(f'\n**마지막 업데이트**: {current_time}\n')

    new_table = '\n'.join(table_lines)

    # 기존 진행 현황 섹션 교체
    pattern = r'## 📊 진행 현황\n.*?\*\*마지막 업데이트\*\*:.*?\n'
    if re.search(pattern, content, re.DOTALL):
        updated_content = re.sub(pattern, new_table, content, flags=re.DOTALL)
    else:
        # 진행 현황 섹션이 없으면 추가
        updated_content = content + '\n\n' + new_table

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"✅ {week_folder.name}/README.md 업데이트 완료")

def update_main_readme(all_weeks_data):
    """메인 README.md를 업데이트합니다."""
    readme_path = Path('README.md')

    if not readme_path.exists():
        print("⚠️  README.md 파일이 없습니다.")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 전체 통계 계산
    total_counts = defaultdict(int)
    for week_name, member_counts in all_weeks_data.items():
        for member, count in member_counts.items():
            total_counts[member] += count

    total_weeks = len(all_weeks_data)
    total_problems = total_weeks * 9

    # 순위 정렬
    sorted_members = sorted(
        MEMBER_ORDER,
        key=lambda m: total_counts.get(m, 0),
        reverse=True
    )

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')

    # 전체 진행률 섹션 생성
    overall_lines = [
        '## 📈 전체 진행률 (누적)\n',
        f'**업데이트**: {current_time}\n',
        f'- 📅 총 {total_weeks}주차 진행',
        f'- 📝 전체 문제: {total_problems}개\n',
        '### 👥 멤버별 누적 통계\n',
        '| 순위 | 멤버 | 총 풀이 | 주평균 | 참여율 | 진행바 |',
        '|------|------|---------|--------|--------|--------|'
    ]

    medals = ['🥇', '🥈', '🥉']
    for idx, member_name in enumerate(sorted_members):
        count = total_counts.get(member_name, 0)
        avg_per_week = count / total_weeks if total_weeks > 0 else 0
        participation_rate = (count / total_problems * 100) if total_problems > 0 else 0
        progress_bar = '⬜' * 10  # 간단한 10칸 바
        rank = medals[idx] if idx < 3 else f'{idx + 1}위'

        overall_lines.append(
            f'| {rank} | {member_name} | {count}개 | {avg_per_week:.2f}개 | {participation_rate:.1f}% | {progress_bar} |'
        )

    overall_lines.append('\n### 📊 주차별 진행률\n')

    # 주차별 진행률 테이블
    for week_name in sorted(all_weeks_data.keys()):
        member_counts = all_weeks_data[week_name]
        overall_lines.append(f'\n#### {week_name}\n')
        overall_lines.append('| 멤버 | 풀이 수 | 진행률 |')
        overall_lines.append('|------|---------|--------|')

        for member_name in MEMBER_ORDER:
            count = member_counts.get(member_name, 0)
            percentage = (count / 9) * 100
            status = '✅' if count >= 9 else '⏳'
            overall_lines.append(f'| {member_name} | {count}/9 | {percentage:.1f}% {status} |')

    overall_lines.append('\n---\n')

    new_section = '\n'.join(overall_lines)

    # 기존 전체 진행률 섹션 교체
    pattern = r'## 📈 전체 진행률 \(누적\)\n.*?---\n'
    if re.search(pattern, content, re.DOTALL):
        updated_content = re.sub(pattern, new_section, content, flags=re.DOTALL)
    else:
        # 섹션이 없으면 파일 끝에 추가
        updated_content = content + '\n\n' + new_section

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print("✅ README.md 업데이트 완료")

def main():
    """메인 실행 함수"""
    print("🚀 알고리즘 스터디 진행률 업데이트 시작...\n")

    week_folders = get_week_folders()

    if not week_folders:
        print("⚠️  주차 폴더를 찾을 수 없습니다.")
        return

    all_weeks_data = {}

    for week_folder in week_folders:
        print(f"📂 {week_folder.name} 스캔 중...")
        member_counts = count_solutions(week_folder)
        all_weeks_data[week_folder.name] = member_counts

        # 주차별 README 업데이트
        update_week_readme(week_folder, member_counts)

        # 결과 출력
        for member in MEMBER_ORDER:
            count = member_counts.get(member, 0)
            print(f"  - {member}: {count}문제")
        print()

    # 메인 README 업데이트
    update_main_readme(all_weeks_data)

    print("\n✨ 모든 업데이트가 완료되었습니다!")

if __name__ == '__main__':
    main()