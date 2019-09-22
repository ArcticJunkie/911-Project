
print("Hello World")
print("Welcome to Edureka")

print("Happy Learning \nWelcome to Python")

######################################Variables
A=10
B='edureka!'

print(A,B)

#another example

x,y,z=10,20,30

print(x)
print(y)
print(z)


######################################Numbers
A=10

B=10.65

C=10+6j

print(A,B,C)


######################################String
str1='Welcome'
str2="to"
str3="""101001"""

print(str1)
print(str2)
print(str3)

string="Python"
print(string)
print(len(string))
print(string[1:4])
print('y' in string)

0



print("Welcome to %s"%("python"))
print("My name is %s and my age is %d"%("jupyter",20))

str='edurekakakakakaka222'
print(str.capitalize())
print(str.count("ka",0,11))
print(str.count("ka",0,len(str)))



print(max(str))
print(min(str))
print(str.replace('e','--E--',3))
print(str.upper())
print(str.index('k'))

str1="Happy Learning"

print(str1[::-1])

print(str1[2:7])

print(str1.find('L'))

str2="Welcome to Edureka"

print(str1+' '+str2)

print(str1*20)



######################################Tuples#60
tup1=("Haddop","Haddop","Java")

print(len(tup1))
print(max(tup1))
print(min(tup1))





tup1=("Haddop","Python","Java")

print(len(tup1))

print(tup1*3)

print("Java" in tup1)

tup2=(1,3,5,7)
tup3=(2,4,6,8)
tup4=tup2+tup3
print(tup4)


print(tup2)


tup=(1,3,5,2)

print(sorted(tup))

print(tup[::-1])


tuple1=(1,3,5,7,'a','b')
lst=list(tuple1)

print(sorted(tuple1))

print(lst)

tuple1[0]="Python"
print(lst)

tuple2=tuple(lst)
print(tuple2)


######################################Diff b/n list and tuples
#List
list=[1,2,"Python","Android"]
print(list)

list[2]="Data Science"
print(list)

#Tuple
tup=(1,2,3,"Data Science")
print(tup)

tup[1]="Python"
print(tup)


########################################List inside tuple
list=[(1,2,3),("Python","Java")]
print(list)
print(len(list))
print(list[1][1])

list[0][1]=50
print(list)

list[0]=(6,7,8)
print(list)



tup=([1,2,3],[3,4,5],[5,6,7])
print(tup)
print(len(tup))
print(tup[0][1])

#Updating Tuple
tup[0][1]=90
print(tup)

#Deleting element in Tuple
del(tup[1])
print(tup)





list=[1,2,'Python','Android']
print(list)

list[2]='Data Science'
print(list)

tup=(1,2,3,'Data Science')
print(tup)

tup[1]='Python'
print(tup)



tuple1=(1,2,3,5,7,'a','b')
lst=list(tuple1)
print(lst)

lst[1]='Python'
print(lst)

tuple2=tuple(lst)
print(tuple2)




##########################################List Indexing and Slice
list=["Hadoop","Python","Android"]
print(list[1])

print(list[0:2])

print(list[-1])

list=["Hadoop","Python","Android"]

list[1]="Java"
print(list)

del(list[2])
print(list)

list=[1,2,3]
list.append("Machine Learning")
print(list)

list.extend(['g','h'])
print(list)

list.insert(1,'Scripting')
print(list)

list.remove(3)
print(list)




list3=[1,2,5,'Python','Haddop']
print(type(list3))

print([x**2 for x in[1,2,3,4,5]])


list4=['Pytyhon','Java','Haddop','Android']
print(list4.sort())
print(list3.reverse())

print([x**2 for x in[1,2,3,4,5]])

list=[1,2,3,4,5,'a','b','c']
print(list.pop(3))

list.remove('a')
print(list)

list1=['Python','XYZ','ABC','PQR']
print(list1)

print(sorted(list1))

print(list1[::-1])



###################################################Tuple inside a LIST
list=[(1,2,3),("Python","Java")]
print(list)
print(len(list))
print(list[1][0:1])

list[0][1]=50
print(list)





tup=([1,2,3],[3,4,5],[5,6,7])
print(tup)
print(len(tup))
print(tup[0][1])

#Updating Tuple
tup[0][1]=90
print(tup)

#Deleting element in Tuple
del(tup[1][2])
print(tup)





list=[1,2,'Python','Android']
print(list)

list[2]='Data Science'
print(list)

tup=(1,2,3,'Data Science')
print(tup)

tup[1]='Python'
print(tup)



tuple1=(1,2,3,5,7,'a','b')
lst=list(tuple1)
print(lst)

lst[1]='Python'
print(lst)

tuple2=tuple(lst)
print(tuple2)



################################################DICTIONARIES
A={'Age':24, 'Name':'John'}

print(A)

dict={1:"Python",2:"Android"}
print(dict)
print(dict[2])

dict[1]="Javascript"
print(dict)

