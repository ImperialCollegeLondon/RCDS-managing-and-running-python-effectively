# This function contains an assert statement which will fail
def assert_function():
    assert(False)

# This print statement will always be executed
print("I'm printing")

#If this file has been called directly, call the function
if __name__ == "__main__":
    assert_function()