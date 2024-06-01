import math

A = 9.8


def acceleration_of_object(v, A, d):
    speed = math.sqrt(v ** 2 + 2 * A * d)
    return speed


def main():
    d = float(input('Введите высоту с какой опущен объект: '))
    v = float(input("Введите скорость объекта: "))
    acceleration = acceleration_of_object(v, A, d)
    print(f'Скорость соприкосновения с землей: {acceleration}')


if __name__ == "__main__":
    main()