del(dict[2])
print(dict)

print(len(dict))

print(type(dict))


#add
dict1={1:'Python',2:'Android'}
print(dict1.items())

print(dict1.keys())

print(dict1.values())



dic={3:'Python',1:'Java',2:'Big Data'}
ks=(dic.keys())
print(ks)

sk=sorted(ks)
print(sk)

for key in sk:
    print(key,'=>',dic[key])



rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],'age': 40.5}
print(rec.get('name'))
rec['name']['last']


#############################################################TUPLES an LIST in a DICTIONARIES
#tuple in set
dict={1:(1,2,3),2:(3,4,5)}
print(dict)
print(dict[1][1])


#list in set
dict={1:["Python","Java"],2:[1,3,5,7]}
print(dict)
print(dict[1][0])


###################################################################SET
A={1,2,3,3}

print(A)

###SET operator
X=set('Welceeeeome To Edureka')
print(X)

A={1,2,3,4}
B={3,4,5,6}
print(A|B)
print(A&B)

A={1,2,3,4,5}
B={4,5,6,7,8}
print(A-B)

s={'a','b','c','d','e','f','o','v'}
set1={'a','b','d','o','v'}
set2={'a','c','d','o','e'}
print(set1|set2)
print(set1&set2)
print(set1-set2)

#add

s={1,2,3,'a','b'}
set1={1,'a','b'}
print(5 in s)

print(set1.issubset(s))

print(5 not in s)

print(s.issuperset(set1))

print(s.union(set1))

print(s.intersection(set1))

print(s.difference(set1))

print(s.symmetric_difference(set1))


s={1,2,3,'a','b'}
s.add('c')
print(s)

s.remove(1)
print(s)

s.discard(3)
print(s)


s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.remove(10)
print (s)
s.discard(10)


 

s.pop()
print(s)

s.clear()
print(s)


#################################################PYTHON OPERATORS

########################################### OPERATORS
# Arithmetic operators
a=50
b=40
print(a+b)

print(a-b)

print(a*b)

print(a/b)

print(a%b)

print(a//b)

print(a**b)


#Assignment Operators

a=30
b=30
a=b
print(a)

a=a+b
a+=b
print(a)

a=a-b
a-=b
print(a)


a*=b
print(a)

a/=b
print(a)

a = a**b
a**=b
print(a)

a//=b
print(a)

# Comparison Operator
a=50
b=100
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Logical Operators

a=101
b=50

print(a and b)
print(a or b)
print(b or a)
print(not a)


#Bitwise Operators
a=10
b=35

print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>b)

#Identity Operators

a=[1,3,5,7,'Python']
a=b
print(b is a)

print(a is not b)

# Membership Operators

list1=[1,10,100,"Data Science"]
print(30 in list1)
print(20 not in list1)




#####################CONDITIONAL OPERATORS
X=15
Y=15

if(X<Y):
    print('X is less than Y')
   
elif(X>Y):
    print('X is greater than Y')
else:
    print('X and Y are equal')



# If else statement
a=30

if(a<10):
    print("Less than 10")
if(10<=a<=25):
    print("In between 10 and 25")
else:
    print("Greater than 25")

# if elif else

marks=70
if(marks<40):
    print("Fail")
elif(40<marks<=60):
    print("Average")
else:
    print("Congratulations!! Well done")

	
	
##################################################LOOPS

################################WHILE LOOP
count=0
while(count<=5):
    print(count)
    count=count+1
print("Good bye!")


#Example
rank=5
while(rank!=12):
    print("Rank is ",rank)
    rank+=1

################################FOR LOOP
fruits=['Banana','Apple','Grapes']

for index in range(len(fruits)):
    print(fruits[index])
    
    

#Example

list1=[1,2,3,"Python"]

for i in list1:
    print(i)
	




#######################################NESTERD LOOPS

count=1
for i in range(10):
    print(i)

    for j in range(i,10):
        count=count+2

#nested loops
for i in range(1,4):
    print("#")
    for j in range(1,5):
        print("*")
		
		
################################LOOP CONTROL	
for i in range(10,50):
    print(i)
    if(i==30):
        break

for j in range(1,11):
    #print(j)
    if(j==5):
        continue
    print(j)



for k in range(1,3):
    pass

print("Loop ends here")





#################################################KEY BOARD INPUT
str=input("Enter your input")
print("Received input is: ",str)


# Example

name=input("Enter your name")

age=input("Enter your age")

print("Welcome ",name)
print("Your age is ",age)

print("After 5 years, your age will be :",(int(age)+5))




##################################################FILE OPERATIONS
import os
newfile=open("Edureka_Py.txt","w+")

for i in range(1,10):
    newfile.write("\n Hello, welcome to Python:")


for i in range(1,10):
    print(newfile.read())

newfile.seek(5)
print(newfile.tell())
os.rename("Edureka_Py.txt","Python1.txt")
os.remove("Python1.txt")

newfile.close()






















