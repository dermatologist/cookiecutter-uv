{% if cookiecutter.dhti == 'y' %}
from .chain import TestChain
__all__ = ["TestChain"]
{% endif %}