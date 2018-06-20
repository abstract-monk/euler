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


