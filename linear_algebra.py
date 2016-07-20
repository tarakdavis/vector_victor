# import math


def shape(vector):
    return (len(vector), )


def compare_shapes(*args):
    return len(set([shape(item) for item in args])) == 1


def vector_add(a, b):
    if not compare_shapes(a, b):
        raise ShapeError
    else:
        return [sum(values) for values in zip(a, b)]


def vector_sub(a, b):
    if not compare_shapes(a, b):
        raise ShapeError
    else:
        return [x - y for x, y in zip(a, b)]


def vector_sum(*args):
    if not compare_shapes(*args):
        raise ShapeError
    return [sum(values) for values in zip(*args)]


def dot(a, b):
    if not compare_shapes(a, b):
        raise ShapeError
    else:
        return sum([x * y for x, y in zip(a, b)])


class ShapeError(Exception):
    pass
