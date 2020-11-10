import time


def _time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result

    return wrapper


@_time
def test_build_list():
    l = list(range(1000000))


@_time
def test_build_set():
    s = set(range(1000000))


@_time
def test_build_tuple():
    t = tuple(range(1000000))


test_build_list()
test_build_set()
test_build_tuple()

@_time
def test_list():
    999999 in l

@_time
def test_set():
    999999 in s



# faster in searching an element set>list>tuple
