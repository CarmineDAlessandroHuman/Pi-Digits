from circle import Circle
from point import Point

import sys

def main():
    radius = int(sys.argv[1])
    circle = Circle(radius)

    if radius > 1000:
        print('Warning: long waiting time')

    area = 0.0
    for x in range(precision*2):
        for y in range(precision*2):
            point = Point(x, y)
            if circle.is_in_the_circle(point):
                area += 1

    pi = area / precision**2
    print(pi)

if __name__ == "__main__":
    main()
