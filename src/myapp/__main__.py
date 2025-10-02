import sys
sys.path.append("src")

from myapp._version import __version__

def main():
    print(f"myapp {__version__}")
    print("Hello from myapp!")

if __name__ == "__main__":
    main()
