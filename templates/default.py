from typing import Optional
from PIL import Image, ImageDraw

from templates.base import BaseTemplate
from font_manager import get_font
from text_renderer import wrap_text, draw_text_centered

BG_COLOR = (255, 255, 255)
TITLE_COLOR = (30, 30, 30)
SUBTITLE_COLOR = (90, 90, 90)
AUTHOR_COLOR = (140, 140, 140)
ACCENT_COLOR = (41, 128, 185)
PADDING = 80
ACCENT_H = 8


class DefaultTemplate(BaseTemplate):
    def render(
        self,
        title: str,
        subtitle: Optional[str] = None,
        author: Optional[str] = None,
        font_weight: int = 700,
    ) -> Image.Image:
        img = Image.new("RGB", (self.WIDTH, self.HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(img)

        title_font = get_font(72, font_weight)
        subtitle_font = get_font(48, font_weight)
        author_font = get_font(30, font_weight)
        content_w = self.WIDTH - PADDING * 2

        # Accent bar removed — clean white background only

        # Calculate content block height
        title_lines = wrap_text(draw, title, title_font, content_w)
        title_lh = draw.textbbox((0, 0), "Ag", font=title_font)[3]
        title_block_h = len(title_lines) * title_lh + max(0, len(title_lines) - 1) * 12

        sub_block_h = 0
        if subtitle:
            sub_lh = draw.textbbox((0, 0), "Ag", font=subtitle_font)[3]
            sub_block_h = sub_lh + 24  # 24px gap above subtitle

        content_block_h = title_block_h + sub_block_h

        # Vertically center content block
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
