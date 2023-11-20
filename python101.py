#!/bin/python3

#print string

print("hello damianorina")
print(""" this is a multiline 
string word """)

#concatination
print("this is a new string" + " whats so ever")
print('\n') #new line


#math
print("math time")
print(50 + 50)  #add
print(100 - 50) #substract
print(50 * 50) #multiply
print(100/50) #division
print(50 * 50 + 25 - 40 / 50) #pemdas
print(50 ** 2) #exponents
print(50 % 8) #modulo or remainder
print(50 // 6) #number without leftover

print('\n')
#variables & methods
print("fun with variables and methods")
quote = "all is fare in love and war"
print(len(quote))#length
print(quote.upper())#uppercase
print(quote.lower())#lowercase
print(quote.title())#title

name ="Damian"
age = 26 #int int(29)
gpa = 4.5 #float float(4.5)

print("my name is " + name +" and i am" + str(age)+ " years old.")
print('\n')
age += 1
print(age)

birthday = 1
age += birthday
print(age)
#functions
print("now some functions")
def who_am_i():
	name = "Damian"
	age = 26
	print("My name is " + name +" and i am " + str(age) +"years old")
who_am_i()
#adding in parameters
def add_one_hundred(num):
	print(num + 100)
add_one_hundred(100)

#add multiple parameters
def add(x,y):
	print(x + y)
add(8,7)

#use return
def multiply(x,y):
	return x * y
print(multiply(4,5))

def square_root(x):
	return x ** 0.5
print(square_root(64))	

print('\n') #newline
#boolean expressions(True or False)
print("boolean expressions")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9
print(bool1,bool2,bool3,bool4)
print(type(bool1))

#relational and boolean operaters
greater_than = 7 > 5
less_than = 4 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)
test_and = (7 > 5) and (9 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = not True

print(test_and,test_or,test_not)
print('\n') #newline
#conditional statements
print("conditional statements")
def soda(money):
	if money >= 2:
		return "you earn yourself a Soda"
	else:
		return "No Soda for you"
print(soda(3))
print(soda(1))
def alchohol(money,age):
	if (money >= 5) and (age >= 18):
		return "You Can drink alchohol"
	elif (money <= 5) and (age >= 18):
		return "you have insufficient balance"
	elif (money >= 5) and (age <= 18):
		return "you are below 18 years old"
	else:
		return " you are under age and broke"
print(alchohol(5,18))
print(alchohol(4,18))
print(alchohol(6,16))
print(alchohol(4,16))

print('\n') #print newline
#list
print('list:')
movies = ["transformers","extraction2","john wick","fast and furious 10"]
print(movies)
print(movies[0])
print(movies[0:2])
print(movies[1:])
print(movies[:1])

print(movies[-1])
print(len(movies))
movies.append("The hangover")
print(movies)
movies.pop()
print(movies)
person = ["damian","saint john","atandi","omwando"]
combined = zip(movies,person)
print(list(combined))

print("\n")
#Tupples
print('tuples:They have parantheses and cannot be changed')
grades =("A","B","C","D")
print(grades[1])

print('\n')
#looping
print("for loop: start to finish of an iterate")

fruits = ["apple","orange","mangoes","strawberry","lemon","pineapple"]
for x in fruits:
	print(x)
	
print("while loops: Execute as long as true")
i = 1
while i < 10:
	print(i)
	i += 1
