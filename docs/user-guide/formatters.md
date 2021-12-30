A **formatter** is a tool to format your code style automatically: remove unused imports or add new lines at the end of file etc.

Tools are setuped in the template are described below

!!! Hint
    You can run __all__ these formatters with `make format`. Do it when you do not want to waste time on code formatting by a hard

## `black`
Black is a formatter for your code style.

Suppose you have a file

```python title="file.py"
def  foo(a:int, b =  1):
    print (1 +1)
def bar(): pass
```

Run this
```shell title="Terminal"
black file.py
```

and get this
```python title="file.py"
def foo(a: int, b=1):
    print(1 + 1)


def bar():
    pass

```

It's useful for adding new lines between definitions and breaking too long lines of code, but it does not fix everything by PEP8. It is just for boilerplate fixes. Anyway, you should know PEP8 by hard so there won't be any issues with naming. If you are not sure with about your PEP8 knowledge, check out `pylint`.

## `isort`
`isort` is a formatter to fix your imports order to alphabet order and to divide imports to sections by PEP8

The same way as `black` this

```python
import pytest
import pathlib, os
from sumsub import sum

```

Converted to
```python
import os
import pathlib

from sumsub import sum

import pytest
```
It correctly divides into three sections of __built-in__, __local__, and __third-party__ imports 

## `autoflake`
`autoflake` is a more lightweight and just remove unused imports and unused variables as reported by pyflakes. The template is configured only for unused imports