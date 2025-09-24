{% if cookiecutter.dhti == 'y' %}
from .chain import DhtiChain
__all__ = ["DhtiChain"]
{% endif %}