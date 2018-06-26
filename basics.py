#!/usr/bin/env python

#split string into substrings if it find a separator

str = "Hello, World"
str1 = "vallabh"
print(str.split(","))

#in and not in
print("vallabh" in str1) #returns true
print("vallabh" in str) #returns false

#lists

list = ["a","b","c"]
print(list) #prints complete list
print(list[1]) #prints first collection

list.append("d") #appends a collection to the list
print(list)


list1 = ["e","f","g"]
list.append(list1) #appends list1 with list
print(list)

names = ['vallabh','vijay','vishwa','vijay']
names1 = ['vishal','chandra','vamshi']
names.extend(names1) #extends with names
print(names)
count = names.count('vijay') #prints the count of vijay in list
print("the count of names list is", count)

index = names.index('vallabh') #displays the index of vallabh
print index

names.insert(2, "kala")
print("list names after inserting kala in 2 index",names)

names.pop(2)
print("list names after popping kala in 2 index",names)

names.reverse()
print("List names revered", names)

names.sort()
print("list names after sorting",names)


#tuples

tuple = ("apple","banana","mango")
print("tuple",tuple)
print("first tuple", tuple[0])
