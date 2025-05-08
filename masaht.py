pi = 3.141592653589793

def square_area(side):
    return side * side

def circle_area(radius):
    return pi * radius * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def get_func(ls):
    funcs = {
        'square': square_area,
        'circle': circle_area,
        'rectangle': rectangle_area,
        'triangle': triangle_area
    }
    return [funcs[shape] for shape in ls]


