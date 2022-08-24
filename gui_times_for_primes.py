from time import time
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Times for Primes')

low_label = tk.Label(root, text="Number to start at", width=30, height=1)
low_label.grid(row=0, column=0)
lowest_number_var = tk.IntVar()
low_number_entry = tk.Entry(root, textvariable = lowest_number_var, width=30)
low_number_entry.grid(row=1, column=0)
low_number_entry.delete(0, "end")  # Clear the entry box

high_label = tk.Label(root, text="Number to stop at", width=30, height=1)
high_label.grid(row=0, column=1)
highest_number_var = tk.IntVar()
high_number_entry = tk.Entry(root, textvariable = highest_number_var, width=30)
high_number_entry.grid(row=1, column=1)
high_number_entry.delete(0, "end")  # Clear the entry box

time_label = tk.Label(root, text="Time elapsed (in seconds)", width=30, height=1, anchor='e')
time_label.grid(row=2, column=0)
time_elapsed = tk.StringVar()
time_elapsed.set("0")
searching_time = tk.Label(root, textvariable = time_elapsed, relief=SUNKEN, width=30, height=1, anchor='w')
searching_time.config(bg="white")
searching_time.grid(row=2, column=1)

prime_label = tk.Label(root, text="Most recently found prime number", width=30, height=1, anchor='e')
prime_label.grid(row=3, column=0)
this_number = StringVar()
this_number.set('')
current_number = tk.Label(root, textvariable=this_number, relief=SUNKEN, width=30, height=1, anchor='w')
current_number.config(bg="white")
current_number.grid(row=3, column=1)

number_of_primes_label = tk.Label(root, text="Number of primes found", width=30, height=1, anchor='e')
number_of_primes_label.grid(row=4, column=0)
primes_found = StringVar()
primes_found.set(0)
number_of_primes = tk.Label(root, textvariable=primes_found, relief=SUNKEN, width=30, height=1, anchor='w')
number_of_primes.config(bg="white")
number_of_primes.grid(row=4, column=1)


def is_prime(number, begin_time):
    root.update()
    is_it_prime = True
    for n in range(2, number):
        n_ratio = number/n
        time_elapsed.set(str(time() - begin_time))
        searching_time['textvariable'] = time_elapsed
        root.update()
        if n_ratio.is_integer():
            is_it_prime = False
            break
        root.update_idletasks()
    return is_it_prime


def list_primes(print_primes=True):
    start_number = int(low_number_entry.get())
    end_number = int(high_number_entry.get())
    root.update()
    primes_list = []
    begin_time = time()
    n_of_primes = 0
    for n in range(start_number, end_number):
        root.update()
        start_time = time()
        prime_test = is_prime(n, begin_time)
        finish_time = time()
        root.update()
        if prime_test is True:
            primes_list.append(n)
            n_of_primes += 1
            primes_found.set(str(n_of_primes))
            number_of_primes['textvariable'] = primes_found
            this_number.set(str(n))
            current_number['textvariable'] = this_number
            root.update()
            if print_primes:
                print(n, "  ", (finish_time - start_time), " seconds to validate    ", (time() - begin_time), " seconds in total")
        root.update()
        root.update_idletasks()
    return primes_list


start_button = tk.Button(root, text='Find those primes!', command=list_primes, width=30, height=1)
start_button.grid(row=5, column=0)
start_button = tk.Button(root, text='Quit', command=root.destroy, width=30, height=1)
start_button.grid(row=5, column=1)
root.mainloop()


print("\n", len(p_list), " prime numbers between {} and {}".format(lowest_number, highest_number))
print("\nThey are: ", p_list)
