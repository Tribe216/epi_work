import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    # TODO - you fill in here.
    if(intersection_found(R1, R2)):
        new_x = max(R1.x, R2.x)
        new_width = min(R1.x + R1.width, R2.x + R2.width) - new_x
        new_y = max(R1.y, R2.y)
        new_height = min(R1.y + R1.height, R2.y + R2.height) - new_y
        return Rectangle(new_x, new_y, new_width, new_height)
    else:
        return Rectangle(0,0,-1,-1)
   
def intersection_found(R1, R2):
    return (
        R1.width + R1.x >= R2.x and 
        R2.width + R2.x >= R1.x and
        R1.height + R1.y >= R2.y and 
        R2.height + R2.y >= R1.y
    )

def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
