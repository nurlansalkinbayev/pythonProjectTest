import time

# получаем текущее локальное время в виде кортежа
current_time=time.localtime()
# преобразуем кортеж времени в строку
time_str=time.asctime(current_time)

print(time_str)

