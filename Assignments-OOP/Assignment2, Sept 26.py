'''
Name: Cameron Troester
Email: cdtroester1022@my.mwsu.edu
Assignment: Homework 2 - Getting your python feet wet
Due: 26 Sep @ 1:00 p.m
'''

from fractions import gcd

class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)

    def __add__(self,rhs):

        counter = 0
        #Creating a temp of the numerator of the 2 fractions
        tempnum = (self.numerator * rhs.denominator) + (self.denominator * rhs.numerator)
        
        #Creating a temp of the denominator of the 2 fractions
        tempdem = self.denominator * rhs.denominator

        #creating a temp of the Gcd of the new fraction, imported from fraction
        factor = gcd(tempnum, tempdem)

        #This whole block basically deals with reducing if whole numbers
        #are possible
        while (tempnum > tempdem):
            counter += 1
            tempnum = tempnum - tempdem
        if (tempnum == tempdem):
            counter += 1
        
        #after whole numbers are settled, this reduces the fraction
        tempnum /= factor
        tempdem /= factor

        #will print out the fraction and it's whole number if there is one
        if (counter == 0):
            return (fraction(tempnum,tempdem))
        else:
            return "%d %d/%d" % (counter, tempnum, tempdem)

if __name__ == '__main__':
    a = fraction(1,2)
    b = fraction(3,4)
    c = a + b
    print(c)
