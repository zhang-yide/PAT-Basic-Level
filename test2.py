import functools


def log(func):
    @functools.wraps(func)
    def deco(*arg, **kwarg):
        print('call %s():' % func.__name__)
        return func(*arg, **kwarg)
    return deco


@ log
def now():
    print('2019-12-25')
    print(int('10110', base=2))


if __name__ == '__main__':
    now()
    print(now.__name__)
