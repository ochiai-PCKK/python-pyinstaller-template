import subprocess, shutil, pathlib

def run(cmd):
    print(f"==> {cmd}")
    subprocess.check_call(cmd, shell=True)

def get_version():
    ns = {}
    version_file = pathlib.Path("src/myapp/_version.py")
    exec(version_file.read_text(encoding="utf-8"), ns)
    return ns.get("__version__", "0.0.0-dev")

def main():
    version = get_version()
    print(f"==> Building version {version}")

    # PyInstaller
    run("uv run pyinstaller packaging/app.spec --clean")

    # ZIP化
    out_dir = pathlib.Path("dist")
    zip_path = out_dir / f"myapp-{version}-win64.zip"
    if zip_path.exists():
        zip_path.unlink()
    shutil.make_archive(str(zip_path.with_suffix("")), "zip", out_dir / "myapp")

    print(f"==> Done. Created {zip_path}")

if __name__ == "__main__":
    main()
