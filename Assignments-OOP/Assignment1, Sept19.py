'''
Name: Cameron Troester
Email: cdtroester1022@my.mwsu.edu
Assignment: Homework 1 - List and Dictionaries
Due: 19 Sept @ 1:00 p.m.
'''

'''
Problem A 
1---it will print out values 1 and 3

2---It will print out a list of [1, 5, 4, 2, 6]

3---it will print out the value 5

4---It will print out True (a 4 exists in a)

5---It will print out a list containing the values
    [1, [5, 1], 4, 2, 3]
'''

# Problem B
x = [3, 1, 2, 1, 5, 1, 1, 7]

def remove_all(el, lst):
    #for loop to go through the whole list
    for n in lst:
        #if statement that looks for the element and deletes it
        if (el in lst):
            lst.remove(el)

remove_all(1, x)
print(x)

# Problem C 
p = [1, 2, 4, 2, 1]

def add_this_many(x, y, lst):
    for n in lst:
        #Going through the list, if the value X is in the list at
        #a given poisition, you add y to the list and continue through
        #the list, no need for a counter variable
        if x == lst.index(n):
            lst.append(y)

add_this_many(1, 5, p)
print(p)

# Problem D 
'''
1-- prints [3, 1, 4, 2]

2-- prints [3, 1, 4, 2, 5, 3]

3-- prints [1, 2, 3]

4-- prints [3, 1, 4, 2, 5, 3]

5-- prints []

6-- prints [1, 4, 2]

7-- prints [3, 5, 2, 4, 1, 3]
'''

# Problem E 
x = [3, 2, 4, 5, 1]

def reverse(lst):
    #the list starts at the beginning, goes to the end, and goes backwards
    lst = lst[::-1]
    print(lst)

reverse(x)

# Problem F 
x = [1, 2, 3, 4, 5]

def rotate(lst, k):
    return lst[-k:] + lst[:-k]

print(rotate(x, 3))


# Problem H 
'''
1-- Prints False

2-- prints 4

3-- prints false 

4-- prints out the whole Dictionary
    {('eli manning', 'giants'): 2, 'joe montana': 4, 'tom brady': 3, 'joe flacco': 0,
    'peyton manning: 1'}

5-- Prints out the whole list with the word cats in it now
    {('eli manning', 'giants'): 2, 'joe montana': 4, 'tom brady': 3, 'joe flacco': 0,
    'peyton manning: 1', 3: 'cat'}

6-- Prints out the whole list with a new key value for the set (eli manning, giants)
    {('eli manning', 'giants'): 5, 'joe montana': 4, 'tom brady': 3, 'joe flacco': 0,
    'peyton manning: 1', 3: 'cat'}

7-- Breaks the code cause you used [[]] instead of [()], bad syntax
'''

# Problem I 
d = {1: {2:3, 3:4}, 2:{4:4, 5:3}}

def replace_all(d, x, y):
    for key in d:
        #if the key value matches x, what you are looking for, then
        #set it the key value to y. then recall the function to keep Going
        #through the dictionary 
        if d[key] == x:
            d[key] = y
        elif type(d[key]) == dict: replace_all(d[key], x, y)

replace_all(d, 3, 1)
print(d)

# Problem J 
d = {1:2, 2:3, 3:2, 4:3}

def rm(d, x):
    #put them all in a list, then go through and search for the key value
    #x, if you find it, delete it. 
    items = [y for y in d if d[y] == x]
    for y in items:
        del d[y]

rm(d, 2)
print(d)
