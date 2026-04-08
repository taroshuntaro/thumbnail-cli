from typing import Optional
from PIL import Image, ImageDraw

from templates.base import BaseTemplate
from font_manager import get_font
from text_renderer import wrap_text, draw_text_centered

GRAD_TOP = (72, 52, 212)      # deep purple
GRAD_BOTTOM = (43, 134, 197)  # sky blue
TITLE_COLOR = (255, 255, 255)
SUBTITLE_COLOR = (220, 220, 255)
AUTHOR_COLOR = (180, 210, 230)
PADDING = 80


def _create_gradient(width: int, height: int, top: tuple, bottom: tuple) -> Image.Image:
    """Create a vertical linear gradient image."""
    gradient = Image.new("RGB", (1, height))
    for y in range(height):
        t = y / (height - 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        gradient.putpixel((0, y), (r, g, b))
    return gradient.resize((width, height), Image.NEAREST)


class GradientTemplate(BaseTemplate):
    def render(
        self,
        title: str,
        subtitle: Optional[str] = None,
        author: Optional[str] = None,
        font_weight: int = 700,
    ) -> Image.Image:
        img = _create_gradient(self.WIDTH, self.HEIGHT, GRAD_TOP, GRAD_BOTTOM)
        draw = ImageDraw.Draw(img)

        title_font = get_font(72, font_weight)
        subtitle_font = get_font(40, font_weight)
        author_font = get_font(30, font_weight)
        content_w = self.WIDTH - PADDING * 2

        title_lines = wrap_text(draw, title, title_font, content_w)
        title_lh = draw.textbbox((0, 0), "Ag", font=title_font)[3]
        title_block_h = len(title_lines) * title_lh + max(0, len(title_lines) - 1) * 12

        sub_block_h = 0
        if subtitle:
            sub_lh = draw.textbbox((0, 0), "Ag", font=subtitle_font)[3]
            sub_block_h = sub_lh + 24

        content_block_h = title_block_h + sub_block_h

        available_top = PADDING
        available_bottom = self.HEIGHT - (60 if author else PADDING)
        available_h = available_bottom - available_top
        block_y = available_top + max(0, (available_h - content_block_h) // 2)

        draw_text_centered(
            draw, title_lines, title_font,
            (PADDING, block_y, self.WIDTH - PADDING, block_y + title_block_h),
            TITLE_COLOR, line_spacing=12,
        )

        if subtitle:
            sub_y = block_y + title_block_h + 24
            sub_lines = wrap_text(draw, subtitle, subtitle_font, content_w)
            sub_lh = draw.textbbox((0, 0), "Ag", font=subtitle_font)[3]
            draw_text_centered(
                draw, sub_lines, subtitle_font,
                (PADDING, sub_y, self.WIDTH - PADDING, sub_y + sub_lh * len(sub_lines)),
                SUBTITLE_COLOR, line_spacing=8,
            )

        if author:
            draw.text(
                (PADDING, self.HEIGHT - 50),
                f"by {author}", font=author_font, fill=AUTHOR_COLOR,
            )

        return img
