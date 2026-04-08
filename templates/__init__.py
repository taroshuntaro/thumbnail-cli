from templates.base import BaseTemplate
from templates.default import DefaultTemplate
from templates.dark import DarkTemplate
from templates.gradient import (
    GradientTemplate,
    GradientSunsetTemplate,
    GradientOceanTemplate,
    GradientForestTemplate,
    GradientRoseTemplate,
    GradientSakuraTemplate,
)

_TEMPLATES: dict = {
    "default": DefaultTemplate,
    "dark": DarkTemplate,
    "gradient": GradientTemplate,
    "gradient-sunset": GradientSunsetTemplate,
    "gradient-ocean": GradientOceanTemplate,
    "gradient-forest": GradientForestTemplate,
    "gradient-rose": GradientRoseTemplate,
    "gradient-sakura": GradientSakuraTemplate,
}


def get_template(name: str) -> BaseTemplate:
    if name not in _TEMPLATES:
        raise ValueError(
            f"Unknown template: '{name}'. Available: {list(_TEMPLATES.keys())}"
        )
    return _TEMPLATES[name]()
