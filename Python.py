"""
                                                    What is Module?
When i do import pandas, whats happening here? Its simply a module which is being directed to our comp. A module is simply a code 
written by somebody else. 2 types- Built_in, These are already available in our comp. External, These modules are only used when
we install it using pip or conda.
"""

"""
                                                    Print In Python
print("Hello") - Python is analyzing it as a string thus using double quotes
print(5*4) - Can also do computataions, like this
print(5) - Or just simply print any number u want
"""

"""
                                    Escape Sequence And Comments And Some print parameters
--Escape Seq
print("Hiii\nHow are u?")#Here if i want to see how are u in next line, then use \n which is a escape sequence

--Comment
#This is a single line comment
As u know i am already using multi line cmmt

--Print Parameters
print("Hii", 7) #Here whwn we print then the space that comes b/w datatypes in python is simply a space. But if u want
                #To give another characters bo/w the spaces we can do so using separator parameter
print("Hii" ,7 , sep="~")

print("Hello" , end="Lund") #Here the use of end parameter is to, what to print after the end of this print func
print("Hii Ji")
"""

"""
                                                        Data Types
Variables are simply containers that are used to store data
Where as, data types are the types of values that can be stored in a variable

--Types of Data Types
1- Numeric
a= 7 #An int
b=1.1 #A float
c = complex(3 , 5) #A complex
print(type(a) , type(b ), type(c)) #Here i used the types func which will return the datatypes of these variables i.e. a,b,c

2- String
a = "I am a string"
print(type(a))

3- Boolean

4- Sequenced Data
|- List
list  = [1,2,4.4,"Hirak"] #A collection of different data types, separated by commas enclosed with square bracks
                          #Lists are mutable means it can be modified
print(list)
||- Tupple
tupple = (1,2.2, complex(5,4) , "Yoo") #Similar to list has different types, separated by commas, and enclosed with paranth
print(tupple)                          #Tuple are immutable and cant be modified unlike list

5- Mapped Data: Dictoinary
dict = {"Name" : "Hirak" , "Age" : 19 } #Dicts are simply maps like in c++, which stores key:value piars, Unordered and enclosed
print(type(dict))                       #Using curly bracks
"""

"""
                                                        Operators
1- Arithmetic
+ ADD
- SUB
* MUL
/ DIVISON print(5/3) #A float will come unlike c++ not an int
% MODULOS print(5%3) #A reminder will come
// FLOOR DIVISION print(5//3) #But with this the decimal part will be removed
"""

"""
                                                    TypeCasting
The ability to change the type of one datatype to another is known as typecasting

2 types
|- Explicit
Under this the developer changes the type by himself or herself
a = "1"
b ="2"
print(a+b) #As expected its taking as string and concating it
#But lets use typecasting
print(int(a)+int(b)) #Here its changed this is explicit casting
||- Implicit
Under this the compiler does casting by itself
a =9.9
b =4
print(a+b) #Here it changed the b which was an int to float, It is done so that no data is lost
            #As if it converted the float to int the result would have been 13 so .9 data would have been lost
"""

"""
                                                    Taking User Input
In order to take input from user we use input() func
a = input("Enter the num: ")
print("The number is", a)

If during the input u want to tell the compiler that this input will be considered as int then,
a  = int(input("Enter the num: "))
print(a)

#Important
#Every input that u take will be considerd as an str 
print("The number is", type(a)) #Class<str> will be printed

#Now,
a = input("Enter the first num: ") #3
b = input("Enter the second num: ") #2
print(a+b) #As we know every input will be considered as an string there it will concatenate and result will be 32

#To change this we use typecasting
print(int(a)+int(b)) #Therfore 5 will be printed out
"""

"""
                                                    More About Strings
Strings are immutable means that cannot be modified
name = "Hirak"
name[2] = "B"
print(name)
Will thorw an error

name = "Hirak"
name1 = name[0:2] + "B" +name[3:]
print(name1)
Thus we have to create a new str

name ="Hirak" #Simply we know collection of chars, we can aslo use the single quotes

--Double quotes inside the single quotes
#But suppose when we want to use double quotes inside a double quote like
#"Hi how are u "I am fine"" #This will throw an error, Therefore we use single quotes then use doub le quotes inside it. 
name = 'Hii, "How are u?"' #Here it will work

--Multiline strings
name = Therefore --Unable to use this as inside the comment
use the
multiline strings #This will print all chars including the spaces
print(name)
"""

"""
                                                    String Slicing
Note- Always remember, under slicing in strings or lists or any datatype the end element is not included [0:3] - will print 0,1,2 

--Length Func
name = "Hirak"
print(len(name)) 

--String Slicing
name = "Hirak"
print(name[0:5]) #Whats happening is that its taking index from 0 and printing till 4 just like an array in c++ n-1;
print(name[:5]) #If no zero directlt assume start from 0
print(name[0:]) #If no at end point then it will be replaced by len(name) which is 5
print(name[0:len(name)]) #This is equal to the above one, this is being done by compiler behind our backs
print(name[0:-3]) #Here whats happening is that to calculate the end point its being replaced by len of name then subtr -3
print(name[0:len(name)-3]) #This is equal to above, this is being done by compiler behind our backs
"""

