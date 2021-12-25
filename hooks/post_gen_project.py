import os


os.system(
    "git init && "
    "git remote add origin https://github.com/{{cookiecutter.github_project_name}} && "
    "git checkout -b gh-pages && "
    "git commit --allow-empty -m \"Initial commit for GH Pages\" && "
    "git push origin gh-pages -f && "
    "git checkout -b {{cookiecutter.github_main_branch}} && "
    "make install-dev-all"
)