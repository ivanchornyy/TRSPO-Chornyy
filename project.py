import threading
import time

def calculate_square(numbers):
    for n in numbers:
        print(f"Square of {n}: {n * n}")
        time.sleep(1)

def calculate_cube(numbers):
    for n in numbers:
        print(f"Cube of {n}: {n * n * n}")
        time.sleep(1)

numbers = [2, 3, 4, 5]

# Створюємо потоки
thread1 = threading.Thread(target=calculate_square, args=(numbers,))
thread2 = threading.Thread(target=calculate_cube, args=(numbers,))

# Запускаємо потоки
thread1.start()
thread2.start()

# Чекаємо завершення потоків
thread1.join()
thread2.join()

print("Обчислення завершено.")
