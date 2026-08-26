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

It's possible to have multiple Python installations, e.g. both Python 3.13 and 3.14, on the same computer. This can work, but sometimes it can lead to conflicts or confusion about which version is being used.

## Python Environments and `venv`

It is also possible to create separate Python environments for different projects, based off of the same Python installation. This is useful when you want to manage dependencies for each project independently, avoiding conflicts between packages required by different projects.

`venv` is a module that comes with Python and allows you to create lightweight, isolated Python environments. Each environment has its own Python interpreter and can have its own set of installed packages, independent of other environments.

To create a new Python environment using `venv` you can use the command `python -m venv myenv`, where `myenv` is the name of the environment you want to create. This will create a directory containing the files of the environment. This can sit in the same directory as the project it is created for.

**Task**: Create a new Python environment using `venv` by running the command `python -m venv myenv` in the terminal.

### Activating the Environment

After creating a new environment, you need to activate it to start using it. The command to activate the environment depends on your operating system:

* On Windows: `myenv\Scripts\activate`
* On macOS and Linux: `source myenv/bin/activate`

Once activated, your terminal prompt will typically change to indicate the active environment, and any Python commands you run will use the environment's interpreter and packages.

You  should see the name of the active environment in parentheses in your terminal prompt, indicating that the environment is currently active.

**Task**: Activate the environment you created by running the appropriate command for your operating system in the terminal. If you are running these materials in a Codespace, this is a Linux-based system.

### Deactivating the Environment

To deactivate the Python environment, run the command `deactivate` in the terminal. This will return you to the system's default Python interpreter and packages.

**Task**: Deactivate the environment by running the command `deactivate` in the terminal.

## Packages

Packages are collections of Python modules that provide additional functionality. There are many packages in Python and the variety of them is one of Python's strengths - finding the right package for your needs can save you a lot of time and effort.

### Package Managers and `pip`

A package manager is a tool that automates the process of installing, upgrading, configuring, and removing packages. The most commonly used package manager for Python is `pip`, which comes pre-installed with Python. `pip` accesses packages from the [Python Package Index (PyPI)](https://pypi.org/), which is a repository of software for the Python programming language.

To install a package using `pip`, you can use the command:

```bash
pip install package_name
```

where `package_name` is the name of the package you want to install. To uninstall a package, you can use the command:

```bash
pip uninstall package_name
```

 You can also specify a version of the package by using 

```bash
pip install package_name==version_number
```

**Task**: Activate your virtual environment in the terminal. Install the `numpy` package using `pip` by running the command `pip install numpy` in the terminal. Observe what version number of the package is installed. Then, uninstall it by running the command `pip uninstall numpy`. Finally, install version 2.3.3 of `numpy` and observe the version number of the package that is installed.

## Requirements Files

A requirements file is a text file that lists the packages and their versions required for a Python project. It allows you to easily share your project's dependencies with others or recreate the same environment on another machine.

The file is typically named `requirements.txt` and is often found in the root directory of a Python project. Each line in the file specifies a package and its version, for example:

```
numpy==2.3.3
pandas==1.5.0
```

The `==2.3.3` is optional and specifies the exact version of the package to install. If you omit the version, `pip` will install the latest version available.

It is possible to create a requirements file manually or automatically. To create a requirements file the specifies all of the packages and their versions that are currently installed in your environment, you can use the command:

```bash
pip freeze > requirements.txt
```

To install the contents of a requirements file, you can use the command:

```bash
pip install -r requirements.txt
```

The `-r` flag tells `pip` to install the packages listed in the requirements file.

** Task**: Create a requirements file for your virtual environment by running the command `pip freeze > requirements.txt` in the terminal. Open the `requirements.txt` file and observe its contents. Add the package `scipy` (don't specify a version number) to the requirements file manually and save it. Then, install the packages listed in the requirements file in your virtual environment by running the command `pip install -r requirements.txt` in the terminal. You should see that `numpy` is already installed, but `scipy` is installed as a new package.