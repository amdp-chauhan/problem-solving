# *args -- Remember '*' sign matters, instead of args, we can use anything we want
def multiply(a, b, *args):
    mul = a * b
    print(f'args: {args}')
    for num in args:
        mul *= num

    return mul

print(multiply(1, 2, 3, 4, 5)) #output: 120




# **kwargs -- Remember '**' sign matters, instead of kargs, we can use anything we want
def print_arguments(arg1, arg2, **kwargs):
    print(f'arg1: {arg1}')
    print(f'arg2: {arg2}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print(print_arguments(arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3", arg4 = "argument 4", arg5 = "argument 5"))
