import time
import random

# получаем текущее локальное время в виде кортежа
current_time = time.localtime()
# преобразуем кортеж времени в строку
time_str = time.asctime(current_time)

# print(time_str)

start_time = time.time()

deck = list(range(1000, 10000))
hand = random.sample(deck, k=200)
# Сумма чисел в списке
hand_sum = sum(hand)
print(hand)
print(hand_sum)
end_time = time.time()

execution_time = end_time - start_time

print(f'Execution time: {execution_time} seconds.')
