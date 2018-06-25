import argparse
import concurrent.futures
import math


PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    7882827029832222,
    9920209222920930]


PRIMES = PRIMES * 10


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def is_even(n):
    return n % 2 == 0


results = list()


def main(workers=4):
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        #for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        for result in executor.map(is_prime, PRIMES):
            results.append(result)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()        
    parser.add_argument('-c', '--cores', help='Number of cores (max)', type=int, required=True)
    args = parser.parse_args()

    main(workers=args.cores)
