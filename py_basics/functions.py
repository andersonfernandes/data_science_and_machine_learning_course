def square_it(x):
    return x*x

print("Square of 12:", square_it(12))


# Functions as parameters
def call_func(f, x):
    return f(x)

print(call_func(square_it, 10))


# Lambda functions(inline functions)
print(call_func(lambda x: x*x*x, 2))
