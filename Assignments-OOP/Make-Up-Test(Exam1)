# Cameron Troester

-----

## 1: Definitions: 

Using python comments, label all lines that an OOP definition could be applied to.

```python

class Employee:

   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


emp1 = Employee("Zara", 2000)

emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount

```
-----

## Answer 1

```python```
"""the class Employee plus the variable and methods are a form of encaplsulation""

""" Class """
class Employee:

	""" Class variable/ Data Member """
   empCount = 0

	""" Constructor """
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

	"""Method"""
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

	"""Method"""
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"""Instantiation"""
emp1 = Employee("Zara", 2000)

"""Instantiation"""
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount
```

-----

## 2: List Functions

Given the list below:

```python
States = ['Alabama','Illinois','Wyoming','New York', 'Vermont', 'New Hampshire', 'Maine', 'Texas']
```

**A)** Sort the list

**B)** Add 'Oklahoma' to the list in alphabetical order without sorting the list again. Actually, write a function that would add an item to the list in alphabetical order. Example:

----
## Answer 2:
## Part A

States = sorted(States)
print(States)

## Part B
```python```
States = ['Alabama','Illinois','Wyoming','New York', 'Vermont', 'New Hampshire', 'Maine', 'Texas']

States = sorted(States)

print(States)

#your wording was odd, I read it as adding any item to the list in the right location, so I let the user decide on the item

def addInOrder(L):
	item = input("Enter what you want to add to the list: ")
	for x in range(len(L)):
		if(L[x] > item):
			break
	L.insert(x, item)
		

addInOrder(States)
print(States)





## 3: Looping over Lists
(10 Points)

Using the following list as an example: `L = [10,20,30,40,50,60,70,80,90,100]` write a function that would divide each value by its index location + 1. Our example list would turn into: `L = [10,10,10,10,10,10,10,10,10,10]`. Remember NOT to get caught up on these values. Your function should work on any list.

Usage:
```python
L =  [10,20,30,40,50,60,70,80,90,100]
NList = addPrevious(L)
print(NList)
# prints: [10,10,10,10,10,10,10,10,10,10]
```

Your answer should consist of just the function definition and none of the usage I provided above.

## Answer 3

L = [14, 3, 43, 50, 55, 66, 74, 84, 99, 101]

def divIndex(L):
	L2 = []
	for x in range(len(L)):
		L2.append(L[x] / (x + 1))
	return L2
	
print(divIndex(L))

-----

## 4: Looping over Dictionaries
(10 Points)

Given the following dictionary: 
```python
months = { 1 : "January", 
     	2 : "February", 
    	3 : "March", 
        4 : "April", 
     	5 : "May", 
     	6 : "June", 
    	7 : "July",
        8 : "August",
     	9 : "September", 
    	10 : "October", 
        11 : "November",
    	12 : "December" }
```
Iterate over this dictionary, and create a new one that only uses the first three letters of the month. Also make the new months all lowercase. Your new dictionary should look like:

```
abbr_months = {1:"jan",
        2 :"feb",
        3 :"mar",
        4 : "apr", 
     	5 : "may", 
     	6 : "jun", 
    	7 : "jul",
        8 : "aug",
     	9 : "sep", 
    	10 : "oct", 
        11 : "nov",
        12 : "dec" }
```

To help you look up `string slicing` and `lower`. 

Your answer should include just the code that loops and creates the new dictionary.

## Answer 4

newMonths = {}

for key, value in months.items():
	newMonths[key] = value[:3].lower()
	
print(newMonths)
-----

## 5: Min and Max
(10 Points)

- Assume that pythons built in min , max , and sort functions are broken. Write a function that receives a list then traverses the list and returns the `min` , `max`, and `average` values in a tuple.

```python
def miniStats(L):
""" 
@Description: Finds the min,max,and average values in a list
@Params: L (list)
@Returns: tuple (int,int,double)
"""
	# Start with a copy of the list so we don’t modify the original.
	L = L[:]



```

When writing your answer, include the entire function definition (without the comment block).

-----
## Answer 5

def miniStats(L):
	sum = 0
	L2 = []
	L = L[:]
	
	
	L = sorted(L)
	L2.append(L[0])
	L2.append(L[-1])
	
	for x in L:
		sum += x
	
	L2.append(sum / len(L))
	return tuple(L2)
	
print(miniStats(Stuff))


## 6: Prime Class


Write a class called `myPrimes` that represents a collection of your prime numbers. 
- `addPrime` : 
    - receives a prime number and adds it to your collection of primes
    - it must be checked to make sure it's prime! (should be a private method that does this).
- `removePrime`:
    - a method will remove a prime from your list
- `printPrimes`:
    - this method will print your prime numbers out 
 


## Answer 6

class myPrimes(object):
	def __init__(self):
		self.L = [2, 3, 5, 7, 9, 11]
		""" 
		I did a repr and str method instead of printPrimes due to the fact that we are
		working with objects
		"""
	def __repr__(self):
		return (self.L)
		
	def __str__(self):
		return "Prime numbers: %s" % (self.L) 

	def __primeCheck(self):
		num = int(input("Enter in a positive prime number: "))
		if num > 1:
			for i in range(3, num):
				if (num % i) == 0:
					return self.__primeCheck()
				else:
					return num
			for i in range(2, num):
				if (num % i) == 0:
					return self.__primeCheck()
				else:
					return num
		else:
			self.__primeCheck()

	def addPrime(self):
		self.L.append(self.__primeCheck())
		self.L = sorted(self.L)
		
		again = input("Do you want to add more numbers? (y) or (n): ")
		if (again == 'y'):
			print("\nCurrent List: ")
			print(self.L)
			print()
			self.addPrime()
		
	def removePrime(self,L):
		item = int(input("What number do you want removed: "))
		if(item not in self.L):
			print(str(item) + " was not in the list")
			print("\nCurrent List: ")
			print(self.L)
			print()
		while(item in self.L):
			self.L.remove(item)
		
		again = input("Do you want to remove more numbers? (y) or (n): ")
		if(again == 'y'):
			print("\nCurrent List:")
			print(self.L)
			print()
			self.removePrime(L)
		

L2 = myPrimes()
L2.addPrime()
print(L2)
L2.removePrime(L2)
print(L2)
-----
