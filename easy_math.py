import operator as op

def setup():
    print("setting stuff up")

def calculate(number1, number2, operation):
    arithmetic_function = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    return arithmetic_function[operation](number1, number2)


def teardown():
    print("tearing stuff down")