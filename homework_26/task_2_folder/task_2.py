import threading
import random


# E:\python\study_1\study_1\homework_26\task_2_folder\random_nums.txt

path = input('Enter file path: ')


def filling_nums():
    with open(path, 'w') as f:
        for i_nums in range(10):
            f.write(f'{random.randint(1, 10)}\n')


def filling_simple():
    with open('simple_nums.txt', 'w') as f:
        with open(path, 'r') as rf:
            for cur_num in rf.readlines():
                if simple_nums(int(cur_num)):
                    f.write(f'{cur_num}')


def filling_fact():
    with open('factorial.txt', 'w') as f:
        with open(path, 'r') as rf:
            for cur_num in rf.readlines():
                factorial = calc_factorial(int(cur_num))
                f.write(f'{factorial}\n')


def simple_nums(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True


def calc_factorial(num):
    factorial = 1
    while num >= 1:
        factorial *= num
        num -= 1
    return str(factorial)


nums_thread = threading.Thread(target=filling_nums)
simple_thread = threading.Thread(target=filling_simple)
fact_thread = threading.Thread(target=filling_fact)


if __name__ == '__main__':
    nums_thread.start()
    nums_thread.join()

    fact_thread.start()
    simple_thread.start()
    fact_thread.join()
    simple_thread.join()