"""
                                                    String Methods
Important-- No actual changes are being made in the main string. A copy is being created. In python strings are immutable
1-lower Chnages the chars to lower case
name ="Hirak"
print(name.lower())

2-Upper Changes the chars to upper case
print(name.upper())

3-Replace Replaces the desired given string with the new given string
name = "Hirak"
print(name.replace("Hirak" , "Bala"))

4-Capitalize Changes the first letter of the sentence to capital 
name = "hirak bala"
print(name.capitalize())

5-Title Changes the letter of each word in a given sentence to capital
name = "hirak bala"
print(name.title())

6-Strip Remove trailing and leading whitespaces from a sentence
name = "   hirak hu    "
print(name.strip())

7-Find Returns the index where a word starts, if not found returns -1
name = "Hirak Bala"
print(name.find("y"))

8-Count Returns the  umber of times a char occurs in a string, if not found 0
name = "Hirak"
print(name.count("a"))

9-Swapcase Replces lower to upper and vice versa
n = "Www hackKKeraNk.cOm"
new_str = n.swapcase()
print(new_str)
"""

"""
                                                         If else
Simply like in c++, but remeber the identation and the semi colon
a = int(input("Enter your age: "))
if(a>=18):
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
"""

"""
                                                    Match Case Statement
In C++ only char and int,float,double can be taken in expression in switch case
int x;
    cin >> x;
    switch (x)
    {
    case 1:
        cout << "This is One";
        break;
    case 2:
        cout << "This Is Two";
        break;
    default:
        cout << "By Default";
        break;
    }

Difference b/w switch in c++ and match in python
x = int(input("Enter the num: "))

match x:                                                        
    case 1:
        print("One")
    case 2:
        print("This is Two")
    case _:
        print("By Default")
"""

"""
                                                        For Loop
While loops are used when a segment of code needs to execute repeatedly while a condition is true

For loops iterate over a sequence of elements, executing the body of the loop for each element in the sequence

Just like in c++ a loop will run till end-1

# For a list, similarly with tuples and dicts
list = ["Hirak" , "Kunal" , "Akhilesh"]
for i in list:
    print(i)

# For a string 
name = "Hirak"
for i in name:
    print(i , end= ",")

# For printing nums, use range
for i in range(5):
    print(i , end =",")

# Now, a for loop takes three parameters
# 1- Start 2- End 3- StepIn
for i in range(2, 5): #Similar to above loop just i have added the start, otherwirse the compiler will assume to start from 0
    print(i)

for i in range(0,5,2): # By adding the stepin its adding the value of it or jumping till end>start
    print(i)
"""

"""
                                                        While Loop
Some logic based while loop
a = 0
while a != 5:
    a = int(input("Enter the num: "))
    if a != 5:
        print("Not Equal")
    else:
        print("Its equal")

Simple Incrementing
a = 0
while(a<4):
    print(a)
    a = a+1

Simple Decrementing
a = 7
while(a !=0 ):
    print(a)
    a = a-1
"""

"""
                                                    Break And Continue
Similar to c++,
Break- Exit the loop
Continue- Skip that iteration 

for i in range(0 , 4):
     if(i==2):
        break #Once it touches 2 break out of the loop
     
     print(i)
   
for i in range (0,4):
    if(i==2):
        continue #Once it touches 2 skip that print means iteration
    print(i)

i =0 
while(i<5):
    if(i==3):
     break
    print(i)
    i = i+1

i = 0
while(i<7):
   if(i==4):
       i = i+1
       continue
   print(i)
   i = i+1
"""

"""
                                                        Functions
Just like in c++,
instead of writing int,float or void in return type we use def, then func name and parameters then semi colon

def clac (a , b):
    if(a>b):
        print(a)
    else:
        print(b)

      
clac(7,6)

# Check wheether a num is prime or not
def prime(a):
    if(a<=1):
        return False
    for i in range(2, a):
        if(a%i == 0):
            return False
            break

    return True

# Check Odd Even
a = int(input("Enter the num u want to find: "))
if(a%2==0):
    print("Even")
else:
    print("Odd")

# Check sum
a = int(input("Enter the num u want to find the fact of: "))
fact = 0
for i  in range(1 ,a+1):
    fact += i

print(fact)



"""

"""
                                                    Function Arguments
4 Types
1- Default Args
# Here b is a default args, same like in c++, i can also pass the value of b, if not given then use default else passed use that
def avg(a , b = 9):
    return (a+b)/2

print(avg(9 ))

2- Keyword Args
print(avg(3,4)) #Here a =3, b = 4
print(avg( b =4, a = 5)) #But here, b =4 , a = 5 We can change the order by assining args to their respective values

3- Required Args
def avg(a , b):
    return a+b


print(avg(4,5)) #This means we have to pass the parameters into the func as per the args mentioned in it

4- Variable length args
def avg(*nums): #Taking as a tuple after using one *
    print(type(nums))
    sum =0
    for i in nums:
        sum += i

    return sum/2


print(avg(4,3,2,3))

def avgg(**nums): #Taking as a dict after using two **
    print(type(nums))
    sum =0
    for i in nums:
        sum += i

    return sum/2

# Will throw an error as dict is a key value pairs, will understand later
print(avgg(4,3,2,3))
"""

