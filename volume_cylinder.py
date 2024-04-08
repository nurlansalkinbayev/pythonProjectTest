import math


def calculate_cylinder_volume(radius, height):
    # Вычисляем площадь основания цилиндра (площадь круга)
    base_area = math.pi * radius ** 2
    # Вычисляем объем цилиндра
    volume = base_area * height
    return round(volume, 1)


def main():
    # Получаем радиус и высоту от пользователя
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    # Вычисляем и выводим объем цилиндра
    volume = calculate_cylinder_volume(radius, height)
    print("Объем цилиндра:", volume)


if __name__ == "__main__":
    main()

