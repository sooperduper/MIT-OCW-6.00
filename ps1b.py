#!/usr/bin/env python
# encoding: utf-8
"""
ps1a.py
Problem Set 1b

Created by Sarah on 2012-02-20.
From: MIT OpenCourseWare
Course: Introduction to Computer Science and Programming
MIT Course Number: 6.00
"""

import math
from math import log

# Simple function to check if a number is prime
def isPrime(num):
  divisor = 1     # excluding 1, count the number of divisors
  counter = 1     # counter starts at 1
  squareRoot = math.sqrt(num)   # get the square root of the given number
  prime = False   # Returning prime, initiatizing as False
  
  # Until reaching the square root of the number, 
  # count how many divisors we encounter
  while (counter <= squareRoot):
    if num % counter == 0:
      divisor += divisor
    counter += 1
  
  # If the provided number only has 2 divisors it is prime
  if divisor == 2:
    return True
  # Otherwise, it's not prime
  else:
    return False

counter = 2     # Starting at 2 (not counting 1 as a prime)
primeCount = 0  # Stores a count of the prime numbers identified
target = 1000   # Goal is to identify the 1000th prime
logSum = 0

# Loop until reaching the 1000th prime
while (primeCount < target):
  
  # Find out if counter is prime
  currNum = isPrime(counter)
  
  # If the number is prime  
  if (currNum == True):
    print counter
    
    primeCount += 1     # Increase the counter
    
    logSum += log(counter)
      
    # End once the target is reached
    if (primeCount == target):
      print "1000th Prime: ", counter
      print "Sum of logs of primes: ", logSum
      print "Ratio: ", (float(logSum)/float(counter))
      
  counter += 1