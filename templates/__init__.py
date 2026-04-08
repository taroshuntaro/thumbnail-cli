from templates.base import BaseTemplate
from templates.default import DefaultTemplate

_TEMPLATES: dict = {
    "default": DefaultTemplate,
}


def get_template(name: str) -> BaseTemplate:
    if name not in _TEMPLATES:
        raise ValueError(
            f"Unknown template: '{name}'. Available: {list(_TEMPLATES.keys())}"
        )
    return _TEMPLATES[name]()
