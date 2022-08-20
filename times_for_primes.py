from time import time


def is_prime(number):
    is_it_prime = True
    for n in range(2, number):
        n_ratio = number/n
        if n_ratio.is_integer():
            is_it_prime = False
    return is_it_prime


def list_primes(start_number, end_number, print_primes=True):
    primes_list = []
    for n in range(start_number, end_number):
        start_time = time()
        prime_test = is_prime(n)
        finish_time = time()
        if prime_test is True:
            primes_list.append(n)
            if print_primes:
                print(n, "  ", (finish_time - start_time), " seconds to validate")
    return primes_list

lowest_number = 1000
highest_number = 10000

p_list = list_primes(lowest_number, highest_number)
print("\n", len(p_list), " prime numbers between {} and {}".format(lowest_number, highest_number))
print("\nThey are: ", p_list)


