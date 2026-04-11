from typing import Optional, Tuple
from PIL import Image, ImageDraw

from templates.base import BaseTemplate
from font_manager import get_font
from text_renderer import wrap_text, draw_text_centered

PADDING = 80
ColorRGB = Tuple[int, int, int]


class SplitTemplate(BaseTemplate):
    """Left accent color panel + right white panel."""

    ACCENT_COLOR: ColorRGB = (26, 35, 126)   # Deep indigo
    BG_COLOR: ColorRGB = (255, 255, 255)
    TITLE_COLOR: ColorRGB = (30, 30, 30)
    SUBTITLE_COLOR: ColorRGB = (90, 90, 90)
    AUTHOR_COLOR: ColorRGB = (200, 200, 230)
    SPLIT_RATIO: float = 0.36

    def render(
        self,
        title: str,
        subtitle: Optional[str] = None,
        author: Optional[str] = None,
        font_weight: int = 700,
    ) -> Image.Image:
        img = Image.new("RGB", (self.WIDTH, self.HEIGHT), self.BG_COLOR)
        draw = ImageDraw.Draw(img)

        split_x = int(self.WIDTH * self.SPLIT_RATIO)
        draw.rectangle([(0, 0), (split_x, self.HEIGHT)], fill=self.ACCENT_COLOR)

        title_font = get_font(72, font_weight)
        subtitle_font = get_font(48, font_weight)
        author_font = get_font(28, font_weight)

        right_start = split_x + 48
        content_w = self.WIDTH - right_start - PADDING

        title_lines = wrap_text(draw, title, title_font, content_w)
        title_lh = draw.textbbox((0, 0), "Ag", font=title_font)[3]
        title_block_h = len(title_lines) * title_lh + max(0, len(title_lines) - 1) * 12

        sub_block_h = 0
        if subtitle:
            sub_lh = draw.textbbox((0, 0), "Ag", font=subtitle_font)[3]
            sub_block_h = sub_lh + 24

        content_block_h = title_block_h + sub_block_h
        available_top = PADDING
        available_bottom = self.HEIGHT - PADDING
        block_y = available_top + max(0, (available_bottom - available_top - content_block_h) // 2)

        draw_text_centered(
            draw, title_lines, title_font,
            (right_start, block_y, self.WIDTH - PADDING, block_y + title_block_h),
            self.TITLE_COLOR, line_spacing=12,
        )

        if subtitle:
            sub_y = block_y + title_block_h + 24
            sub_lines = wrap_text(draw, subtitle, subtitle_font, content_w)
            sub_lh = draw.textbbox((0, 0), "Ag", font=subtitle_font)[3]
            draw_text_centered(
                draw, sub_lines, subtitle_font,
                (right_start, sub_y, self.WIDTH - PADDING, sub_y + sub_lh * len(sub_lines)),
                self.SUBTITLE_COLOR, line_spacing=8,
            )

        if author:
            draw.text(
                (20, self.HEIGHT - 50),
                f"by {author}", font=author_font, fill=self.AUTHOR_COLOR,
            )

        return img


class BorderTemplate(BaseTemplate):
    """White background with a thick colored border frame."""

    ACCENT_COLOR: ColorRGB = (41, 128, 185)  # Blue
    BG_COLOR: ColorRGB = (255, 255, 255)
    TITLE_COLOR: ColorRGB = (30, 30, 30)
    SUBTITLE_COLOR: ColorRGB = (90, 90, 90)
    AUTHOR_COLOR: ColorRGB = (140, 140, 140)
    BORDER_WIDTH: int = 18

    def render(
        self,
        title: str,
        subtitle: Optional[str] = None,
        author: Optional[str] = None,
        font_weight: int = 700,
    ) -> Image.Image:
        img = Image.new("RGB", (self.WIDTH, self.HEIGHT), self.BG_COLOR)
        draw = ImageDraw.Draw(img)

        bw = self.BORDER_WIDTH
        draw.rectangle(
            [(0, 0), (self.WIDTH - 1, self.HEIGHT - 1)],
            outline=self.ACCENT_COLOR,
            width=bw,
        )

        title_font = get_font(72, font_weight)
        subtitle_font = get_font(48, font_weight)
        author_font = get_font(30, font_weight)

        inner_pad = bw + PADDING
        content_w = self.WIDTH - inner_pad * 2

        title_lines = wrap_text(draw, title, title_font, content_w)
        title_lh = draw.textbbox((0, 0), "Ag", font=title_font)[3]
        title_block_h = len(title_lines) * title_lh + max(0, len(title_lines) - 1) * 12

        sub_block_h = 0
        if subtitle:
            sub_lh = draw.textbbox((0, 0), "Ag", font=subtitle_font)[3]
            sub_block_h = sub_lh + 24

        content_block_h = title_block_h + sub_block_h
        available_top = inner_pad
        available_bottom = self.HEIGHT - (bw + 60 if author else inner_pad)
        block_y = available_top + max(0, (available_bottom - available_top - content_block_h) // 2)

        draw_text_centered(
            draw, title_lines, title_font,
            (inner_pad, block_y, self.WIDTH - inner_pad, block_y + title_block_h),
            self.TITLE_COLOR, line_spacing=12,
        )

        if subtitle:
            sub_y = block_y + title_block_h + 24
            sub_lines = wrap_text(draw, subtitle, subtitle_font, content_w)
            sub_lh = draw.textbbox((0, 0), "Ag", font=subtitle_font)[3]
            draw_text_centered(
                draw, sub_lines, subtitle_font,
                (inner_pad, sub_y, self.WIDTH - inner_pad, sub_y + sub_lh * len(sub_lines)),
                self.SUBTITLE_COLOR, line_spacing=8,
            )

        if author:
            draw.text(
                (inner_pad, self.HEIGHT - bw - 46),
                f"by {author}", font=author_font, fill=self.AUTHOR_COLOR,
            )

        return img


class StripeTemplate(BaseTemplate):
    """White background with a diagonal stripe pattern."""

    STRIPE_COLOR: ColorRGB = (220, 232, 255)  # Light blue tint
    BG_COLOR: ColorRGB = (255, 255, 255)
    TITLE_COLOR: ColorRGB = (30, 30, 30)
    SUBTITLE_COLOR: ColorRGB = (90, 90, 90)
    AUTHOR_COLOR: ColorRGB = (140, 140, 140)
    STRIPE_WIDTH: int = 18
    STRIPE_GAP: int = 42

    def render(
        self,
        title: str,
        subtitle: Optional[str] = None,
        author: Optional[str] = None,
        font_weight: int = 700,
    ) -> Image.Image:
        img = Image.new("RGB", (self.WIDTH, self.HEIGHT), self.BG_COLOR)
        draw = ImageDraw.Draw(img)

        # Draw 45° diagonal stripes across the full canvas
        step = self.STRIPE_WIDTH + self.STRIPE_GAP
        for i in range(-self.HEIGHT, self.WIDTH + self.HEIGHT, step):
            draw.line(
                [(i, 0), (i + self.HEIGHT, self.HEIGHT)],
                fill=self.STRIPE_COLOR,
                width=self.STRIPE_WIDTH,
            )

        title_font = get_font(72, font_weight)
        subtitle_font = get_font(48, font_weight)
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
        block_y = available_top + max(0, (available_bottom - available_top - content_block_h) // 2)

        draw_text_centered(
            draw, title_lines, title_font,
            (PADDING, block_y, self.WIDTH - PADDING, block_y + title_block_h),
            self.TITLE_COLOR, line_spacing=12,
        )

        if subtitle:
            sub_y = block_y + title_block_h + 24
            sub_lines = wrap_text(draw, subtitle, subtitle_font, content_w)
            sub_lh = draw.textbbox((0, 0), "Ag", font=subtitle_font)[3]
            draw_text_centered(
                draw, sub_lines, subtitle_font,
                (PADDING, sub_y, self.WIDTH - PADDING, sub_y + sub_lh * len(sub_lines)),
                self.SUBTITLE_COLOR, line_spacing=8,
            )

        if author:
            draw.text(
                (PADDING, self.HEIGHT - 50),
                f"by {author}", font=author_font, fill=self.AUTHOR_COLOR,
            )

        return img
