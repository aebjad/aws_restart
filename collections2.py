#### In Python, string and numeric data types are often used in groups called collections. 
###  Three such collections that Python supports are the list, the tuple, and the dictionary.

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#### Accessing a list by position
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

###### Changing the values in a list
myFruitList[2] = "orange"
print(myFruitList)

### The tuple is like a list, but it can't be changed. 
### A data type that can't be changed after it's created is said to be immutable. To define a tuple, you use parentheses instead of brackets ([]). 
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

### Trying: TypeError: 'tuple' object does not support item assignment
#myFinalAnswerTuple[2] = "orange"
#myFinalAnswerTuple[3] = "orange"
#print(myFinalAnswerTuple)

###  dictionary data type
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# Accessing a dictionary by name
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
# trying: got KeyError: 0
#int(myFavoriteFruitDictionary[0])
# trying: KeyError: 'banana'
#Sprint(myFavoriteFruitDictionary["banana"])
# trying
print(myFavoriteFruitDictionary)
myFavoriteFruitDictionary["Paulo"] = "orange"
print(myFavoriteFruitDictionary)
#trying:
myFavoriteFruitDictionary2 = {
  'Akua' : 'strawberry',
  "Saanvi" : 'pear',
  'Paulo' : 'mango'
}
print(myFavoriteFruitDictionary2)


####  Creating a mixed-type list
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#  for loop statement to traverse the list and print the data type for each item in the list:
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    