"""
   
                                                        Lists          
Lists are ordered items that stores multiple datatypes separted byb commas and inside []   

Note- Always remember, under slicing in strings or lists or any datatype the end element is not included [0:3] - will print 0,1,2 

1- Slicing
As we have already seen in strings we can also perform slicing in lists also
list = [1,2,3,"Hirak" , True]
print(type(list))
print(list[:]) #Python will convert list[0:len(list)]
print(list[0:]) #Again same as above

2- Negative Indexing
When finding the index during -ve indexing first calculate the len of item then substract, or at end of list -ve index will be -1
list = [1,2,3,"Hirak" , True]
print(type(list))
print(list[-2:-1]) #Python will list[len(list)-2 : len(list)-1]

3- Finding
We can find any elemnt which is present in the list or not
list = [1,2,3,"Hirak" , True]

if "Hirak" in list:
    print("Yes")
else:
    print("No")

4- Jump to
list = [1,2,3,4,5,6,69]
print(list[0:len(list) : 2]) #Start 0, end len(list) , jump to by 2 just like in for loop i+=2 in c++

5- List Comprehension
lst = [i for i in range(4)] #Jo bhee value for i in range (4) yani 0,1,2,3 isko hamare phele i me dalo phir list m
print(lst)

# Can also apply conditions
lst2  = [i *i for i in range(10) if i%2==0] #Take even nums
print(lst2)
"""

"""
                                                    List Methods 
list = [1,2,5,4,3,6]

# Sorts the list
list.sort()
print(list)

# Reverses the list
list.reverse()
print(list)

# Sorts the list in reverse order
list.sort(reverse=True)
print(list)

# Adds an item at the end of list
list.append(8)
print(list)

# Remove an element
list.remove(5)
print(list)

# Copy the list item to new list m
m = list.copy()
print(m)

# Concatenate the m and list and add it to new list ll 
ll = m+list
print(ll)

# Return a number which will tell count of a particular item
print(list.count(4))

# Insert an elemnt at index 4 which is 6
list.insert(4,6)
print(list)

# Returns a num which tells at which index an element is present
print(list.index(4))     
"""

"""
                                                        Tuples
Tuples are simply non changeble but have similar characteristics to list, once declred we cannot change the items in tuple

list = [1,2,3]
list[0] = 4
print(list)
#Can be changed but,

tup = (1,2,3)
tup(0) = 22 #Will throw an error

# If tup has one element it will be considered as an int
tup = (1)
print(type(tup)) #To solve this, use ,
tup = (1,)
print(type(tup))
"""

"""
                                                    Tuples Methods
We cannot changes anything in tuples, if u want to do so, convert tuple in list then apply changes in that list,
then again convert that list into tuple.

However there are some methods
tup = (1,4,3,2)
print(len(tup))
print(tup.count(4))
print(tup.index(3))
"""

# KBC
# list = ["Which is smallest capital of india" , "Longest River" , "Largest State In India" , "Who built Taj Mahal"]
# list2 = ["Goa" , "Nile" , "Rajasthan" , "Akbar"]

# cont = 0
# for i in range(len(list)):
#     print(list[i])
#     a = str(input("Enter the answer: "))
#     if(a == list2[i]):
#         print("Correct answer")
#         cont = cont+50
#         print("U won: " ,cont)
#     else:
#         print("Wrong answer")
#         print("U won only: " ,cont)
#         break

"""
                                                        Fstrings
F strings are used for formatting purposes. If u want to place a large string inside a string we use fstring
name = "dprijvejviodsjb dnhfiob "
country = "snvjsnkjnsfjkvngfgbdf fc"
print(f"My {name} is and i am from {country}") #Use an f which tells compiler that its fstring then use curly braces
# If u want to see the {name} and {country} as an output use double {{}}
print(f"My {{name}} is and i am from {{country}}")
"""

""" 
                                                        Docstrings
These are special strings that are used after the func defination and classes so that we may look at it if there's anything imp
def squar(n):
    '''This is a docstring''' Its only after used func defination or class if not will not be docstrings
    print(n**2)

squar(5)
print(squar.__doc__) This will print our docstrings
"""

"""
                                                        Recursion
def fibo(n):
    if(n==0):
        return 0 
    if(n==1):
        return 1
    return n *fibo(n-1)

print(fibo(3))
"""

"""
                                                        Sets
Sets are unordered collection of items that does not include repeted items in the output , cant do indexing

# list = [1,1,2,3,"True" ,False ]
# tup = (1,1,2,3,"Hirak" , True)

# for item in list:
#     print(item , end=",") #Here this will include 1,1 two items, and will come in same order

# for item2 in tup:
#     print(item2 , end=",") #Same here

# But in sets no repeted items in output and the items may come in any order
sets = {1,1,"Hirak",True , 2,2,3,4}
for i in sets:
    print(i)  #Here it will output 1,Hirak,2,3,4 in any order. Note, true = 1, 
    therefore 1 will be printed only 1 time as no repe

h ={}  #As dict also uses {} , there output will be dict
print(type(h))
# To make a set then,
h= set()
print(type(h))
"""

"""
                                                        Sets Methods
# Union
#Takes union means all items without repetitions
set = {1,2,3,1,1,"Hirak",7}
set2 = {1,2,5,3,2,"Bala"}
print(set.union(set2))

# Intersection
print(set.intersection(set2))

# Difference
#Simply means the items present in set2 are present in set or not. If the items are present then give the un-present ones
#A-B
print(set.difference(set2))

# Add
set.add("yoo")
print(set)

# Update
#If u want to add more than one items
ll = {7,8,9}
set.update(ll)
print(set)

# Remove/Discrad
set.remove(4) #If elemnt not present that we want to delete then remove will throw an error
print(set) 
set.discard(4) #But discrad will not throw an error
print(set) 

# pop/clear/del 
"""

