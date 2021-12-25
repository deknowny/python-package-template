import sys

try:
    import pymake
except ImportError:
    print(
        "Error: `py-make` is required. "
        "Run `{} -m pip install py-make`".format(
            sys.executable
        )
    )