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
