"""Entrypoint for app, enables execution with `python -m deadnews_template_python_rust`."""

from deadnews_template_python_rust.deadnews_template_python_rust import sum_as_string

if __name__ == "__main__":
    print(sum_as_string(2, 2))  # noqa: T201
