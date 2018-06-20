#!/usr/bin/python

# Project Euler Problem 3:
# ------------------------
# The prime factors of 13195 are 5, 7, 13, 29.
# What is the largest prime factor of the number 600851475143 ?

def isprime(n):
    ''' check if n is prime or not '''    
    # check special cases
    if n == 1:
        return False
    if n == 2:
        return True
    # check if divisible by only even prime number
    if n % 2 == 0:
        return False
    # check if divisible by only odd numbers up to n/2
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i+=2
    return True

def get_prime_factors(num):
   ''' return list of of prime factors for given number '''
   factors = []
   # check special case of 2
   if num % 2 == 0:
       factors.append(2)
   # check odd numbers up to n/2
   i = 3
   while i*i <= num:
       if num % i == 0 and isprime(i):
           factors.append(i)
       i+=2
   return factors

print(max(get_prime_factors(600851475143)))

