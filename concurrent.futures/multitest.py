import argparse
import concurrent.futures
from random import randint


def is_even(n):
    return n % 2 == 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()        
    parser.add_argument('-c', '--cores', help='Number of cores (max)', type=int, required=True)
    parser.add_argument('-l', '--listlength', help='Length of test list', type=int, required=False, default=1000000)

    args = parser.parse_args()

    print('Generating test list of length {}...'.format(args.listlength))
    test_nums = [randint(1, 1000) for _ in range(0, args.listlength)]
    print('Done.')

    results = list()

    print('before with concurrent jawn.')
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.cores) as executor:
        print('executor')
        for throwaway, result in zip(test_nums, executor.map(is_even, test_nums)):
            print('Doing something with {}!'.format(result))
            results.append(result)
