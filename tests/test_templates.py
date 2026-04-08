import pytest
from PIL import Image
from templates import get_template


def _assert_valid_thumbnail(img: Image.Image) -> None:
    assert isinstance(img, Image.Image)
    assert img.size == (1280, 670)
    assert img.mode == "RGB"


def test_default_template_title_only():
    template = get_template("default")
    img = template.render(title="テストタイトル")
    _assert_valid_thumbnail(img)


def test_default_template_all_options():
    template = get_template("default")
    img = template.render(
        title="テストタイトル",
        subtitle="サブタイトルです",
        author="テスト著者",
    )
    _assert_valid_thumbnail(img)


def test_default_template_long_title():
    template = get_template("default")
    img = template.render(
        title="これは非常に長いタイトルで折り返しが必要になるはずです。テキストが正しく折り返されることを確認します。"
    )
    _assert_valid_thumbnail(img)


def test_unknown_template_raises():
    with pytest.raises(ValueError, match="Unknown template"):
        get_template("nonexistent")
