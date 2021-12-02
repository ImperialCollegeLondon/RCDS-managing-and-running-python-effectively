for i in range(10):
    # The output of this print statement may be redirected from stdout
    print(i)
    if i > 5:
        # This output of this exception may be redirected from stderr
        raise ValueError("The value of i was " + str(i) + ", which is too high!")