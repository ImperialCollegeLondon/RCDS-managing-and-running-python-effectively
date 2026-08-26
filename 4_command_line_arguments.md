# Command Lines Arguments

When running a program on the command line, the name of the command can often be followed by one or more arguments, which are used to modify the behaviour of the command. We've already seen how the command `python` can be followed by the name of a Python file to run that file, and how the command `python -m` can be followed by the name of a module to run that module. 

In this section, we'll look at how to pass arguments to a Python program, and how to access those arguments from within the program. This prevents having to edit the program to change its behaviour which, in turn, makes it easier to give it to other people to use.

## Getting Arguments with `sys.argv`

There are many ways to get arguments from the command line in Python, but the simplest is to use the `sys.argv` list. This list contains all of the arguments that were passed to the program, including the name of the program itself as the first element. The `sys` module is part of the Python standard library, so you don't need to install anything to use it. You just need to import it at the top of your program.

`sys.argv` is a list of strings, the first of which is the name of the program, and the rest are the arguments that were passed to the program. For example, if you run the command:

```bash
python my_program.py arg1 arg2 arg3
```

`sys.argv` will be:

```python
['my_program.py', 'arg1', 'arg2', 'arg3']
```

As each entry is a string, you may need to convert them to approriate types using functions like `int()` or `float()` if you want to use them as numbers or `bool()` if you want to use them as booleans.

**Tak**: Examine [`Examples/Arguments/addition.py`](Examples/Arguments/addition.py) to see how to use `sys.argv` to get arguments from the command line. Run the code from the command line, providing different numbers of numeric arguments, and see how the output changes.

## Exercise: Division using `sys.argv`

Create a new script named `divider.py` designed to calculate and print the result when one value is divided by another. The script should read arguments provided on the command line. The first is the numerator, the second is the denominator. So, using the command `python divider.py 5.2 2` should cause the value `2.6` to be printed.
Consider what your code should do if:
- The number of arguments provided is not 2
- The arguments cannot be converted to floats

A sample solution can be found in [`sample_solutions/divider.py`](sample_solutions/divider.py).

### Limits to `sys.argv`

`sys.argv` is a simple way to get arguments from the command line, but it starts to become cumbersome when working with large numbers of arguments, names arguments, or optional arguments. For more complex inputs, you may want to use the [`argparse`](https://docs.python.org/3/library/argparse.html) module, which is also part of the Python standard library.

## Limits to Command Line Arguments

Command line arguments are great when you want to run a program, specifying a few inputs to describe each run. However, when the information you want to provide to a program gets more complex, command line arguments can become unwieldy and difficult to manage. In such cases, it may be better to specify the inputs in a configuration or input file that the program can read. This allows you to specify much more information, save input files for later use, or iterate on files, keeping an input file for each case.
