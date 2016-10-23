# Ineritance

### Questions

***1.*** Implement the `Cat` class by inheriting from the `Pet` class. Make sure to use superclass
methods wherever possible. In addition, add a `lose_life` method to the `Cat` class.

```python
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
    
    
    
    
    def talk(self):
        """A cat says meow! when asked to talk."""
        
        
        
        
    def lose_life(self):
        """A cat can only lose a life if they have at least
        one life. When lives reach zero, the ’is_alive’
        variable becomes False.
        """
        
        
```

### Answer 1

```python
class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It’s alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print("...")
        
        
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
    	Pet.__init__(self, name, owner)
    	self.lives = lives
    	
    def talk(self):
    	print(self.name + " says meow!")
    
    def lose_life(self):
    	if (self.lives >= 1):
    		self.lives -= 1
    		print(self.name + " has lost a life and is now down to " + str(self.lives) + " lives left")
    	else:
    		Pet.is_alive = False
    		if (Pet.is_alive == False):
    			print(self.name + " has lost it's last life, and is now dead")
```

***2.*** Assume these commands are entered in order. What would Python output?

```python
class Foo(object):
    def __init__(self, a):
        self.a = a
    def garply(self):
        return self.baz(self.a)
        
class Bar(Foo):
    a = 1
    def baz(self, val):
        return val
        
f = Foo(4)
b = Bar(3)
print(f.a)
# prints what ?

print(b.a)
# prints what ?

print(f.garply())
# prints what ?

print(b.garply())
# prints what ?

b.a = 9
print(b.garply())
# prints what ?

f.baz = lambda val: val * val
print(f.garply())
# prints what ?
```
### Answer 2

```python
class Foo(object):
    def __init__(self, a):
        self.a = a
    def garply(self):
        return self.baz(self.a)
        
class Bar(Foo):
    a = 1
    def baz(self, val):
        return val
        
f = Foo(4)
b = Bar(3)
print(f.a)
# prints what ?

# Prints out the number 4

print(b.a)
# prints what ?

# Prints out the number 3

print(f.garply())
# prints what ?

#Errors from no attribute

print(b.garply())
# prints what ?

# Prints out the number 3

b.a = 9
print(b.garply())
# prints what ?

# Prints out the number 9

f.baz = lambda val: val * val
print(f.garply())
# prints what ?

# Prints out the number 16

```
