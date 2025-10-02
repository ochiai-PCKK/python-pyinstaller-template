# scripts/write_version.py
import sys, pathlib, subprocess

def get_latest_tag():
    try:
        return subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"]
        ).decode().strip()
    except subprocess.CalledProcessError:
        return None

# 1. コマンド引数 > Gitタグ > デフォルト の順で優先
ver = None
if len(sys.argv) > 1:
    ver = sys.argv[1]
else:
    tag = get_latest_tag()
    ver = tag if tag else "0.0.0-dev"

ver = ver.strip().lstrip("v")

# 2. _version.py に書き込み
pkg = pathlib.Path("src/myapp")
pkg.mkdir(parents=True, exist_ok=True)
(pathlib.Path("src/myapp/_version.py")).write_text(f'__version__ = "{ver}"\n', encoding="utf-8")

print(f"Wrote version {ver} to _version.py")
