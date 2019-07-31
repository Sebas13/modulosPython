from socketserver import StreamRequestHandler, TCPServer
from urllib.request import urlopen
import time
from functools import wraps

#
# class EchoHandler(StreamRequestHandler):
#     def handle(self):
#         for line in self.rfile:
#             self.wfile.write(b'GOT:' + line)
#
#
# serv = TCPServer((' ', 15000), EchoHandler)
#
# class UrlTemplate:
#     def __init__(self, template):
#         self.template = template
#
#     def open(self, **kwargs):
#         return urlopen(self.template.format_map(kwargs))
#
# # Carrying extra state with call back functions
#
#
# class ResultHandler:
#     def __init__(self):
#         self.sequence = 0
#
#     def handler(self,result):
#         print('[{}] Got: {}'.format(self.sequence, result))
#         self.sequence += 1

#
# def sample():
#     n = 0
#
#     # Closure Function
#     def func():
#         print('n=', n)
#
#     def get_n():
#         return n
#
#     def set_n(value):
#         nonlocal n
#         n = value
#
#
#
# f = sample()
# f.set_n(25)
# f()

_formats = {

    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == ' ':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


d = Date(2012, 12, 21)
# format(d)
# print(format(d))

#Wrap a function with extra code

# def timethis(func):
#     '''
#     Decorator that reports the execution time
#
#     '''
#
#     @wraps(func)
#     def wrapper(*args):
#         start = time.time()
#         result = func(*args)
#         end = time.time()
#         print(func.__name__, end-start)
#         return result
#     return wrapper()
#
# #Example of usage
#
#
# @timethis
# def countdown(n):
#     '''
#     Counts down
#     '''
#
#     while n > 0:
#         n -= 1
#
#
# countdown(55000)
# countdown(55000000000000)

#
def decorator(func):
    def check(a, inc):

        a = a if a > 0 else 0
        inc = inc if inc > 0 else 0

        ret = "~~~~~~   " + func(a, inc) + "   ~~~~~~"
        return ret
    return check

@decorator
def nextyear(age, inc):
    return "Age after %s year(s): %s" % (inc, age + inc)


# def decorator(func):
#     def check(a, inc):
#         # fixes both args so they are nonnegative
#         a = a if a > 0 else 0
#         inc = inc if inc > 0 else 0
#         # adds fanciness around returned statement
#         ret = "~~~ " + func(a, inc) + " ~~~\n"
#         return ret
#
#     return check
#
#
# @decorator
# def nextyear(age, inc):
#     return "Age after %s year(s): %s" % (inc, age + inc)


print(nextyear(-5, 3))  # 1
print(nextyear(18, -10))  # 19

print(nextyear(-5, 3))
print(nextyear(18, -10))

a_string = "This is a global variable"


def foo():
    print(locals())


print(globals())
foo()


def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def apply(func, x, y):
    return func(x, y)


print(apply(add, 2, 8))
print(apply(substract, 2, 8))
