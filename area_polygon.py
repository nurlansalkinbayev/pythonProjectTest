import math

PI = 3.14


def area_of_polygon(s, n):
    area = (n * s ** 2) / (4 * math.tan(PI / n))
    return round(area, 2)


def main():
    s = int(input('Введите длину стороны многоугольника: '))
    n = int(input('Введите количество сторон многоугольника: '))
    total_area = area_of_polygon(s, n)
    print('Площадь многоугольника: ', total_area)


if __name__ == "__main__":
    main()