"""
                                                            Dicts
Dicts are simply like map in c++, storing key value pairs and are ordered
dict = {"Hirak" : "Human" , "Cllg": "MERI" , "Roll_no" : 54}

print(dict)

print(dict.keys()) #Will print keys

print(dict.values()) #Will print values

print(dict.items()) #Will print respective key:values pair

print(dict["Cllg"]) #Can also do using indexing

for keys in dict.keys(): #To print the keys using loop
    print(keys)

for values in dict.values(): #To print the values using loop
    print(values)

for key , values in dict.items(): #To print the key:values using loop use fstring
    print(f"{key} : {values}")
"""

"""
                                                        Dict Methods
# Update
# This adds the key and value pair in the dict
dict = {"Hirak" : "Human" , "Age" : 19}
dict.update({"Sex" : "Male"})
for key , value in dict.items():
    print(key , value)

# Clear
# Clears the entire dict
dict = {"Loda" : "Lund", "Lassan" : "Bhencho"}
dict.clear()
print(dict)

# Pop 
# Delets the key value pair by passing the key value
dict= {"Hanji" :"Sex Chaiye" , "Lunde" : "Hanji Dedo"}
dict.pop("Hanji")
print(dict)

# PopItem
# Delte the last item in the list
dict= {"Hanji" :"Sex Chaiye" , "Lunde" : "Hanji Dedo"}
dict.popitem()
print(dict)

# Del
# Will delete the whole dict existence including its variable name if parameter not given
dict= {"Hanji" :"Sex Chaiye" , "Lunde" : "Hanji Dedo"}
del dict
"""

"""
                                                Else Block With For and While
We can use the else block with the for and while loop also
for i in range(5):
    print(i)
    if(i ==3):
        break
else:
    print("Loop ended now")
print("Else will not run as we encountered a break, But no break then will execute the else")

i = 0
while(i<4):
    print(i)
    i +=1
else:
    print("Loop Ended")
"""

"""
                                                    Exception Handling
a = input("Enter the num: ")

try:
    num = int(a)
    print(f"The multiplication table of {num} is:")
    for i in range(1, 11):
        print(f"{i} x {num} = {i * num}")
except ValueError: #The valueError that I have used is called as exception classes,
                   #Python has many other exception classes which i will learn later 
    print("Invalid Input: Please enter a valid integer")
"""

"""
                                                        Finally Keyword
The thing is a finally keyword is always excuted whether the try and except block runs or not. So why not use print rather than 
finally keyword.

try:
    list = [1,2,3,4]
    a= int(input("Enter the index"))
    print(list[a])
except:
    print("Value Error")
# finally:
print("I am always executed") #Its also executing nicely whether try and except runs or not

Here comes the difference,
If i use print inside a func after using the return statement then it will not be executed
But incase, of finally keyword it will always run

def check():
    try:
        list = [1,2,3,4]
        a= int(input("Enter the index"))
        print(list[a])
    except:
        print("Value Error")
        return 1 #The print statement will not run as we have a return statement.
    # finally: #But if i include the finally keyword it will always run
print("I am always executed") 
        
check()
"""

"""
                                                    Raising Custom Errors
We use exception handling when we dont want to interrupt the flow and want the program to continue.
But, in raise case we use the raise keyword to make the program raise an error amd make it stop at that time
a = input("Enter the string:")
if(a == "quit"):
    print(a)
else:
    raise ValueError ("No match") 
"""

# Using both custom errors and error handling and making a calculator
# a = int(input("Enter the number one:"))
# b = int(input("Enter the number two:"))
# c = input("Enter the operator:")
# if((a >=0 and a<=100) and (b>=0 and b<=100)):
#     try:
#         match c:
#             case "+":
#                 print("Then addition is:",a+b)
#             case "-":
#                 print("Then substraction is",a-b)
#             case "/":
#                 print("Then division is",a/b)
#             case "*":
#                 print("Then multiplication is",a*b)
#             case _:
#                 print("Please enter a valid operator (+, -, /, *)")
#     except ZeroDivisionError:
#         print("Division by zero is not allowed")

#     finally:
#         print("Now, the code has ended successfully")
# else:
#     raise ValueError ("Please enter the correct value b/w 0 to 100")

# Excersie on code and decode
# print("Lets start the coding")
# a = input("Enter the code: ")
# if(len(a)>3):
#     b = a[1:] + a[0]
#     c = input("Add any three random chars: ")
#     d = input("Add any three random chars: ")
#     if((len(c)==3) and (len(c)==3)):
#         b = c[0:]+ a[1:] + a[0]   + d[0:]
    
#     else:
#         raise ValueError ("Enter chars == 3")
#     print(b)
# else:
#     b = a[::-1]
#     print(b)

# print("Coding ended!\n\n")
# print("Lets start the decoding")

# if(len(b)<3):
#     print(b)
# else:
#     b  = b[3:]
#     b = b[0:-3]
#     b= b[-1] + b[0:-1]
#     print(b)

"""
                                                    Short Hand If-Else
print if-condition else print
Mostly used when conditions are short 
a = 77
b = 788
print(a) if a>b else print(b) 
"""

"""
                                                    Virtual Environment
A virtual env is a separate env in a file through which we can download and run different version of pacakages such as mumpy, pandas etc.
We use a virtual env when suppose my frnd has 1.3 version of pandas and in my local computer on VS code I have 1.5. So, to use
that I can use the concept of virtual env and download my own version of different packages.

To create-
python -m venv hirak_venv

To activate-
hirak_venv\scripts\activate\bat

To deactivate
deactivate

Now suppose u want to send all the versions that u have used to a frnd. Then u wont write down the versions in paper right?
Thats when we use requirements.txt. It contains all the info about our packages

To create-
pip freeze > requirements.txt

To load those packs ur frnd can run this command and all the required packages will be installed in his venv
pip install -r requirements.txt
"""

