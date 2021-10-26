for i in range(10):
    print(i)
    if i > 5:
        raise ValueError("The value of i was " + str(i) + ", which is too high!")