import os
from unittest.mock import patch
import font_manager


def test_get_font_path_returns_cached_file(tmp_path):
    """フォントファイルが存在する場合はダウンロードせず返す。"""
    fake_font = tmp_path / "NotoSansJP.ttf"
    fake_font.write_bytes(b"dummy")

    with patch.object(font_manager, "FONT_PATH", str(fake_font)):
        result = font_manager.get_font_path()

    assert result == str(fake_font)


def test_get_font_path_creates_fonts_dir_and_downloads(tmp_path):
    """fonts/ ディレクトリが存在しない場合は作成してダウンロードする。"""
    fonts_dir = tmp_path / "fonts"
    font_path = fonts_dir / "NotoSansJP.ttf"

    def fake_retrieve(url, dest):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "wb").close()

    with patch.object(font_manager, "FONTS_DIR", str(fonts_dir)):
        with patch.object(font_manager, "FONT_PATH", str(font_path)):
            with patch("urllib.request.urlretrieve", side_effect=fake_retrieve):
                result = font_manager.get_font_path()

    assert fonts_dir.exists()
    assert result == str(font_path)
