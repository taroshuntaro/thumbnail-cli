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


def test_dark_template_title_only():
    template = get_template("dark")
    img = template.render(title="ダークテーマテスト")
    _assert_valid_thumbnail(img)


def test_dark_template_all_options():
    template = get_template("dark")
    img = template.render(
        title="ダークテーマ",
        subtitle="サブタイトル",
        author="著者",
    )
    _assert_valid_thumbnail(img)


def test_gradient_template_title_only():
    template = get_template("gradient")
    img = template.render(title="グラデーションテスト")
    _assert_valid_thumbnail(img)


def test_gradient_template_all_options():
    template = get_template("gradient")
    img = template.render(
        title="グラデーション",
        subtitle="サブタイトル",
        author="著者",
    )
    _assert_valid_thumbnail(img)


def test_gradient_sunset_template():
    img = get_template("gradient-sunset").render(title="夕焼けグラデーション")
    _assert_valid_thumbnail(img)


def test_gradient_ocean_template():
    img = get_template("gradient-ocean").render(title="オーシャングラデーション")
    _assert_valid_thumbnail(img)


def test_gradient_forest_template():
    img = get_template("gradient-forest").render(title="フォレストグラデーション")
    _assert_valid_thumbnail(img)


def test_gradient_rose_template():
    img = get_template("gradient-rose").render(title="ローズグラデーション")
    _assert_valid_thumbnail(img)


def test_gradient_sakura_template():
    img = get_template("gradient-sakura").render(title="桜グラデーション")
    _assert_valid_thumbnail(img)


def test_template_font_weight_bold():
    template = get_template("default")
    img = template.render(title="フォントウェイトテスト", font_weight=900)
    _assert_valid_thumbnail(img)


def test_template_font_weight_thin():
    template = get_template("dark")
    img = template.render(title="フォントウェイトテスト", font_weight=100)
    _assert_valid_thumbnail(img)
