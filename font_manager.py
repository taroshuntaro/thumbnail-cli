import os
import urllib.request

FONTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
FONT_PATH = os.path.join(FONTS_DIR, "NotoSansJP.ttf")

_FONT_URL = (
    "https://github.com/google/fonts/raw/main/ofl/notosansjp/"
    "NotoSansJP%5Bwght%5D.ttf"
)


def get_font_path() -> str:
    """Return path to Noto Sans JP font, downloading if necessary."""
    if os.path.exists(FONT_PATH):
        return FONT_PATH
    os.makedirs(FONTS_DIR, exist_ok=True)
    print("Downloading Noto Sans JP font (first time only)...")
    urllib.request.urlretrieve(_FONT_URL, FONT_PATH)
    print(f"Font saved to: {FONT_PATH}")
    return FONT_PATH
