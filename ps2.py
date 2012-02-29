#!/usr/bin/env python
# encoding: utf-8
"""
ps2.py
Problem Set 2

Created by Sarah on 2012-02-27.
From: MIT OpenCourseWare
Course: Introduction to Computer Science and Programming
MIT Course Number: 6.00
"""

def nuggetDistribution(num):
	for a in range(num/6+1):
		for b in range(num/9+1):
			for c in range(num/20+1):
				if 6*a + 9*b + 20*c == num:
					print 'To purchase', userInput, 'number of McNuggets, you need to buy: '
					print 'Num of 6 packs: ', a
					print 'Num of 9 packs: ', b
					print 'Num of 20 packs: ', c
					return True	
	print 'You cannot buy that number of McNuggets'
	return False

userInput = int(raw_input("How many McNuggets do you want to buy? "))
numNuggets = nuggetDistribution(userInput)
