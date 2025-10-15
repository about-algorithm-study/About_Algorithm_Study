#!/usr/bin/env python3
# scripts/update_weekly_progress.py
"""
누적 주간 진행률 업데이트 스크립트
- 전체 주차의 진행률을 누적해서 추적
- 멤버별 전체 통계 생성
- 루트 README 업데이트
"""

import os
import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# 스터디 멤버 정보
MEMBERS = {
    'kky': '김강연',
    'sjh': '신재혁',
    'ocm': '오창민',
    'smk': '송민경',
    'cjg': '최재각'
}

WEEKLY_TARGET = 9


def scan_all_weeks():
    """모든 주차의 진행상황 스캔"""
    
    base_path = Path('.')
    week_folders = sorted([f for f in base_path.iterdir() 
                          if f.is_dir() and '주차' in f.name])
    
    if not week_folders:
        print("⚠️ 주차 폴더를 찾을 수 없습니다.")
        return []
    
    print(f"📁 발견된 주차: {len(week_folders)}개")
    for folder in week_folders:
        print(f"  - {folder.name}")
    
    all_weeks_data = []
    
    for week_folder in week_folders:
        print(f"\n🔍 스캔 중: {week_folder.name}")
        
        week_data = {
            'name': week_folder.name,
            'total_problems': 0,
            'members': {initial: {'solved': 0, 'problems': []} 
                       for initial in MEMBERS.keys()}
        }
        
        # 문제 폴더 스캔
        problem_folders = [f for f in week_folder.iterdir() 
                          if f.is_dir() and any(f.name.startswith(prefix) 
                          for prefix in ['BOJ_', 'SWEA_', 'PRO_', 'LTC_'])]
        
        week_data['total_problems'] = len(problem_folders)
        print(f"  📝 문제 수: {len(problem_folders)}개")
        
        for problem_folder in problem_folders:
            py_files = list(problem_folder.glob('*.py'))
            
            for py_file in py_files:
                file_name = py_file.stem
                parts = file_name.split('_')
                
                if len(parts) >= 3:
                    initial = parts[-1].lower()
                    
                    if initial in MEMBERS:
                        week_data['members'][initial]['solved'] += 1
                        week_data['members'][initial]['problems'].append(problem_folder.name)
        
        # 멤버별 진행률 출력
        for initial, name in MEMBERS.items():
            solved = week_data['members'][initial]['solved']
            print(f"    {name}: {solved}개")
        
        all_weeks_data.append(week_data)
    
    return all_weeks_data


def calculate_cumulative_stats(all_weeks_data):
    """누적 통계 계산"""
    
    cumulative = {
        'total_weeks': len(all_weeks_data),
        'total_problems_available': len(all_weeks_data) * WEEKLY_TARGET,
        'members': {
            initial: {
                'name': name,
                'total_solved': 0,
                'by_week': {},
                'participation_rate': 0,
                'average_per_week': 0
            }
            for initial, name in MEMBERS.items()
        }
    }
    
    # 주차별 데이터 집계
    for week_data in all_weeks_data:
        week_name = week_data['name']
        
        for initial in MEMBERS.keys():
            solved = week_data['members'][initial]['solved']
            cumulative['members'][initial]['total_solved'] += solved
            cumulative['members'][initial]['by_week'][week_name] = solved
    
    # 멤버별 통계 계산
    for initial, data in cumulative['members'].items():
        total_solved = data['total_solved']
        total_weeks = cumulative['total_weeks']
        
        # 평균 및 참여율 계산
        data['average_per_week'] = round(total_solved / total_weeks, 2) if total_weeks > 0 else 0
        data['participation_rate'] = round(
            (total_solved / cumulative['total_problems_available'] * 100), 1
        ) if cumulative['total_problems_available'] > 0 else 0
    
    return cumulative


