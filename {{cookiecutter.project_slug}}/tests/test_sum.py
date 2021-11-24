from {{cookiecutter.project_slug}}.mysum import mysum


def test_sum():
    assert mysum(2, 2) == 4