"""
                                                        Importing                                                         
Importing is a technique through which you can load code from different files into your own scripts or files
import numpy
import numpy as nu
import numpy * This will load every funcs that are available in the numpy. However not recommended.
from numpy import read.csv  This will load a particular func from this module
print(dir(numpy)) This will show us all the func and methods that are available inside this module
"""

"""
                                                        Local VS Global
x = 4 #Its a global Variable
def printt():
    y = 6 #Its a local Varaiable, If i print outside the func will throw an error
    print(y)
    #x=88 This will not change our global variable
    global x
    x=88 #This will change
    print(x) #Now, what I want to change the global one then use global key

print(x)
print("Inside the func")
printt()
"""

"""
                                                        File Handling

Takes file name then 2nd mode

1- Opening a File
fi = open("File.txt" , "r")
text = fi.read()
print(text)
fi.close()

2- Writing into file
# If i run this the write func will override everything that i had in the file, Therfore use append
# file = open("File.txt" , "w")
# file.write("KJHKJJKJKOJJJKJNKJNHJ")
# file.close()

file = open("File.txt" , "a")
file.write("KJHKJJKJKOJJJKJNKJNHJ")
file.close()

                                                        Readlines
file = open("File.txt" , "r")
while True:
    line = file.readlines()
    if not line:
        break
    print(line)
"""

"""
                                                    Lambda Functions
A func which does not have any name rather anomynous
name = lambda : (expression) , Mostly used when dealing with small func
def mul(x):
    return x*x
print(mul(5))


x = 8
mul = lambda: ( x * x)
print(mul())
"""

"""
                                                    Map, Filter, Reduce                                                    
# Map
This simply applies a func to the whole iterable object
Takes two args 1st func 2nd iterable obj
l = [1,2,3,4,5]
ll = 0
for i in l:
    ll += i

print(ll)

Now, lets use maps
l = [1,2,3,4,5]
def sq(x):
    return x*x

Have to convert to list or the type of iterable obj
l = list(map(sq , l))
print(l) 

Or u can also do this using lambda
l = list(map(lambda x:x*x , l))
print(l)

# Filter
This filter our any obj that we pass. Returns true if it satisfies otherwise false
ll = [1,2,3,4,5]
def even(x):
    return x%2==0

ll = list(filter(even , ll)) #Using list as I have list as an iterable obj and i want to retuen that
print(ll)
Or can also use lambda
ll = list(filter(lambda x: x%2==0 , ll))
print(ll)

# Reduce
Under this it basically does computations on pairs means will only be used when using 2 or more args 
from functools import reduce

li = [22, 33, 44, 1, 2, 4]
result = reduce(lambda x, y: x + y, li)
print(result)

# Didnt use the list keyword to convert as its returning a result so if i use then it would be converted as an list
"""

"""
                                                        Is and ==
Is directly checks the the value at the memory location, but == checks the value
def check(x,y):
    if x==y:
        return True
    else:
        return False

print(check(4,2))

def check(x,y):
    if x is y:
        return True
    else:
        return False

print(check(4,4))
"""

# Snake Water Gun
# print("----------Let's start the game-----------")
# count = 0
# print("Starting for three rounds")

# while count <= 2:
#     Me = int(input("Choose any number between 1 and 3 (1: Snake, 2: Water, 3: Gun): "))
#     print("Your opponent has also chosen their number.")

#     # Generate opponent's choice (randomly)
#     import random
#     Opponent = random.randint(1, 3)

#     if Me == 1 and Opponent == 2:
#         print("You win! Snake beats Water.")
#     elif Me == 2 and Opponent == 3:
#         print("You win! Water beats Gun.")
#     elif Me == 3 and Opponent == 1:
#         print("You Win! Gun beats Snake.")
#     elif Me == 2 and Opponent == 1:
#         print("Opponent wins! Snake beats Water.")
#     elif Me == 3 and Opponent == 2:
#         print("Opponent wins! Water beats Gun.")
#     elif Me == 1 and Opponent == 3:
#         print("Opponent Wins! Gun beats Snake.")
#     else:
#         print("It's a draw!")

#     count += 1



# Min and Max In An List
# max = 9999
# min =-9999
# listt = [1,2,3,4,5,6,7,8]
# sum =0
# for i in range(0,len(listt) ):
#     if(max>listt[i]):
#         max = listt[i]
#     elif(min<listt[i]):
#         min = listt[i]

# print(max)
# print(min)


# Linear Search
# def searching(listt , key):
#     answer = False
#     for i  in range(0 , len(listt)):
#         if(key == listt[i]):
#             answer = True
#             break
#         else:
#             answer= False

#     return answer

# listt = [1,2,3,4,55,6,7,]
# if(searching(listt , 0)):
#     print("Present")
# else:
#     print("Not Present")


# Duplicates Elements
# ll = [1,1,3,3,5,5]
# result = []
# for i in range(0 , len(ll) ):
#     if(ll.count(i)>1):
#         result.append(ll[i])
# print(result)


# Unique Elements
# ll = [1, 1, 3, 3, 5, 7]
# result = []
# for item in ll:
#     if ll.count(item) == 1:
#         result.append(item)
# print(result)


# Binary Search
# ll = [1, 2, 3, 4, 5, 6, 7]

