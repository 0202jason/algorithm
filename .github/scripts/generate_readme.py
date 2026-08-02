"""
Algorithm 리포지토리 README 자동 생성 스크립트

파일명 규칙:
  baekjoon/       → 2603_색종이.py    (번호_제목.py)
  programmers/    → 두개뽑아서.py 또는 두개뽑아서.java (제목, 번호 없음)
  SWEA/           → 1234_파리퇴치.py  (번호_제목.py)
  algoalgo_arena/ → 임의 파일명 허용

실행: python .github/scripts/generate_readme.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent

PLATFORMS = {
    'baekjoon': {
        'name': 'Baekjoon',
        'has_number': True,
        'problem_url': 'https://www.acmicpc.net/problem/{}',
    },
    'SWEA': {
        'name': 'SWEA',
        'has_number': True,
        'problem_url': '',
    },
    'programmers': {
        'name': 'Programmers',
        'has_number': False,
        'problem_url': '',
    },
    'algoalgo_arena': {
        'name': 'AlgoAlgo',
        'has_number': False,
        'problem_url': '',
    },
}

# GitHub 마크다운 앵커: 헤더 텍스트 소문자 + 공백→- + 특수문자 제거
def to_anchor(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text


def parse_filename(stem: str, has_number: bool) -> tuple[str, str]:
    if has_number:
        match = re.match(r'^(\d+)[_\-\s](.+)$', stem)
        if match:
            return match.group(1), match.group(2).replace('_', ' ')
        if stem.isdigit():
            return stem, ''
    return '', stem.replace('_', ' ')


def collect(platform: str, meta: dict) -> list:
    folder = ROOT / platform
    if not folder.exists():
        return []
    results = []
    source_files = sorted(
        file
        for pattern in ('*.py', '*.java')
        for file in folder.rglob(pattern)
    )
    for source_file in source_files:
        if source_file.stem.startswith('__'):
            continue
        number, title = parse_filename(source_file.stem, meta['has_number'])
        results.append({
            'number': number,
            'title':  title,
            'path':   source_file.relative_to(ROOT).as_posix(),
        })
    return results


def collect_concepts() -> list:
    folder = ROOT / 'Concepts'
    if not folder.exists():
        return []
    return [
        {
            'name': f.stem.replace('_', ' '),
            'path': f.relative_to(ROOT).as_posix(),
        }
        for f in sorted(folder.glob('*.md'))
        if f.name != 'README.md'
    ]


def make_table(problems: list, meta: dict) -> list:
    has_number = meta['has_number']
    url_tpl    = meta.get('problem_url', '')

    def num_cell(p):
        if not p['number']:
            return '&nbsp;'
        return f'[{p["number"]}]({url_tpl.format(p["number"])})' if url_tpl else p['number']

    def title_cell(p):
        label = p['title'] if p['title'] else (p['number'] if p['number'] else '-')
        return f'[{label}]({p["path"]})'

    lines = []
    if has_number:
        lines.append('| # | Title | &nbsp; | # | Title |')
        lines.append('|:---:|:---|:---:|:---:|:---|')
    else:
        lines.append('| Title | &nbsp; | Title |')
        lines.append('|:---|:---:|:---|')

    for i in range(0, len(problems), 2):
        left  = problems[i]
        right = problems[i + 1] if i + 1 < len(problems) else None

        if has_number:
            ln = num_cell(left)
            lt = title_cell(left)
            rn = num_cell(right)   if right else '&nbsp;'
            rt = title_cell(right) if right else '&nbsp;'
            lines.append(f'| {ln} | {lt} | &nbsp; | {rn} | {rt} |')
        else:
            lt = title_cell(left)
            rt = title_cell(right) if right else '&nbsp;'
            lines.append(f'| {lt} | &nbsp; | {rt} |')

    return lines


def render(all_problems: dict, concepts: list) -> str:
    total = sum(len(v) for v in all_problems.values())

    # 실제로 문제가 있는 플랫폼만
    active = [(p, m) for p, m in PLATFORMS.items() if all_problems.get(p)]

    # TOC — anchor는 헤더 텍스트와 정확히 일치해야 함
    toc_lines = []
    for platform, meta in active:
        count  = len(all_problems[platform])
        anchor = to_anchor(meta['name'])
        toc_lines.append(f'[{meta["name"]}](#{anchor}) &nbsp;·&nbsp; {count} problems')
    if concepts:
        toc_lines.append(f'[Concepts](#concepts) &nbsp;·&nbsp; {len(concepts)} topics')

    lines = [
        '# Algorithm\n',
        '알고리즘 문제 풀이 및 개념 정리 저장소입니다.  ',
        'Python과 Java로 작성하며, 꾸준한 풀이와 기록을 목표로 합니다.\n',
        '![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)\n',
        '![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white)\n',
        '---\n',
        '## Goals\n',
        '- [ ] SWEA B형 취득',
        '- [x] 주기적 풀이 습관 형성',
        '- [ ] 주요 알고리즘 개념 전체 정리\n',
        '---\n',
        f'## Problems &nbsp; <sub>total {total}</sub>\n',
    ]

    # TOC
    lines.append(' &nbsp;|&nbsp; '.join(toc_lines) + '\n')

    # 각 플랫폼 섹션 — 헤더는 이름만 (앵커 기준), 문제 수는 다음 줄
    for platform, meta in active:
        problems = all_problems[platform]
        count    = len(problems)
        lines.append(f'### {meta["name"]}\n')
        lines.append(f'<sub>{count} problems</sub>\n')
        lines.extend(make_table(problems, meta))
        lines.append('')

    if concepts:
        lines.append('---\n')
        lines.append('### Concepts\n')
        lines.append(f'<sub>{len(concepts)} topics</sub>\n')
        lines.append('| Topic | Link |')
        lines.append('|:---|:---:|')
        for c in concepts:
            lines.append(f'| {c["name"]} | [→]({c["path"]}) |')
        lines.append('')

    lines += [
        '---\n',
        '## Best Practice\n',
        '1. **가독성 우선** — PEP 8 지키기 (클래스: PascalCase / 함수·변수: snake_case / 상수: SNAKE_CASE)',
        '2. **효율성 체크** — 시간복잡도 O(N)을 항상 계산하고 제출',
        '3. **기록의 힘** — 어떻게 풀이를 시작했는지, 왜 이 알고리즘을 선택했는지, AI의 도움을 어떻게 받았는지 주석으로 생각의 흐름 남기기\n',
        '---\n',
        '<p align="right"><em>"가독성 우선, 효율성 체크, 기록의 힘"</em></p>\n',
    ]

    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    all_problems = {p: collect(p, m) for p, m in PLATFORMS.items()}
    concepts     = collect_concepts()
    readme       = render(all_problems, concepts)

    with open(ROOT / 'README.md', 'w', encoding='utf-8') as f:
        f.write(readme)

    total = sum(len(v) for v in all_problems.values())
    print(f'Done - {total} problems, {len(concepts)} concepts')
