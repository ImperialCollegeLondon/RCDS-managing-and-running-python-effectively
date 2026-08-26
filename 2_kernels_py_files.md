# Kernels and `.py` Files

## Kernels

A Python kernel is an operating system process that interprets and executes Python code. Many front-end interfaces such as editors, Jupyter Notebooks and terminal commands can create kernels. Kernels are created from a Python environment and are separate from the front-end interface that you use to write and run code. The kernel is responsible for executing the code you write in the front-end interface, and it can be started, stopped, and restarted independently of the front-end interface. In some cases, a kernel can persist for extended periods, allowing the persistence of variables and data between code executions.

## `.py` Files

A `.py` file is a plain-text file that contains Python code. It is a common way to write and save Python code for later execution. You can create a `.py` file using any text editor or integrated development environment (IDE) that supports Python. The file can contain functions, classes, and other Python constructs, and it can be executed by running the file in a Python interpreter.

Python files are the natural unit for Python code. They allow code to be built up in many different modules (`.py` files) that can be imported and used in other Python files. This modularity allows for code reuse and organization, making it easier to manage larger codebases. It also allows each module to have its own set of tests ensuring the code works correctly.

## Running `.py` Files in an Editors and IDEs

Editors and integrated development environments (IDEs) are software applications that provide a user interface for writing and running code. If you're viewing these notes in a Codespace, you will be using the Visual Studio Code (VS Code) editor. VS Code is a popular code editor that supports many programming languages, including Python. Like many editors and IDEs, VS Code can be customisaed using extensions. This Codespace is configured to have installed the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for VS Code, which provides features such as syntax highlighting, code completion and debugging tools, as well as the ability to run `.py` files directly. In the case of VS Code, this can be done by clicking the "play" button in the top right corner of the editor window.

**Task**: Open [`Examples/Editor_py/example.py`](Examples/Editor_py/example.py) in the editor and run the code. You should see the output in the terminal window at the bottom of the editor.

## Debugging `.py` Files in an Editor

You can debug a `.py` file in VS Code by setting breakpoints in the code and using the built-in debugger. To set a breakpoint, click in the left margin of the editor window next to the line of code where you want to pause execution. Then, open the "Run and Debug" view in the left sidebar and click "Run and Debug", or click the dropdown menu next to the "play" button in a Python file and click "Python Debugger: Debug Python file". The debugger will pause execution at the breakpoints, allowing you to inspect variables and step through the code. You can step forward through the breakpoints using the controls which appear at the top of the editor window. You can also use the "Run and Debug" view to view the call stack, variables, and other debugging information.

**Task**: Open [`Examples/Editor_py/example.py`](Examples/Editor_py/example.py) in the editor and set a breakpoint on each of the lines 4, 6 and 9. Then, run the debugger and step through the code to see how it executes. You should see that line 4 is never reached, line 6 is executed once and line 9 is executed multiple times.

## Running `.py` Files in a Terminal

To run a `.py` file in a terminal, navigate to the directory containing the file and use the `python` command followed by the file name. For example:

```bash
python Examples/Editor_py/example.py
```

**Task**: Open a terminal in the Codespace and run the `example.py` file using the command above. You should see the output in the terminal.

### Redirecting Output to a File

Sometimes, you may want to capture the terminal output of a Python script and save it to a file. For instance, you may expect a lot of output and want to save it for analysis, or you might be running a script on a remote server and want to save the output for later review.

Python produces two types of output: standard output (stdout) and standard error (stderr). Standard output is the normal output of a program, while standard error is used for error messages and diagnostics. By default, both types of output are displayed in the terminal, but you can redirect them to files.

We'll use the file [`Examples/Redirection/redirection.py`](Examples/Redirection/redirection.py) as an example. To redirect standard output to a file, you can use the `>` operator followed by the file name. For example:

```bash
python Examples/Redirection/redirection.py > output.txt
```

To redirect the standard error to a file, you can use the `2>` operator followed by the file name. For example:

```bash
python Examples/Redirection/redirection.py 2> error.txt
```

You can also redirect both standard output and standard error to different files at the same time. For example:

```bash
python Examples/Redirection/redirection.py > output.txt 2> error.txt
```

You can also redirect both standard output and standard error to the same file using the `&>` operator. For example:

```bash
python Examples/Redirection/redirection.py &> combined_output.txt
```

## Using `__name__`

Whenever you run a Python file, the interpreter sets a special built-in variable called `__name__`. If the file is being run as the main program, `__name__` is set to `"__main__"`. If the file is being imported as a module in another script, `__name__` is set to the name of the module. This allows us to write code that will only execute when the file is run directly using `if __name__ == "__main__":`, and not when it is imported as a module. This is often used to include test code or example usage in a module without executing it when the module is imported.

**Task**: Examine `Examples/name/file_1.py` and `Examples/name/file_2.py`. Notice that `file_1.py` contains a function definition and a test block that will only execute when the file is run directly. Run `file_1.py` in the terminal and observe the output. Then, run `file_2.py` in the terminal and observe that it imports `file_1.py` but does not execute the code on line 6.