# def binary(list, key):
#     s = 0
#     e = len(list) - 1
#     while e >= s:
#         mid = (s + e) // 2
#         if list[mid] == key:
#             return mid
#         elif list[mid] > key:
#             e = mid - 1
#         else:
#             s = mid + 1
#     return None  # Key not found
# result = binary(ll, 7)
# print(result)


# First and last Poisition
# ll = [1, 1, 1, 4, 5, 7, 7]

# def binary(list, key):
#     ans  = 0
#     s = 0
#     e = len(list) - 1
#     while e >= s:
#         mid = (s + e) // 2
#         if list[mid] == key:
#             ans    = mid
#             e = mid-1
#         elif list[mid] > key:
#             e = mid - 1
#         else:
#             s = mid + 1
#     return ans


# def binary1(list, key):
#     ans  = 0
#     s = 0
#     e = len(list) - 1
#     while e >= s:
#         mid = (s + e) // 2
#         if list[mid] == key:
#             ans    = mid
#             s = mid+1
#         elif list[mid] > key:
#             e = mid - 1
#         else:
#             s = mid + 1
#     return ans
# result = binary(ll, 7)
# print(result)
# result = binary1(ll , 1)
# print(result)


"""
                                                Object Oriented Programming
"""

"""
                                                    Classes And Objects
class details:
    name = "Hirak"
    age = 19
    # Here self must be used inside the func so that we can use variables and also is used to pass object as a reference
    def show(self):
        print(f"Your name is {self.name} and age is {self.age}" )

# Different than c++, details obj
obj = details()
obj.show()
"""

"""
                                                    Constructor
If u want to use the constructor we use the __init__ along with a func
A class with constructor in python is also known as abstract class

class details:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"Your name is {self.name} and age is {self.age}" )

# Different than c++, details obj
obj = details("Hirak"  , 19 ) #Here as we know the constructor is taking 3 args here, but if i run it says taking 4 args
                                  #As, the obj is also being passed as a arg to __init__ as I have used the self keyword
obj.show()
"""

"""
                                                    Decorators
A decorator is simply adding addititionl features to the other func without touching that func
It order to create a decorator we create a func and again a func inside that func

A func that swaps if deno>nume

The number of para that our func takes will also be the same as the inner

def outer(func):
    def inner(a  , k):
        if(a<k):
            a,k = k,a
        return func(a , k)

    return inner


@outer
def div(a , b):
    return a/b


print(div(2,4)) 

    
"""

"""
                                                    Getters And Setters
The getter and setters are used with property and setter decorators
And a setter will only take one parameter besides self
We use _name or _age to tell others that these attributes are intended for internal use within the class
Mostly for getters and setters
Can have one setter for only one property

class details:
    def __init__(self , name , age):
        self._name = name
        self._age = age

    @property
    def get_set(self):
        return f"{self._name} {self._age}"
    
    @get_set.setter
    def get_set(self , value):
        if isinstance(value , str):
            self._name = value
        elif isinstance(value ,int):
            self._age = value


obj = details("Hirak Huu" , 19)
print(obj.get_set)

# obj.get_set = "Suraj"
obj.get_set = 88
print(obj.get_set)
"""

"""
                                                            Inheritance                                     
class rec:
    
    def calculate(len , bre , hei):
        return len*bre*hei
    

class are(rec):
    def calculat(pi , r):
        return(pi*r)
    

obj = are
print(obj.calculate(3.2,44,76))
print(obj.calculat(3.2,76))
"""

"""
                                                        Access Modifiers
In Python there's no such thing as public, private, protected but we use some underscores to tell people as a convention,
that we want to use it like that way
class lund:
    # This is public
    name = "Hirak"
    age = 19
    # This is protected, when we use single _, we tell others
    _course = "BCA" 
    # This is private, when we use double __,
    __clg = "MERI"
    # This will create mangling, when we use two __, to access it we use obj._classname__variablename


obj = lund()
print(obj.name)
print(obj.age)
print(obj._course)
print(obj.__clg) #To accesss use obj._lund__clg
"""

# Libraray Management System
# class library:
#     def __init__(self) :    
#         self.listt = []
#         self.no_of_books =0

#     def add(self , book):
#             self.listt.append(book)
#             self.no_of_books = len(self.listt)
#     def printt(self):
#         return f"The books are {self.listt} and the number of books are {self.no_of_books}"

# obj = library()
# obj.add(1)
# obj.add(3)
# obj.add(2)
# print(obj.printt())


"""
                                                        Static Methods
A static method is simply belongs to class rather an object and dont need to pass self as an args.
So, if someone says can create methods without self, Yes we can useing static methods

class pos:
    def __init__(self  , name , position):
        self.name = name
        self.position  = position

    @property
    def get(self):
        print(f"{self.name} = {self.position}")

    @staticmethod
    def show(): #Didnt pass any self
        print("Hello")

obj = pos("Hirak" , "Data Scientist")
obj.get
pos.show() #Here i can call it using class name or also obj name 
"""

"""
                                                Instance Vari VS Class Vari
An instance variable are those that gets defined under the constructor and are a propoerty of the instance.

A class vari are defined just after class defination and are the property of the class.
We use the class name to use the class variable. 
Suppose company name its a class variable but emp names should be instance variable

class employee:
    emp_count = 0 #Class Vari

    def __init__(self ,  Name , age):
        self.name = Name #These are instance Variable
        self.age = age
        employee.emp_count += 1

        
emp = employee("Hirak" , 19)
emp2 = employee("Ak" , 12)
print(employee.emp_count) #Here the number of emp should be a class as we wnt to use this throughtout the class
"""

