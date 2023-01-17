# Problem Set 1
# Name: Ryan Oney
# Collaborators: N/A
# Time: 0.5 hours




# Problem 1
# write a program that computes and prints the 1000th prime number
def is_prime(num):
    # Returns True if num is prime, False otherwise
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

prime_cnt = 0
num = 1
last_prime = 1

while prime_cnt < 1000:
  if is_prime(num):
    prime_cnt += 1
    last_prime = num
  num += 1

print("The 1000th prime number is", last_prime)



# Problem 2
from math import *

def sum_prime_logs(n):
    # Returns the sum of the logs of all the primes between 2 and n, inclusive
    sum = 0
    for i in range(2, n+1):
        if is_prime(i):
            sum += log(i)
    return sum
    
def part_two(n):
    out = sum_prime_logs(n)
    print(out)
    print(n)
    print(out/n)

n = 50000
part_two(n)