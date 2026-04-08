from PIL import ImageDraw, ImageFont
from typing import List, Tuple


def wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    max_width: int,
) -> List[str]:
    """Wrap text to fit within max_width pixels.

    Wraps at word boundaries for Latin text; falls back to character-level
    wrapping for long words and CJK text (no spaces).
    """
    if not text:
        return [""]

    words = text.split(" ")
    lines: List[str] = []
    current = ""

    for word in words:
        word_w = draw.textbbox((0, 0), word, font=font)[2]
        if word_w > max_width:
            # Single word exceeds max_width: split at character level
            if current:
                lines.append(current.rstrip())
                current = ""
            for char in word:
                test = current + char
                if draw.textbbox((0, 0), test, font=font)[2] > max_width and current:
                    lines.append(current)
                    current = char
                else:
                    current = test
        else:
            test_line = (current + " " + word).lstrip() if current else word
            if draw.textbbox((0, 0), test_line, font=font)[2] > max_width and current:
                lines.append(current.rstrip())
                current = word
            else:
                current = test_line

    if current:
        lines.append(current.rstrip())

    return lines if lines else [""]


def draw_text_centered(
    draw: ImageDraw.ImageDraw,
    lines: List[str],
    font: ImageFont.FreeTypeFont,
    bbox: Tuple[int, int, int, int],
    color: Tuple[int, int, int],
    line_spacing: int = 12,
) -> None:
    """Draw lines of text horizontally and vertically centered within bbox."""
    x1, y1, x2, y2 = bbox
    box_w = x2 - x1
    box_h = y2 - y1

    line_h = draw.textbbox((0, 0), "Ag", font=font)[3]
    total_h = len(lines) * line_h + max(0, len(lines) - 1) * line_spacing
    start_y = y1 + max(0, (box_h - total_h) // 2)

    for i, line in enumerate(lines):
        text_w = draw.textbbox((0, 0), line, font=font)[2]
        x = x1 + (box_w - text_w) // 2
        y = start_y + i * (line_h + line_spacing)
        draw.text((x, y), line, font=font, fill=color)
