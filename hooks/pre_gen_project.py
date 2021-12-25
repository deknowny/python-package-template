import sys

try:
    import pymake
except ImportError:
    print(
        "\n\nERROR: `py-make` is required. "
        "Run `{} -m pip install py-make`\n".format(
            sys.executable
        )
    )
    exit(1)