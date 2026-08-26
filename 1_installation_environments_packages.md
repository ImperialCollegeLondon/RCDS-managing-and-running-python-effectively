# Installations, Environments and Packages

**During this section, follow along with activities outlined in the notes**

## Installation

You can install Python on your computer. An installation will typically be of a particular version. You can check the version by opening the terminal and typing `python --version`

**Task**: Run the command in the terminal to check your Python version.

When you install Python you will typically get the Python interpreter, the standard library, and a package manager called `pip` which allows you to install additional Python packages.

### Where to Install Python From

* Python comes pre-installed on most Linux distributions.
* Python can be installed from the [official Python website](https://www.python.org/downloads/).
* On macOS, Python can also be installed using package managers like Homebrew (`brew install python`).
* On Windows, Python can be installed from the [Microsoft Store](https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=en-GB&gl=GB) or from the official Python website.

It's possible to have multiple Python installations, e.g. both Python 3.13 and 3.14, on the same computer. This can work, but sometimes it can lead to conflicts or confusion about which version is being used. It's important to manage your Python installations carefully.

## Python Environments

It is also possible to create separate Python environments for different projects, based off of the same Python installation. This is useful when you want to manage dependencies for each project independently, avoiding conflicts between packages required by different projects.

### `venv`

`venv` is a module that comes with Python and allows you to create lightweight, isolated Python environments. Each environment has its own Python interpreter and can have its own set of installed packages, independent of other environments.

To create a new Python environment using `venv` you can use the command `python -m venv myenv`, where `myenv` is the name of the environment you want to create. This will create a directory containing the files of the environment. This can sit in the same directory as the project it is created for.

**Task**: Create a new Python environment using `venv` by running the command `python -m venv myenv` in the terminal.

#### Activating the Environment

After creating a new environment, you need to activate it to start using it. The command to activate the environment depends on your operating system:

* On Windows: `myenv\Scripts\activate`
* On macOS and Linux: `source myenv/bin/activate`

Once activated, your terminal prompt will typically change to indicate the active environment, and any Python commands you run will use the environment's interpreter and packages.

You  should see the name of the active environment in parentheses in your terminal prompt, indicating that the environment is currently active.

**Task**: Activate the environment you created by running the appropriate command for your operating system in the terminal. If you are running these materials in a Codespace, this is a Linux-based system.