def print_cumulative_summary(cumulative):
    """누적 통계 요약 출력"""
    
    print("\n" + "="*70)
    print("📊 전체 누적 통계")
    print("="*70)
    
    print(f"\n📅 전체 주차: {cumulative['total_weeks']}주")
    print(f"📝 총 문제 수: {cumulative['total_problems_available']}개 ({cumulative['total_weeks']} x {WEEKLY_TARGET})")
    
    print("\n👥 멤버별 누적 통계:")
    print("-" * 70)
    print(f"{'멤버':<10} {'총 풀이':<12} {'주평균':<12} {'참여율':<12} {'순위'}")
    print("-" * 70)
    
    # 총 풀이 수로 정렬
    sorted_members = sorted(
        cumulative['members'].items(),
        key=lambda x: x[1]['total_solved'],
        reverse=True
    )
    
    for rank, (initial, data) in enumerate(sorted_members, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
        
        print(f"{data['name']:<10} "
              f"{data['total_solved']:<12} "
              f"{data['average_per_week']:<12} "
              f"{data['participation_rate']}%{'':<8} "
              f"{medal} {rank}위")
    
    print("\n" + "="*70)


def save_cumulative_log(all_weeks_data, cumulative):
    """누적 로그 저장"""
    
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    week_str = datetime.now().strftime('%Y_W%V')
    log_file = log_dir / f'cumulative_progress_{week_str}.json'
    
    log_data = {
        'timestamp': datetime.now().isoformat(),
        'week_number': week_str,
        'summary': {
            'total_weeks': cumulative['total_weeks'],
            'total_problems': cumulative['total_problems_available'],
            'weekly_target': WEEKLY_TARGET
        },
        'weeks': all_weeks_data,
        'cumulative_stats': cumulative['members']
    }
    
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 누적 로그 저장 완료: {log_file}")
    
    return log_data


def update_root_readme(cumulative, all_weeks_data):
    """루트 README.md 파일에 전체 진행률 업데이트"""
    
    readme_file = Path('README.md')
    
    if not readme_file.exists():
        print(f"\n⚠️ 루트 README 파일을 찾을 수 없습니다: {readme_file}")
        return
    
    # 누적 진행률 섹션 생성
    progress_section = "\n## 📈 전체 진행률 (누적)\n\n"
    progress_section += f"**업데이트**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    progress_section += f"- 📅 총 {cumulative['total_weeks']}주차 진행\n"
    progress_section += f"- 📝 전체 문제: {cumulative['total_problems_available']}개\n\n"
    
    # 멤버별 누적 통계 테이블
    progress_section += "### 👥 멤버별 누적 통계\n\n"
    progress_section += "| 순위 | 멤버 | 총 풀이 | 주평균 | 참여율 | 진행바 |\n"
    progress_section += "|------|------|---------|--------|--------|--------|\n"
    
    # 총 풀이 수로 정렬
    sorted_members = sorted(
        cumulative['members'].items(),
        key=lambda x: x[1]['total_solved'],
        reverse=True
    )
    
    for rank, (initial, data) in enumerate(sorted_members, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"{rank}위"
        
        # 진행바 생성 (10칸 기준)
        total_possible = cumulative['total_problems_available']
        filled = int((data['total_solved'] / total_possible * 10)) if total_possible > 0 else 0
        progress_bar = "🟩" * filled + "⬜" * (10 - filled)
        
        progress_section += (f"| {medal} | {data['name']} | "
                           f"{data['total_solved']}개 | "
                           f"{data['average_per_week']}개 | "
                           f"{data['participation_rate']}% | "
                           f"{progress_bar} |\n")
    
    # 주차별 상세 진행률
    progress_section += "\n### 📊 주차별 진행률\n\n"
    
    for week_data in all_weeks_data:
        week_name = week_data['name']
        progress_section += f"\n#### {week_name}\n\n"
        progress_section += "| 멤버 | 풀이 수 | 진행률 |\n"
        progress_section += "|------|---------|--------|\n"
        
        for initial, name in MEMBERS.items():
            solved = week_data['members'][initial]['solved']
            percentage = (solved / WEEKLY_TARGET * 100) if WEEKLY_TARGET > 0 else 0
            status = "✅" if solved >= WEEKLY_TARGET else "⏳"
            
            progress_section += f"| {name} | {solved}/{WEEKLY_TARGET} | {percentage:.1f}% {status} |\n"
    
    progress_section += "\n---\n"
    
    # README 파일 읽기
    with open(readme_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 기존 진행률 섹션 찾아서 교체
    if '## 📈 전체 진행률 (누적)' in content:
        parts = content.split('## 📈 전체 진행률 (누적)')
        before = parts[0]
        
        # 다음 주요 섹션 찾기 (##으로 시작하는 섹션)
        after_parts = parts[1].split('\n## ')
        if len(after_parts) > 1:
            # 진행률 섹션 이후의 내용 찾기
            after = '\n## ' + '\n## '.join(after_parts[1:])
        else:
            after = ''
        
        new_content = before + progress_section + after
    else:
        # 진행률 섹션이 없으면 파일 끝에 추가
        new_content = content.rstrip() + '\n\n' + progress_section
    
    # README 파일 저장
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ 루트 README 업데이트 완료: {readme_file}")


def main():
    """메인 실행 함수"""
    
    print("🚀 주간 진행률 업데이트 시작!")
    print(f"📅 실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 모든 주차 스캔
    all_weeks_data = scan_all_weeks()
    
    if not all_weeks_data:
        print("❌ 주차 데이터를 찾을 수 없어 종료합니다.")
        return
    
    # 누적 통계 계산
    cumulative = calculate_cumulative_stats(all_weeks_data)
    
    # 요약 출력
    print_cumulative_summary(cumulative)
    
    # 로그 저장
    save_cumulative_log(all_weeks_data, cumulative)
    
    # 루트 README 업데이트
    update_root_readme(cumulative, all_weeks_data)
    
    print("\n✨ 주간 진행률 업데이트 완료!")


if __name__ == '__main__':
    main()