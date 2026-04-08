from PIL import Image, ImageDraw, ImageFont
import text_renderer


def _make_draw():
    img = Image.new("RGB", (1280, 670), (255, 255, 255))
    return ImageDraw.Draw(img)


def _default_font():
    return ImageFont.load_default()


def test_wrap_text_returns_list():
    draw = _make_draw()
    font = _default_font()
    result = text_renderer.wrap_text(draw, "Hello world", font, 1000)
    assert isinstance(result, list)
    assert len(result) >= 1


def test_wrap_text_wraps_long_text():
    draw = _make_draw()
    font = _default_font()
    result = text_renderer.wrap_text(draw, "A" * 300, font, 100)
    assert len(result) > 1


def test_wrap_text_empty_string():
    draw = _make_draw()
    font = _default_font()
    result = text_renderer.wrap_text(draw, "", font, 1000)
    assert result == [""]


def test_draw_text_centered_does_not_raise():
    draw = _make_draw()
    font = _default_font()
    text_renderer.draw_text_centered(
        draw, ["テスト", "テキスト"], font,
        (0, 0, 1280, 670), (0, 0, 0)
    )


def test_wrap_text_japanese_wraps_by_char():
    draw = _make_draw()
    font = _default_font()
    # Japanese text has no spaces; must wrap at character boundary
    result = text_renderer.wrap_text(draw, "あいうえおかきくけこ" * 5, font, 100)
    assert len(result) > 1


def test_wrap_text_kinsoku_no_punct_at_line_start():
    draw = _make_draw()
    font = _default_font()
    # 「。」should not appear at the start of any line
    result = text_renderer.wrap_text(
        draw, "あいうえおかきくけこさしすせそ。たちつてとなにぬねの", font, 100
    )
    for line in result[1:]:  # skip first line
        assert not line.startswith("。"), f"Line starts with 。: {line!r}"
