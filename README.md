# note サムネイル生成ツール

note.com 投稿用のサムネイル画像（1280×670px）を CLI で生成します。

## セットアップ

```bash
cd note-thumbnail
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

# 出力ファイル名を指定
python3 thumbnail.py --title "タイトル" --output my-thumbnail.png
```

## テンプレート一覧

| テンプレート名 | 説明 |
|---|---|
| `default` | 白背景・ダークテキスト・青アクセントバー（デフォルト）|
| `dark` | ダーク背景・白テキスト・水色アクセントバー |
| `gradient` | パープル→ブルーのグラデーション背景・白テキスト |

## オプション

| オプション | 説明 | デフォルト |
|---|---|---|
| `--title` | メインタイトル（必須）| - |
| `--subtitle` | サブタイトル | なし |
| `--author` | 著者名 | なし |
| `--template` | テンプレート名 | `default` |
| `--output` | 出力ファイル名 | `thumbnail-{title}.png` |

## テスト実行

```bash
python3 -m pytest -v
```

## ディレクトリ構成

```
note-thumbnail/
├── thumbnail.py       # CLI エントリポイント
├── font_manager.py    # フォント自動ダウンロード
├── text_renderer.py   # テキスト描画ユーティリティ
├── templates/
│   ├── base.py        # 抽象基底クラス
│   ├── default.py     # 白背景テンプレート
│   ├── dark.py        # ダークテンプレート
│   └── gradient.py    # グラデーションテンプレート
├── fonts/             # フォントキャッシュ（自動生成）
├── tests/             # テストスイート
├── requirements.txt
└── README.md
```

## 将来の拡張予定

- 背景画像対応（`--background image.jpg`）
- AI 画像生成連携
- 複数枚バッチ生成（CSV 入力）
