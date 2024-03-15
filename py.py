#python comments-this a single line comment
"""
this is a simple multiline comment in python
"""
#variables

student_name="Jonathan"#data type is string
student_age=20 #data type is integer
student_fee=100.0#data type float
student_marks=100#data type is integer
is_male=True#data type is boolean
#outputting the values in the variables
print(student_name)
print(student_age)
print(student_fee)
print(student_marks)
print(is_male)

STUDENT_NAME="Jonathan"
student_name="Raph"
print(STUDENT_NAME)

x=y=z=10 #assigning one value to multiple variables
x,y,z=30,40,50#multiple values being assigned to multiple variables

#casting in python
a=1
b="1"
c=a+int(b)
print("the sum of a and b is:",c)

firstname="Jonathan"
secondname="121121"
thirdname=firstname+" "+str(secondname)
print("My third name is :",thirdname)
#logical operator
age=50
nationality="Kenyan"
if nationality=="Kenyan" and age>=35:
    print("you can be  president")
else:
    print("you cannot be president")
constituency="Embakasi,Westlands,Kasarani"
if constituency=="Embakasi"or"Kasarani"or"Westlands":
    print("you are Governor")
else:
    print("you are not Governor")
#trial for even number or odd
"""
x=101
y=2
ans=x%y
print("the answer")
if ans==0:
    print("Even number")
else:
    print("Odd number")
"""
#use of elif
"""
country=input("Enter the country:")
if country=="Rwanda":
    print("East Africa")
elif country=="Kenya":
    print("East Africa")
elif country=="Tanzania":
    print("East Africa")
elif country=="Uganda":
    print("East Africa")
elif country=="Congo":
    print("East Africa")
else:
    print("Unknown Country ")
"""


x=1
while x<=10:
    if x == 3 or x == 5:
        x+=1
        continue
    print("the number is :",x)
    x+=1
print("loop ended")


numbers=[1,3,5,7,9]
total=0
for num in numbers:
        total+=num
print("The sum of odd numbers from 1 to 10 is :",total)

i=0
sum=0
while i<=10:
    if i%2==1:
        sum=sum+i
    i=i+1
print("the total sum is :",sum)




