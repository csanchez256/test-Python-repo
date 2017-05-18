#!/usr/bin/env python
import math #this is a module

print "Hello World!"

x = input("Enter a number: ")

print x

print 1.0/2.0 #floating point division

print 2**8 #double star for exponents

print 0xAF #Hexadecimal

print 010  #Octal

print "exponent function"
print math.pow(2,3)

print "example of lists"
months = ['jan','feb','mar','april']
print months[1]

print "slicing examples"
print months[:3]
print months[1:3] #Gives you a range from [start:end]

#Sorts a list, also \n to add spaces
print "sorting example\n\n"
nums = [3,8,5,6,0,1,9]
nums.sort()
print nums

#creating a function
def foo(talk):
	return "This is a function, " + talk  

print foo("foo")
print "\n"

#Example of a dictionary
memberAge = {'bob': '20', 'bill': '25', 'susan': '30', 'kevin': '35'}
print "Accessing value from dictionary " + memberAge['bob'] + '\n'

#For loops and iterating through dictionaries
print 'iterating through a list'
for month in months:
	print month

print 'iterating range()\n'
for number in range(10):
	print number

print '\n'

#Ranges work like slices, they include the first limit, but not the second limit
for n in range(2,10):
	print n

#Casting a string to a float, and then a float to an integer
print 'casting a string'
a = '3.14159265'
print float(a)
print int(float(a))

#Split String
b = '/usr/bin/env'
print b.split('/')
