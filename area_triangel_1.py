import math


def calculate_area_triangle_1(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
    return round(area, 2)


def is_valid_triangle(s1, s2, s3):
    return s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1


def main():
    s1 = float(input("Введите длину 1 стороны треугольника: "))
    s2 = float(input("Введите длину 2 стороны треугольника: "))
    s3 = float(input("Введите длину 3 стороны треугольника: "))

    if is_valid_triangle(s1, s2, s3):
        total_area = calculate_area_triangle_1(s1, s2, s3)
        print('Площадь треугольника:', total_area)
    else:
        print('Ошибка: введенные значения не могут образовать треугольник.')


if __name__ == '__main__':
    main()
