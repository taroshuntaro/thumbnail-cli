import argparse
import os
import re

from templates import get_template

WIDTH, HEIGHT = 1280, 670


def sanitize_filename(text: str) -> str:
    """Convert title to a safe filename component."""
    text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "", text)
    text = text.replace(" ", "-")
    return text[:80]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="note.com 用サムネイル画像を生成します（1280×670px）"
    )
    parser.add_argument("--title", required=True, help="メインタイトル（必須）")
    parser.add_argument("--subtitle", default=None, help="サブタイトル（任意）")
    parser.add_argument("--author", default=None, help="著者名（任意）")
    parser.add_argument(
        "--template",
        default="default",
        choices=["default", "dark", "gradient"],
        help="テンプレート名（デフォルト: default）",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="出力ファイル名（デフォルト: thumbnail-{title}.png）",
    )
    parser.add_argument(
        "--font-weight",
        type=int,
        default=700,
        metavar="WEIGHT",
        help="フォントウェイト 100-900 (デフォルト: 700). 100=Thin, 400=Regular, 700=Bold, 900=Black",
    )
    args = parser.parse_args()

    if not 100 <= args.font_weight <= 900:
        parser.error("--font-weight は 100〜900 の範囲で指定してください")

    output = args.output or f"thumbnail-{sanitize_filename(args.title)}.png"
    template = get_template(args.template)
    img = template.render(
        title=args.title,
        subtitle=args.subtitle,
        author=args.author,
        font_weight=args.font_weight,
    )
    img.save(output)
    print(f"✅ Saved: {output}  ({WIDTH}×{HEIGHT}px, template={args.template})")


if __name__ == "__main__":
    main()
