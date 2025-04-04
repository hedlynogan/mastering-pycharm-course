# Your turn: Packaging

## Objectives

1. Create a project
2. Make it a package
3. Add a feature
4. Include a package definition file
5. Use the package

## Create a project

We are going to create the file structure of a package. That usually looks something like this:

```
project_folder
   |
   |- package
       | - __init__.py
       | - source_file1.py
       | - source_file2.py
       | - ...
   |- package definition file 1
   |- package definition file 2
   |- package definition file ...
   |- setup.py
```

You'll want *room* in your top level directory for those management files (e.g. license, readme, setup.py). So we are going to create `project_folder` as a PyCharm project.

For this section:

1. Create a folder called `calcy_package`
2. Create a virtual environment called .env in that folder
3. Open it in PyCharm

## Make it a package

Use PyCharm's "create package" feature to create the package implementation itself. Name it **`calcy`** as in calculator.

![Python package](./resources/new-package.png)

Notice it created the empty `__init__.py` for you and the folder icon is slightly different to indicate a package.

## Add a feature

We'll add a couple of simple math methods to our calculator. **Create another Python file** in the folder called `math.py` and add an `add(x, y)` and `subtract(x, y)` pair of methods to `math.py`.

To make importing it easier, add this line to `__init__.py`:

```python
from . import math
```

That means you can consume it by typing `import calcy` then calling `calcy.math.add(7, 11)`. If you omit this, you'll have to type `import calcy.math` to use the library like this even if you have already typed `impot calcy`.

Use the Python Console in PyCharm to test this (it adds the necessary path adjustments to run the package). For example, when I run the Python console, I see this output prior to the `>>>` prompt.

```python
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/michaelkennedy/code/calcy_package'])
```

This is PyCharm automatically extending the Python path. You do **not** need to do anything to make this happen. It's just PyCharm making life easy on us.

Now, in the console, here's one way to test it:

```python
import calcy
calcy.math.add(7, 5) # <-- outputs 12
```

In this special environment, it should work.

## Include a pyproject.toml

It's great you can run your code locally. But for real packages, you'll need to be able to install it for consumers. To do this, we need a `pyproject.toml` file. 

Luckily, we can easily add one. While, at the time of this writing, PyCharm doesn't have support to generate one, they are pretty straightforward. Here is a template you can use. 

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "calcy"
version = "0.0.1"
description = "A LIBRARY DESCRIPTION"
# readme = "readme.md"
license = "MIT"
authors = [
    { name = "YOUR NAME", email = "youremail@email.com" }
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]
keywords = ["calcy", "math", "cacluator"]
dependencies = []

[project.urls]
Homepage = "https://github.com/YOURNAME/calcy"

[tool.hatch.version]
path = "calcy/__init__.py"

[tool.hatch.build.targets.sdist]
include = ["calcy/", "readme.md"]

[tool.hatch.build.targets.wheel]
include = ["calcy/"]
```

1. Create a new file in the top-level folder and name it `pyproject.toml`. Then copy the contents above into it and adjust as needed (e.g. your name).

## Use the package

Now let's install the package. Open a terminal / shell. Activate the virtual environment in the project folder:

```bash
# mac / linux
. .venv/bin/activate 
```

```bash
# Windows
.venv/scripts/activate
```

Now run `pip install -e .` **from the same directory** as it is in as follows. The easiest way to do this is with PyCharm's builtin terminal (make sure the env is activated). If you have used uv, then you'll need `uv pip install -e .` (yes, the dot is part of the command, it means the current working directory)

Now, in the terminal, change out of that folder to somewhere else. Run Python and try to import and use it:

```python
$ (venv) python
import calcy
calcy.math.add(7, 5)
12
```

You've got it working!

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*
