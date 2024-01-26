import threading
import random


numbers = []


def filling_list():
    for i_nums in range(5):
        numbers.append(random.randint(1, 10))
    print(numbers)


def sum_list():
    print(sum(numbers))


def average():
    print(sum(numbers) / len(numbers))


filling_thread = threading.Thread(target=filling_list)
sum_thread = threading.Thread(target=sum_list)
avg_thread = threading.Thread(target=average)


if __name__ == '__main__':
    filling_thread.start()
    filling_thread.join()

    sum_thread.start()
    avg_thread.start()

    sum_thread.join()
    avg_thread.join()
