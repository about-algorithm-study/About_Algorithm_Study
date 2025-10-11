#!/usr/bin/env python3
# scripts/weekly_check.py
"""
주간 알고리즘 스터디 진행상황 체크 스크립트
- 주차별로 9문제 진행 상황 확인
- 각 멤버의 문제 풀이 현황 추적
- 로그 파일 생성 및 README 업데이트
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

# 주당 목표 문제 수
WEEKLY_TARGET = 9


def get_current_week_folder():
    """현재 작업중인 주차 폴더 찾기"""
    base_path = Path('.')
    week_folders = [f for f in base_path.iterdir()
                   if f.is_dir() and '주차' in f.name]

    if not week_folders:
        print("⚠️ 주차 폴더를 찾을 수 없습니다.")
        return None

    # 폴더의 수정 시간 기준으로 정렬 (가장 최근에 수정된 폴더)
    week_folders_sorted = sorted(week_folders, key=lambda f: f.stat().st_mtime)

    # 가장 최근 주차 폴더 반환
    current_week = week_folders_sorted[-1]
    print(f"📁 현재 주차: {current_week.name}")
    return current_week


def scan_weekly_progress(week_folder):
    """주차별 진행상황 스캔"""
    
    if not week_folder or not week_folder.exists():
        print(f"❌ 폴더를 찾을 수 없습니다: {week_folder}")
        return None
    
    progress = {
        'week_name': week_folder.name,
        'total_problems': 0,
        'problems': [],
        'members': {initial: {'solved': 0, 'problems': []} 
                   for initial in MEMBERS.keys()}
    }
    
    # 문제 폴더 스캔 (BOJ_, SWEA_, PRO_ 등)
    problem_folders = [f for f in week_folder.iterdir() 
                      if f.is_dir() and any(f.name.startswith(prefix) 
                      for prefix in ['BOJ_', 'SWEA_', 'PRO_', 'LTC_'])]
    
    print(f"\n🔍 발견된 문제 폴더: {len(problem_folders)}개")
    
    for problem_folder in sorted(problem_folders):
        problem_name = problem_folder.name
        print(f"  📂 {problem_name}")
        
        problem_info = {
            'name': problem_name,
            'solved_by': []
        }
        
        # 문제 폴더 내 파일 스캔
        py_files = list(problem_folder.glob('*.py'))
        
        for py_file in py_files:
            # 파일명에서 이니셜 추출
            # 예: BOJ_1234_kky.py -> kky
            file_name = py_file.stem
            parts = file_name.split('_')
            
            if len(parts) >= 3:
                initial = parts[-1].lower()
                
                if initial in MEMBERS:
                    problem_info['solved_by'].append(initial)
                    progress['members'][initial]['solved'] += 1
                    progress['members'][initial]['problems'].append(problem_name)
                    print(f"    ✅ {MEMBERS[initial]} ({initial}) 풀이 완료")
        
        progress['problems'].append(problem_info)
        progress['total_problems'] += 1
    
    print(f"\n📊 총 문제 수: {progress['total_problems']}개")
    print(f"🎯 목표 문제 수: {WEEKLY_TARGET}개")
    
    return progress


def generate_progress_summary(progress):
    """진행상황 요약 생성"""
    
    print("\n" + "="*60)
    print("📊 주간 진행상황 요약")
    print("="*60)
    
    print(f"\n📁 주차: {progress['week_name']}")
    print(f"📝 등록된 문제: {progress['total_problems']} / {WEEKLY_TARGET}개")
    
    print("\n👥 멤버별 진행현황:")
    print("-" * 60)
    
    for initial, name in MEMBERS.items():
        solved = progress['members'][initial]['solved']
        percentage = (solved / WEEKLY_TARGET * 100) if WEEKLY_TARGET > 0 else 0
        
        status = "🟢" if solved >= WEEKLY_TARGET else "🟡" if solved >= WEEKLY_TARGET * 0.5 else "🔴"
        
        print(f"{status} {name:8s} ({initial}): {solved:2d}/{WEEKLY_TARGET} 문제 ({percentage:5.1f}%)")
        
        if progress['members'][initial]['problems']:
            print(f"   풀이한 문제: {', '.join(progress['members'][initial]['problems'][:3])}")
            if len(progress['members'][initial]['problems']) > 3:
                print(f"              외 {len(progress['members'][initial]['problems']) - 3}개")
    
    print("\n" + "="*60)


def save_weekly_log(progress):
    """주간 로그 저장"""
    
    # logs 디렉토리 생성
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    # 주차 기반 로그 파일명
    week_str = datetime.now().strftime('%Y_W%V')
    log_file = log_dir / f'weekly_log_{week_str}.json'
    
    # 로그 데이터 구성
    log_data = {
        'timestamp': datetime.now().isoformat(),
        'week': progress['week_name'],
        'week_number': week_str,
        'total_problems': progress['total_problems'],
        'target_problems': WEEKLY_TARGET,
        'problems': progress['problems'],
        'members': {
            initial: {
                'name': MEMBERS[initial],
                'solved': info['solved'],
                'problems': info['problems'],
                'percentage': round(info['solved'] / WEEKLY_TARGET * 100, 1) if WEEKLY_TARGET > 0 else 0
            }
            for initial, info in progress['members'].items()
        }
    }
    
    # JSON 파일로 저장
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 로그 저장 완료: {log_file}")
    
    return log_data


def update_readme(progress):
    """README.md 파일 업데이트"""
    
    week_folder = Path(progress['week_name'])
    readme_file = week_folder / 'README.md'
    
    # 진행현황 테이블 생성
    progress_table = "## 📊 진행 현황\n\n"
    progress_table += "| 멤버 | 진행률 | 풀이 문제 수 | 비고 |\n"
    progress_table += "|------|--------|-------------|------|\n"
    
    for initial, name in MEMBERS.items():
        solved = progress['members'][initial]['solved']
        percentage = (solved / WEEKLY_TARGET * 100) if WEEKLY_TARGET > 0 else 0
        
        status = "✅" if solved >= WEEKLY_TARGET else "⏳"
        progress_bar = "🟩" * solved + "⬜" * (WEEKLY_TARGET - solved)
        
        progress_table += f"| {name} | {percentage:.1f}% {progress_bar} | {solved}/{WEEKLY_TARGET} | {status} |\n"
    
    progress_table += f"\n**마지막 업데이트**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    
    # README 파일 읽기 및 업데이트
    if readme_file.exists():
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 기존 진행현황 섹션 찾아서 교체
        if '## 📊 진행 현황' in content:
            # 다음 섹션(##)이 나올 때까지를 진행현황 섹션으로 간주
            parts = content.split('## 📊 진행 현황')
            before = parts[0]
            
            # 다음 섹션 찾기
            after_parts = parts[1].split('\n## ')
            if len(after_parts) > 1:
                after = '\n## ' + '\n## '.join(after_parts[1:])
            else:
                after = ''
            
            new_content = before + progress_table + after
        else:
            # 진행현황 섹션이 없으면 파일 끝에 추가
            new_content = content.rstrip() + '\n\n' + progress_table
        
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"\n✅ README 업데이트 완료: {readme_file}")
    else:
        print(f"\n⚠️ README 파일을 찾을 수 없습니다: {readme_file}")


def main():
    """메인 실행 함수"""
    
    print("🚀 주간 알고리즘 스터디 체크 시작!")
    print(f"📅 실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 현재 주차 폴더 찾기
    week_folder = get_current_week_folder()
    
    if not week_folder:
        print("❌ 주차 폴더를 찾을 수 없어 종료합니다.")
        return
    
    # 진행상황 스캔
    progress = scan_weekly_progress(week_folder)
    
    if not progress:
        print("❌ 진행상황을 스캔할 수 없어 종료합니다.")
        return
    
    # 요약 출력
    generate_progress_summary(progress)
    
    # 로그 저장
    save_weekly_log(progress)
    
    # README 업데이트
    update_readme(progress)
    
    print("\n✨ 주간 체크 완료!")


if __name__ == '__main__':
    main()