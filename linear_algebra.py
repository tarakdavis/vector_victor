# import math


def shape(vector):
    return (len(vector), )


def compare_shapes(*args):
    if not len({shape(item) for item in args}) == 1 == 1:
        raise ShapeError


def vector_add(a, b):
    compare_shapes(a, b)
    return [sum(values) for values in zip(a, b)]


def vector_sub(a, b):
    compare_shapes(a, b)
    return [x - y for x, y in zip(a, b)]


def vector_sum(*args):
    compare_shapes(*args)
    return [sum(values) for values in zip(*args)]


def dot(a, b):
    compare_shapes(a, b)
    return sum([x * y for x, y in zip(a, b)])


def vector_multiply(vector, scalar):
    return [number * scalar for number in vector]


def vector_mean(*args):
    return [sum(values)/len(values) for values in zip(*args)]


def magnitude(vector):
    return sum([number**2 for number in vector]) ** (1/2)


class ShapeError(Exception):
    pass
