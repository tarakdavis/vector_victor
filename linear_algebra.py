import math


def shape(vector):
    return (len(vector), )


def vector_add(a, b):
    if shape(a) != shape(b):
        raise ShapeError
    else:
        return [sum(values) for values in zip(a, b)]


# def poop(*args):
#     print("the poop is", args)
# poop('butt', 'toilet')


class ShapeError(Exception):
    pass
