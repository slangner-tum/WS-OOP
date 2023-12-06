def example_function(param1, param2, param3=0):
    # code section
    result = param1 * param2 + param3  # calculating

    # return section
    return result


def func_no_return(param1):
    print(f"parameter = {param1}")
    return


def func_one_return(param1, param2):
    return param1 + param2


def func_multiple_return(param1, param2):
    return param1 * 2, param2 * 3


def avg_bad(a, b):
    return a + b / 2


def avg_good(a, b):
    return (a + b) / 2




if __name__ == '__main__':
    print(f"return value of {func_no_return.__name__}: {func_no_return(5)}")
    print(f"return value of {func_one_return.__name__}: {func_one_return(5, 6)}")
    print(f"return value of {func_multiple_return.__name__}: {func_multiple_return(2, 3)}")
