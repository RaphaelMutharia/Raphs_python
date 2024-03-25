"""
names=[]
num_names=int(input("How many namews do you want?"))
for i in range(num_names):
    name=input("Enter your name:")
    names.append(name)
for name in names:
    print(name)
"""


fruits=("apple","banana","mangoes")
print(fruits)
print(fruits[2])
myfruitslist=list(fruits)
print(myfruitslist)
myfruitslist[2]="pineapples"
print(myfruitslist)
fruits=tuple(myfruitslist)
print(fruits)



numbers=[1,2,3,4,5,6,7,8,9,1]
print("largest number is ",max(numbers))


mytuple =("apple", 'banana', 'mangoes')
print(mytuple)
raph = list(mytuple)
print(raph)
raph.append("berries")
print(raph)
mytuple=tuple(raph)
print(mytuple)


people={
    "firstname":"John",
    "lastname":"Doe",
    "email":"<EMAIL>"
}

print(people)
people.pop("email")
print(people)
if "John" in people.values():
    print("yes, 'John' is in the values")




list = ["dog", "cat"]
vegies = ["onions", "carrots"]
res = {list[i]: vegies[i] for i in range(len(list))}
print("The resultant dictionary is:"+ str(res))



myset={"audi", "BMW", "Benz"}
print(myset)
myset.add("mazda")
print(myset)
myset.discard("mazda")
print(myset)

#getting the repeated elements
my_list=["apple", "banana", "cherry", "apple", "apple"]
repeated_fruits = set()
non_repeated_fruits = set()
for i in my_list:
     if my_list.count(i)>1:
           repeated_fruits.add(i)
     else:
         non_repeated_fruits.add(i)
print("The repeated items are:", repeated_fruits)
print("the non-repeated items are:", non_repeated_fruits)

#dictionaries
mydict = {"brand": "toyota", "model": "harrier", "year": "2016"}
print("My old dictionary is:", mydict)
delete_keys = ["brand", "model"]
for key in delete_keys:
    del mydict[key]
print("My old dictionary is:", mydict)


number1=0
number2=20
try:
    x=number1/number2
    print(x)
except Exception as e:
    print("something went wrong:", e)
    print("program ended")
else:
    print(x)
    print("all is well")

