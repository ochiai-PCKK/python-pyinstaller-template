from pathlib import Path
try:
    # scripts/write_version.py が生成するモジュール
    from ._version import __version__
except Exception:
    __version__ = "0.0.0-dev"

def main():
    print(f"myapp {__version__}")
    # ここに実処理を書く
    print("Hello from myapp!")

if __name__ == "__main__":
    main()
