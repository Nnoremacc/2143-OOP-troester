### Questions
**1)** What does Python print for each of the following:

```python 
johns_bag = Bag()
johns_bag.print_bag()
# what prints?

for color in [’blue’, ’red’, ’green’, ’red’]:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# what prints?

s = johns_bag.take_skittle()
print(s.color)
# what prints?

print(johns_bag.number_sold)
# what prints?

print(Bag.number_sold)
# what prints?

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
# what prints?

print(Bag.number_sold)
# what prints?

print(soumyas_bag.number_sold)
# what prints?
```

### Answer 1

```python
johns_bag = Bag()
johns_bag.print_bag()
# what prints?

# It prints out an empty list, of your "bag"

for color in [’blue’, ’red’, ’green’, ’red’]:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# what prints?

# prints out a list--['blue','green','red','red']

s = johns_bag.take_skittle()
print(s.color)
# what prints?

# Prints out blue

print(johns_bag.number_sold)
# what prints?

# Prints out 1

print(Bag.number_sold)
# what prints?

# Prints out 1

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
# what prints?

# Prints out a list--['red','green','red']
# Also prints out None, unsure why

print(Bag.number_sold)
# what prints?

# Priints out 2

print(soumyas_bag.number_sold)
# what prints?

# Prints out 2

```

**2)**  Write a new method for the Bag class called take color, which takes a color and
removes (and returns) a Skittle of that color from the bag. If there is no Skittle
of that color, then it returns `None`.

```python
def take_color(self, color):

```


### Answer 2

```python
def take_color(self, color):
    if color in self.Bag():
        return self.Bag().remove(color)
    else:
        return None

```

**3.** Write a new method for the Bag class called take all, which takes all the Skittles
in the current bag and prints the color of the each Skittle taken from the bag.

```python
def take_all(self):

```

### Answer 3

```python

def take_all(self):
    for x in range(len(self.Bag())):
        print(x.color)

```
