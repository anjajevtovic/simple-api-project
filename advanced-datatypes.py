
#LISTS# => mutable - able to add/remove

#use with similar items with a need of
#adding and removing

#initialization
listInit = []

#adding to list
##1
list1 = ["bebe","claw","signature"]
list1.append("queenzy")

##2
###insert(pos, value)
list1.insert(1,"cally_bebe")

##3
list2 = ["shaka"]
list1.extend(list2)

#lookup in lists
list3 = []
list3.extend(list1)
list3.append("bebe")

print("bebe" in list3)
print(list3.index("bebe"))
print(list3.count("bebe"))
list3[len(list3)-1] = "kuku"
list3[-1] = "kookoo"

#removing from list
list3.remove("bebe")
list3.pop()
list3.pop(0)

#sorting
##sorted() returns a copy, sort() has no return
list4 = sorted(list3)
list4.sort(reverse=True)

#count and remove returns only the first
#found in list, duplicate values are not seen

#slicing list
list6 = ['h','e','l','l','o']
print(list6[0:3])
print(list6[1:])
print(list6[:3])
print(list6[2:-1])

#################################################
#################################################

#TUPLES# => immutable - items in it cannot be changed

#for contaioning snapshot of data
#security is heigher since nothing can be changed
#only immutables can be part of tuple

#initialization
tup = ()
tup1 = 100,99,101
type(tup1)

#WARNING: tup = (1) => not tuple => tup = (1,) yes tuple
student = ("Nikolina", 10, "programming", 9.5)

#tuple unpacking
name, index, subject, gpa = student
##if one of the values is not important _ can be used
name1, index1, subject1, _ = student

##this is returning tuple because of the commas
def http_status_code():
    return 200, "OK"

code, message = http_status_code()

#search in tuples
print("Nikolina" in student)
gpa2 = student.index(9.5)

#################################################
#################################################

#SETS# => mutable

#allowing storing other immutable tipes in unsorted way
#no duplicates are allowed => they are ignored
#fast membership testing
#can add or remove

#initialization
setInit = set()
setInit = {1, 67, 88}
print(setInit)

#check hash of the string
print(hash("BEBE"))
#!!!Lists are unhashable

#adding to set
setInit.add(9999)

#removing from set
setInit.remove(1)

##discard is not throwing an error if value is nonexistant
##remove is throwing an error in such a case
setInit.discard(67)

#updating sets
set1 = {1,2,3}
set2 = {"red","black","blue"}
set1.update(set2)
print(set1)
print(set2)

#set operations

rainbow_colors = {"red","orange","yellow","green","blue","violet"}
favourite_colors = {"pink","coral","yellow"}
##union of two sets 
print(rainbow_colors|favourite_colors)
##intersection
print(rainbow_colors&favourite_colors)
##differece
print(rainbow_colors^favourite_colors)
print(favourite_colors^rainbow_colors)

help(set.union)

#making copy of set data stored in list
#we do this when we need data sorted

list5 = list(rainbow_colors)
print(list5.sort())


#################################################
#################################################

#DICTIONARIES#

#mutable => add/remove
#dict values can be mutable
#but keys can only be immutable
#perfect for storing json
#fast search
#dict is sorted in inserted order but cannot search by index

#used when want to find something fast with the key

#initialization
dictInit = {}

dictInit = {1:"joo","two":"claw"}
print(dictInit[1])

#getting value from dict
##get is not throwing excplicit error whereas direct accessing is
print(dictInit.get("twoo"))
print(dictInit[1])

#returning default value if key is not present
print(dictInit.get("four","default value"))

#adding and removing from dict
dictInit["new key"] = "new value"
dictInit["two"] = "overwritten value"

#updating
colorss = {"r":"red","b":"blue"}
numberss = {1:"one",8:"eight"}
print(colorss.update(numberss))

vegetables = {"green":["Spinach"]}
vegetables["green"].append("Apple")
print(vegetables) 

#to get all the keys
vegetables.keys()

#to get all the values
vegetables.values()

#to get all the key-val pairs
vegetables.items() 
#this returns a list of tuples