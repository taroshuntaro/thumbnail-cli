from abc import ABC, abstractmethod
from typing import Optional
from PIL import Image


class BaseTemplate(ABC):
    WIDTH = 1280
    HEIGHT = 670

    @abstractmethod
    def render(
        self,
        title: str,
        subtitle: Optional[str] = None,
        author: Optional[str] = None,
        font_weight: int = 700,
    ) -> Image.Image:
        """Render a 1280×670 thumbnail image."""
        ...