"""
                                                        Class Methods
If u want to change the class variables then use the class methods

class details:

    # Class Variable
    Purpose = "Data Analyst"
    # Constructor
    def __init__(self , name , age):
        self.name = name  #Instance Variable
        self.age =age

    # Simple func
    # def show(self):
    #     print(f"{self.name} {self.age}")

    # Property
    @property
    def show1(self):
        print(f"{self.name} {self.age}")
    
    # Setters
    @show1.setter
    def show1(self , value):
        if(isinstance(value , str)):
            self.name = value
        elif(isinstance(value , int)):
            self.age = value

    # Static Method
    @staticmethod
    def show():
        print("This is an static method")

    #Class Method used to change the class varibles 
    @classmethod
    def change_purpose(cls , new):
        cls.Purpose = new

obj = details("Hirak" , 19)
print(details.Purpose)
print(obj.show1)
obj.show1 = "Hirak Bala"
obj.show1  = 19
print(obj.show1)
details.change_purpose("Data Scientist") 
print(details.Purpose)
"""

"""
                                                    Dir() , dict , help() Method
1- Dir
It will give us every attritbute and methods related to a variable or any data types
a = [1,2,4]
print(dir(a))

2- Dict
It will convert every variables i.e instance variables under __init__to a dictionary
class details:
    def __init__(self , name , age):
            self.name = name
            self.age = age

obj  = details("Hirak" , 19)
a = obj.__dict__
print(a)

3- Help
It will give us details about attritbute and methods related to a variable or any data types
a = 4
print(help(a))
"""

"""
                                                     Super Keyword                              
A super keyword is used when we want to access the methods and constructors of parent into a child

class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def p_show(self):
        print("This is a parent class")

class purpose(person):
    def __init__(self, name, age , purpose): #Here i am taking name and age variables from parent, then creating a new variables
                                             #and assigning it. This fullfills the DRY principle
        super().__init__(name, age)
        self.role = purpose

    def show(self):
        print(f"{self.name} {self.age} {self.role}")

    def c_show(self):
        print("This is a child class")
        super().p_show() #After the print func runs, the parent func will run then
        
    
obj = purpose("Hirak" , 19, "Data Scientist")
obj.show()
obj.c_show()
"""

"""
                                                    Method Overriding
It is a simple technique where we create a func in child class of same name and parameters and thus we override the 
which resides in the parent class. 
Remember that name and param of func should be same in child then only we can say its method overriding

class a:
    def show():
        print("This is class a")

class b(a):
    # pass If no func then parent's class method will run
    def show():
        print("This is class b") #Here this will run as i have override the above func


obj = b
obj.show()
"""

# This should work but some unicode problems
# from pypdf import PdfMerger

# new_pdf = PdfMerger()

# old_pdf = ["C:\Users\HP\Downloads\sql_basic certificate.pdf" , "C:\Users\HP\Downloads\Get_started_to_become_a_Student_Ambassdor.pdf"]

# for i in old_pdf:
#     new_pdf.append(i)

# new_pdf.write("Written")
# new_pdf.close()

"""
                                                    Single Inheritance
class animal():
    def __init__(self , name , species):
        self.name = name
        self.species = species

    def sound(self):
        print("I will make sound of an animal")

class cat(animal):
    def __init__(self, name, breed, species="Cat" ):
        super().__init__(name,species)
        self.breed = breed

    def sound(self):
        print("I will make sound of an",self.species)

obj =cat("Neko","Longtails")
obj.sound()

obj2 = animal("Doggy" , "Dog")
obj2.sound()
"""

"""
                                                    Multiple Inheritance
class employee:
    def __init__(self , name):
        self.name = name

    def show(self):
        print(f"{self.name}")

class dancer:
    def __init__(self , dance):
        self.dance = dance

    def show(self):
        print(f"{self.dance}")

class person(dancer , employee): #It will call that func whose name is given first, here employee's func will run
    def __init__(self, name , dance): #If dancer was ahead, then that show func would have been called
        self.name = name
        self.dance = dance

   

obj = person("Hirak" , "Street Dancer")
obj.show() #Now in c++ this will be known as ambiguity, as two func of same name which to call?
           #But in python we have a simple solutions i.e
"""

"""
                                                    Multilevel Inheritance
class a:
    pass

class b (a):
    pass

class c(b):
    pass
"""

"""
                                                    Hybrid Inheritance
Hybrid - When we use two or more inheritances at the same time then its calles as hybrid
# Using Single and multiple
class a:
    pass

class b (a):
    pass

class c(a):
    pass

class d(c,b):
    pass
"""

"""
                                                         Time Module       
Lets make a program that will tell how many mins takes to run a for and while loop

import time

# Time.time()
t1 = time.time() #Here this is shuru vatt ka time 
for i in range(1,51):
    print(i)
print(time.time()-t1) #Then if i minus shruvat ka with current time then I will get my required time
        # Suppose go get up at 10, then came back to your house at 12, Then if i minus  = 2


t2 = time.time()
i =1
while(i<=51):
    print(i)
    i +=1
print(time.time()-t2)

import time

# Sleep
print(5)
time.sleep(5)
print("This was printed after 5 secs")

# strftime
import time 
print(time.strftime("%H:%M:%S  %Y-%m-%d"))
"""

