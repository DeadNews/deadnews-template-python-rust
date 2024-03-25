import pytest
import deadnews_template_python_rust


def test_sum_as_string():
    assert deadnews_template_python_rust.sum_as_string(1, 1) == "2"
