{% if cookiecutter.dhti == "y" -%}
import pytest
import requests


@pytest.fixture
def chain():
    from src.{{cookiecutter.project_slug}} import TestChain
    return TestChain().chain

def test_chain(chain):
    try:
        input = {
            "input": "Answer in one word: What is the capital of France?"
        }
        result = chain.invoke(input = input)
        assert result == 'Paris'
    except (requests.exceptions.ConnectionError) as e:
        print("ConnectionError: Skipping test")
        assert True
{%- elif cookiecutter.dhti == "n" -%}
from {{cookiecutter.project_slug}}.chain import chain


def test_chain():
    assert chain("foo") == "foo"
{% endif %}