!!! Hint
    If you are familiar with `venv`, you can skip it

By a default behavior you have only _one_ Python in your "Terminal" and only one place where all your dependencies are stored. It's okay for local scripting, but when you develop everything in one _scope_, there is can be a requirement: _every project should have their own python version and own dependencies_. Otherwise, it can cause dependencies' version conflict 

!!! Note
    Any the environment's dependencies CLI scripts, for example, `pytest`, will be installed only inside the environment and does not available outside. So running "rules" for the script are the same as for `python` and described below

Dependencies isolation between your project can be done with `virtualenv` that is a built-in library in Python now

Executing this
```shell title="Terminal"
python -m venv .venv
```
means creating a new environment with `.venv` folder. You can see a such folder in your project

You can access to this environment by 3 ways:

## Full path
Just pass in terminal full pass to python executable: `:::shell .venv/bin/python`. It's a full copy of your python but with isolated dependencies. `:::shell .venv/bin/pip` works too (backslashes for Windows) 

## Activate environment
You can activate the environment and python executable will be accessible with `python3` by this command:

=== "Linux/MacOS"
    ```shell title="Terminal"
    .venv/bin/activate
    ```
=== "Windows"
    ```shell title="Terminal"
    .venv\Scripts\activate.bat
    ```

And a prefix `.venv` will be added to your command line prompt
***
To disable environment run this

=== "Linux/MacOS"
    ```shell title="Terminal"
    deactivate
    ```
=== "Windows"
    ```shell title="Terminal"
    .venv\Scripts\deactivate.bat
    ```

## Via Poetry
If your Poetry configured for local environments (as in this template), you can run
```shell title="Terminal"
poetry run python
```
and it will be executed in the environment