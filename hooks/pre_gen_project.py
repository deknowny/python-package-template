import sys

try:
    import pymake
except ImportError:
    print(
        "\n\nError: `py-make` is required. "
        "Run `{} -m pip install py-make`".format(
            sys.executable
        )
    )
    exit(1)