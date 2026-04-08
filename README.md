# thumbnail-cli

テキストからサムネイル画像を CLI で生成するツールです。  
Python + Pillow 製で、テンプレートを選ぶだけでシンプルにサムネイルを作れます。

> **現在対応しているサイズ**
> - **note.com** 用：1280×670px
>
> 今後は Zenn・Qiita・OGP（1200×630）・YouTube サムネイル（1280×720）など、  
> 各プラットフォームのサイズへの対応を予定しています。

## セットアップ

```bash
cd thumbnail-cli
pip install -r requirements.txt
```

初回実行時に Noto Sans JP フォントが自動ダウンロードされます。

## 使い方

```bash
# 基本（タイトルのみ）
python3 thumbnail.py --title "ChatGPTで副業を始める方法"

# サブタイトルと著者名を追加
python3 thumbnail.py --title "タイトル" --subtitle "サブタイトル" --author "著者名"

# テンプレート指定
python3 thumbnail.py --title "タイトル" --template dark
python3 thumbnail.py --title "タイトル" --template gradient

# フォントウェイトを変更（100=Thin ～ 900=Black、デフォルト: 700/Bold）
python3 thumbnail.py --title "タイトル" --font-weight 400
python3 thumbnail.py --title "タイトル" --font-weight 900

# 出力ファイル名を指定
python3 thumbnail.py --title "タイトル" --output my-thumbnail.png
```

## テンプレート一覧

| テンプレート名 | 説明 |
|---|---|
| `default` | 白背景・ダークテキスト（デフォルト）|
| `dark` | ダーク背景・白テキスト |
| `gradient` | パープル→ブルーのグラデーション |
| `gradient-sunset` | オレンジ→ホットピンクのグラデーション |
| `gradient-ocean` | ティール→ネイビーのグラデーション |
| `gradient-forest` | ダークグリーン→ライムのグラデーション |
| `gradient-rose` | ディープパープル→コーラルピンクのグラデーション |
| `gradient-sakura` | チェリーピンク→ペールピンクのグラデーション |

## オプション

| オプション | 説明 | デフォルト |
|---|---|---|
| `--title` | メインタイトル（必須）| - |
| `--subtitle` | サブタイトル | なし |
| `--author` | 著者名 | なし |
| `--template` | テンプレート名 | `default` |
| `--font-weight` | フォントウェイト（100–900） | `700`（Bold） |
| `--output` | 出力ファイル名 | `thumbnail-{title}.png` |

## テスト実行

```bash
python3 -m pytest -v
```

## ディレクトリ構成

```
thumbnail-cli/
├── thumbnail.py       # CLI エントリポイント
├── font_manager.py    # フォント自動ダウンロード
├── text_renderer.py   # テキスト描画ユーティリティ（禁則処理対応）
├── templates/
│   ├── base.py        # 抽象基底クラス
│   ├── default.py     # 白背景テンプレート
│   ├── dark.py        # ダークテンプレート
│   └── gradient.py    # グラデーションテンプレート群（6バリアント）
├── skill/
│   ├── SKILL.md       # コーディングエージェント向けスキル定義
│   └── thumbnail-cli.skill  # インストール用スキルパッケージ
├── sample/            # サンプル生成画像
├── fonts/             # フォントキャッシュ（自動生成）
├── tests/             # テストスイート
├── requirements.txt
└── README.md
```

## コーディングエージェントで使う（スキル）

`skill/thumbnail-cli.skill` を [GitHub Copilot CLI](https://githubnext.com/projects/copilot-cli) などのコーディングエージェントにインストールすると、自然言語でサムネイルを生成できます。

```
# 使用例
「note記事「Pythonで始める機械学習入門」のサムネイルを作ってください」
「gradient-sakura テンプレートで桜の記事のサムネイルを作って」
「副業ガイドの記事に合うサムネイル、著者名も入れてください」
```

スキルが自動的にテンプレートを選択し、コマンドを実行して画像を生成します。

## 将来の拡張予定

- **他プラットフォーム対応**：Zenn・Qiita・OGP・YouTube サムネイルなど各サイズへの対応
- 背景画像対応（`--background image.jpg`）
- AI 画像生成連携
- 複数枚バッチ生成（CSV 入力）
