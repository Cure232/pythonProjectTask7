import multiprocessing
import random

R = 3.0                             # R - радиус окружности вписанной в квадрат, у которого a = 2R


def estimate_pi(n):
    count = 0                       # count - кол-во точек внутри окружности
    for _ in range(n):              # n - кол-во поставленных внутри квадрата точек
        x = random.uniform(-R, R)   # P = πR^2/a^2 = πR^2 / (2R)^2= πR^2/(2R)^2 = π/4
        y = random.uniform(-R, R)   # Где P = count / n
        if x ** 2 + y ** 2 <= R ** 2:
            count += 1
    return 4 * count / n            # return: Pi = count / n * 4


if __name__ == '__main__':
    num_points = int(input())

    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    chunk_size = num_points // num_processes

    results = pool.map(estimate_pi, [chunk_size] * num_processes)
    pi_estimate = sum(results) / num_processes

    print('Estimated value of pi:', pi_estimate)

