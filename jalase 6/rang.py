def red(f):
    def inner(*args, **kawargs):
        return "\033[31;1m " + f(*args, **kawargs) +"\033[0m"

    return inner


def yellow(f):
    def inner(*args, **kawargs):
        return "\033[33;1m " + f(*args, **kawargs) +"\033[0m"

    return inner

def green(f):
    def inner(*args, **kawargs):
        return "\033[32;4m " + f(*args, **kawargs) +"\033[0m"


@red
def echo(a):
    return a


print(echo("hello"))

@yellow
def echo(b):
     return b

print(echo("how are you"))

@green
def echo(c):
     return c
print(echo("ggg"))