"""
                                                        Walrus Operator
With walrus operator we can do assignments within an expression
# Without walrus

# food = list()
# while True:
#     a = input("Enter the food u like:")
#     if a == "quit":
#         break
#     else:
#         food.append(a)

# With walrus

# food = list()
# while (a := input("What food do u like: ")) != "quit":
#     food.append(a)

"""

# Text To speak

# from win32com.client import Dispatch

# speak = Dispatch("SAPI.SpVoice").Speak

# name  = ["Hirak" , "Rakesh" , "Kunal" , "Ahmed"]
# for i in name:
#     speak(f"Hi{i}")

"""
                                                        Generators                                                        
These are simple func that runs or does thing on the fly. Means it will not be stored in memory rather than when necessary
we will get it.
ex- A list will store but a generator will give those values when we need
Mostly used for harder, larger 

def gene():
    for i in range(1000):
        yield i #Yield is used to tell its a generator, and will go on the fly

n = gene()
# print(next(n)) #Next is used to get values on the fly
# print(next(n))
# print(next(n))

for i in gene(): #Or can use for loop
    print(i)
"""

# Sleep Reminder

# import asyncio
# from plyer import notification

# async def notify():
#     await asyncio.sleep(3600)  # Wait for 1 hour
#     notification.notify(
#         title='Time Alert',
#         message='1 hour has passed! Time to take a break!',
#         timeout=10  # Duration in seconds for the notification to stay on screen
#     )

# # Run the async function
# asyncio.run(notify())

"""
                                                  Again Revesiting OOPs
1- Basics
class archer:
    Race = "Human"
    def __init__(self , hp  , mana , arrows):
        self.hp = hp
        self.mana=  mana
        self.arrows = arrows

    def shoot(self):
        if self.arrows>1:
            self.arrows -= 1
            print(f"{self.arrows} arrows left")

        else:
            print("0 arrows left")

hirak = archer(100 , 50 , 3)
hirak.shoot()
hirak.shoot()
hirak.shoot()
hirak.shoot()
print(hirak.__dict__) #Will only give instance var not class var

2- Inheritance
class person:
    def __init__(self , age) -> None:
        self.age = age


    def walk(self):
        print("I am walking")

class sex(person):
    def __init__(self, age , gender) -> None:
        super().__init__(age)
        self.gender = gender
    
    def walk(self):
        print("I am floating")

    def show(self):
        print (f"{self.age} {self.gender}")


p = person(19)
p.walk()

s = sex(20 , "M")
s.walk()
s.show()

3- DataClasses
# Here this type of class only setting attributes, no methods thus we use dataclasses
class bow:
    def __init__(self , name , dmg) -> None:
        self.name = name
        self.dmg = dmg

bow1 = bow("Raazor" , 80)
print(bow1) #This was printing address

from dataclasses import dataclass

@dataclass
class bow:
    name : str #Here much easier and simple than previous class 
    dmg : float

bow1 = bow("Utter rex" , 4.33)
print(bow1) #This is printing values


class student:
    def __init__(self, name , list):
        self.name = name
        self.marks = list

    def avg(self):
        sum = 0
        for i in self.marks:
            sum +=i

        print(f"The avg of {self.name} is :",sum/3)

s1 = student("Hirak" , [99,44,2])
s1.avg()
s2 = student("Pankaj" , [22,44,55])
s2.avg()
"""

# class bank:
#     def __init__(self  , acc):
#         self . balance = 0
#         self . account_no = acc

#     def credit(self):
#         self.balance += int(input("Enter the credited amt:")) 

#     def debit(self):
#         self.balance -= int((input("Enter the debited amt")))

#     def av_balance(self):
#         print(f"Your balance is {self.balance}")

# hirak  = bank(444)
# hirak.credit()
# hirak.debit()
# hirak.av_balance()

# tip = (6,2,3)
# ll = list(tip)
# ll.reverse()

# tip  = tuple(ll)
# print(tip)

# n = int(input("Value"))
# for i in range(1,n+1):
#     print(i , end = "")

# string = "Hirak bala"
# a = string.split()
# a = "-".join(a)
# print(a)

# def print_full_name(first, last):
#     # Write your code here
#     str = f"Hello {first} {last}! You just delved into python"
#     print(str)

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


# string = "Hirak Hirak bala"
# sub  = "Hirak"
# countt= string.count(sub)
# print(countt)

# 1- Create a qr code
# import qrcode
# qrr = qrcode.make("https://www.google.com/") #First assign the url u need the qr for
# qrr.save("Google.png") #Then save it, if run then will be saved on onii chan document

# 2- Email checker
# email = input("Enter your email: ")

# # Check if the email is non-empty
# if len(email) > 6:
#     # Check if the first character is uppercase
#     if email[0].isupper():
#         # Check if there is exactly one '@' symbol in the email
#         if "@" in email and email.count("@") == 1:
#             # Check if there is a '.' within the last four characters
#             if email[-4] == ".":
#                 # Check if the rest of the email is in lowercase
#                 if email[1:].islower():
#                     # Check if there is a space in the email
#                     for i in email:
#                         if i == " ":
#                             print("Wrong email")
#                             break
#                     else:
#                         print("Email is valid")
#                 else:
#                     print("Email should be lowercase after the first character")
#             else:
#                 print("Email should contain a '.' near the end")
#         else:
#             print("Email should contain exactly one '@'")
#     else:
#         print("First character should be uppercase")
# else:
#     print("Email cannot be empty")



import os
print(os.getcwd())
print("hello")

