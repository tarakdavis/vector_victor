import math


def shape(vector):
    return (len(vector), )


def vector_add(a, b):
    if shape(a) != shape(b):
        raise ShapeError
    else:
        return [sum(values) for values in zip(a, b)]

def vector_sub(a, b):
    if shape(a) != shape(b):
        raise ShapeError
    else:
        return [x - y for x, y in zip(a, b)]




class ShapeError(Exception):
    pass
