#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Market Scout 发布防线：仓库工作树 vs 发布包的一致性校验。

背景：v5.0.0 发布时曾出现"包内是 V5、仓库 main 只剩 V4 源码"的失误
（commit e35b584 只提交了 README/图片/安装包，源码树未入库）。
本脚本用于发布前强制核对：仓库内容 == 发布包内容，不一致即阻止发布。

用法：
    python tools/verify_source_sync.py                      # 对比本目录与 releases/market-scout-v5.0.0.zip
    python tools/verify_source_sync.py <package.zip>        # 指定其他包

规则：
    - 包内文件（market-scout/...）必须与仓库工作树逐文件一致（规范化 CRLF/LF 后按内容比较）
    - 双方都排除 releases/ 与 __pycache__（发布包不嵌套自身；releases/ 是发布资产）
    - 任一 MISMATCH / MISSING / EXTRA 都会输出明细并返回退出码 1
"""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LF = chr(10).encode()
CRLF = chr(13).encode() + LF
ZIP_PREFIX = 'market-scout/'


def norm(b):
    return b.replace(CRLF, LF)


def worktree_files(root):
    out = {}
    for p in sorted(root.rglob('*')):
        if p.is_dir():
            continue
        rel = p.relative_to(root).as_posix()
        if rel.startswith('releases/') or '__pycache__' in rel or rel.endswith('.pyc'):
            continue
        out[rel] = p.read_bytes()
    return out


def package_files(pkg):
    out = {}
    with zipfile.ZipFile(pkg) as zf:
        for n in zf.namelist():
            if not n.startswith(ZIP_PREFIX):
                continue
            rel = n[len(ZIP_PREFIX):]
            if rel.endswith('/'):
                continue
            out[rel] = zf.read(n)
    return out


def main():
    pkg_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_PKG()
    if not pkg_path.exists():
        print('[verify_source_sync] FATAL: package not found: ' + str(pkg_path), file=sys.stderr)
        return 1
    wt = worktree_files(ROOT)
    pk = package_files(pkg_path)
    problems = []
    for rel in sorted(set(list(wt) + list(pk))):
        if rel not in wt:
            problems.append('EXTRA in package (missing in worktree): ' + rel)
        elif rel not in pk:
            problems.append('MISSING in package: ' + rel)
        elif norm(wt[rel]) != norm(pk[rel]):
            problems.append('CONTENT DIFF: ' + rel)
    print('verify_source_sync: worktree=%d files, package=%d files' % (len(wt), len(pk)))
    if problems:
        for p in problems:
            print('  [FAIL] ' + p, file=sys.stderr)
        print('RESULT: FAIL - repository and package are OUT OF SYNC; abort release.', file=sys.stderr)
        return 1
    print('RESULT: PASS - repository working tree == package content')
    return 0


def DEFAULT_PKG():
    return ROOT / 'releases' / 'market-scout-v5.0.0.zip'


if __name__ == '__main__':
    sys.exit(main())
