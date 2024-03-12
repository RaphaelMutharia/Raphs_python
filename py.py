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