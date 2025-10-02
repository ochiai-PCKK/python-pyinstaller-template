# python-pyinstaller-template
Pyinstallerでビルドしたアプリをリリースするまでのワークフローのテンプレート

## ワークフローについてのポイント
1. バージョン管理を厳密に行う
2. CI/CDパイプラインは自動的に行うが、ローカルでビルドすることとする。

## バージョン管理

1. バージョンは `src/myapp/_version.py` で管理されています。
2. タグは `v1.2.3` の形式で管理されています。
3. バージョン更新は `scripts/write_version.py` を使用してください。

## ディレクトリ構造

```
├── packaging/           # パッケージング関連ファイル
│   ├── app.spec         # PyInstaller specファイル
│   └── version.rc       # バージョン情報リソースファイル
├── scripts/             # ビルドスクリプト
│   ├── release_build.py # リリースビルド用スクリプト
│   └── write_version.py # バージョン情報書き込みスクリプト
├── src/                 # ソースコード
│   └── myapp/           # アプリケーションパッケージ
│       ├── __init__.py
│       ├── __main__.py  # エントリーポイント
│       └── _version.py  # バージョン情報
├── tests/               # テストコード
├── .python-version      # Pythonバージョン管理用
├── pyproject.toml       # プロジェクトメタデータ
└── README.md            # このファイル
```
## セットアップ

### 前提条件
- Python 3.12+
- uv
- Git

### インストール

1. リポジトリをクローン:
   ```bash
   git clone https://github.com/yourusername/python-pyinstaller-template.git
   cd python-pyinstaller-template
   ```

2. 仮想環境の作成と有効化:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # または
   source .venv/bin/activate  # macOS/Linux
   ```

3. 依存関係のインストール:
   ```bash
   uv sync
   ```

## 開発

### アプリケーションの実行

```bash
python -m myapp
```

### テストの実行

```bash
pytest
```

## ビルド

### 開発用ビルド

```bash
pyinstaller packaging/app.spec
```

### リリース用ビルド

```bash
python scripts/release_build.py
```

## バージョン管理

バージョンは `src/myapp/_version.py` で管理されています。新しいリリースを作成する際は、このファイルを更新してください。

## CI/CD

このプロジェクトではローカルでビルドすることを推奨します。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルを参照してください。