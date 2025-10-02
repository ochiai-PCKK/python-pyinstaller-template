# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

SPEC_DIR = Path(SPECPATH).resolve()   # packaging/
PROJECT_ROOT = SPEC_DIR.parent        # プロジェクトルート

a = Analysis(
    [str(PROJECT_ROOT / 'src' / 'myapp' / '__main__.py')],  # 絶対パス化
    pathex=[str(PROJECT_ROOT)],                             # ルートを探索パスに
    binaries=[],
    datas=[],
    hiddenimports=[
        'encodings','encodings.utf_8','encodings.cp932','codecs',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(
    pyz, a.scripts, name='myapp', console=True,
    exclude_binaries=True,
    upx=False, version_file=str(SPEC_DIR / 'version.rc.txt'),
)
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, name='myapp', upx=False)
