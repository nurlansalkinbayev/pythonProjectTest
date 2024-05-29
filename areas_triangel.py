def calculate_area_triangle(lenght, height):
    area = 0.5 * lenght * height
    return area


def main():
    lenght = float(input('Введите длину основания: '))
    height = float(input('Введите высоту отрезка опущенного на основание: '))
    total_area = calculate_area_triangle(lenght, height)
    print('Площадь треугольника:', total_area)


if __name__ == '__main__':
    main()