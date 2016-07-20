import math


def shape(vector):
    return (len(vector), )


def vector_add(a, b):
    return [x + y for x, y in zip(a, b)]

# class ShapeError(exception):
#     pass
