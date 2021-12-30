Sometimes it is necessary to have a dependency with its source by a hand. Maybe you develop it or just fix some bugs or want to add new feature, anyway you need that its source code dto be placed with your source

## 1) Folder for your dependencies
It cannot be placed in `.venv` anymore. All dependencies' source code usually place in `vendor` folder, so, firstly, you need to create it

## 2) Add git submodule
```shell title="Terminal"
git add submodule {repository url} vendor/{repo name}
```
Submodule is correctly handled by Git when you do commit. It is recognized as another repository, not just an ordinary folder. It is still a Git repository that can be pulled, for example.  

!!! Hint
    Recommend you add such dependencies from your own fork of the original repository


## 3) Add it with `poetry`
```shell title="Terminal"
poetry add vendor/{name}
```
or another way as described in [how to add a dependency](./manage-dependencies.md)

And you see something like this
```toml title="pyproject.toml"
[tool.poetry.dependencies]
my-package = {path = "../my/path"}
```


!!! Tip
    If you want to edit the source code, you should add `:::toml develop = true`
    
    ```toml title="pyproject.toml"
    [tool.poetry.dependencies]
    my-package = {path = "../my/path", develop = true}
    ```
    