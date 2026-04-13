# functions :
# ques1 :
# hcf = 1
# def HCF(a,b):
#     hcf = 1
#     if a<b:
#         small = a
#     else:
#         small = b
#     for i in range(1,small+1):
#         if (a%i==0) and (b%i==0):
#             hcf = i
#     print("the hcf of the given number is : ",hcf)
# (HCF(20,40))
# (HCF(529,456))
# def factor(n):
#     fac_sum = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             fac_sum = fac_sum + 1
#             print(i)
#     print("The total number of factors are : ", fac_sum)

# factor(7)
# factor(10)
# user = input("m")
# def ASCII_to_value(a):
#     print(f"ASCII to value {a} :",ord(a))
# def value_to_ASCII(b):
#     print(f"value to ASCII {b} :",chr(b))
   
# ASCII_to_value('a')
# value_to_ASCII(97)

# def bin_oct_hexa(a):
#     print("binary equivalent :",bin(a))
#     print("octal equivalent : " ,oct(a))
#     print("hexadecimal equivalent : " ,hex(a))
# bin_oct_hexa(10)
# def sum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum+i
#     print(sum)
# sum(5)

# 5! =5*4*3*2*1
# def factorial(n):
#     if n==1:
#         return n 
#     elif n <0:
#         print("Please enter the positive number!")
#     fac = 1
#     for i in range(n,0,-1):
#         fac = i*fac
#     print(fac)
# # factorial(7)
# str1 = "P@#yn26at^&i5ve" 
# count_char = 0
# count_symb = 0
# count_num = 0
# for ch in str1:
#     if ch.isalpha():       
#         count_char += 1
#     elif ch.isdigit():     
#         count_num += 1
#     else:                  
#         count_symb += 1
# print("Chars =", count_char)
# print("Digits =", count_num)
# print("Symbols =", count_symb)   
# string = "Hello COMPUTER!"
# print(len(string))

# user = input("Enter a string : ")
# first_time = []
# duplicate = []
# dup_sum= 0
# for i in user:
#     if i not in first_time:
#         first_time.append(i)
#     else:
#         duplicate.append(i)
#         dup_sum = dup_sum+1
# print("The duplicate character is :  ",duplicate)    
# print("The sum of the duplicate character is :  ",dup_sum)   
# str = input("Enter a string: ")
# rev = ""
# for i in range(len(str)-1,-1,-1):
#       rev = rev+str[i]
# if rev == str:
#         print("String is pallindrom ")
# else:
#      print("String is not pallindrom")


# #  Write a Program to find the square root of a number.
# num = int(input("Enter a number :"))
# sqr_root = num**0.5
# print("The square root of the number is :",sqr_root)

# import math
# # find the value tan of 45 degrees :
# degree = 45
# angle = degree*2*math.pi/360.0
# math.tan(angle)
# print(angle)

# Write a program to print the calendar for the month of March, 1991.
# import calendar
# c = calendar.month(2007,9)
# print(c)

# age = input("Enter your age : ")
# print(age)

# OOPS PRACTICE CODE --------------------

# class Factory :
#     def __init__(self,brand,product,per_costing):
#         # print(self)
#         self.brand = brand
#         self.product = product
#         self.per_costing = per_costing

#     def show_details(self):
#         print(f"Your details or the factories are {self.brand} , {self.product} , {self.per_costing}")


# ojc = Factory("reebok" , "shoes" , 500)
# ojc1 = Factory("campus" , "bags" ,1000)
# # print(ojc.brand ,ojc.product,ojc.per_costing)
# # print(ojc1.brand ,ojc1.product,ojc1.per_costing)

# ojc.show_details()
# ojc1.show_details()

# # TYPES OF ATTRIBUTES AND CLASSES:
# class Houses :
#     friends = "vibes_match_life_set" # class attributes
#     def __init__(self,floor,rooms,price):
#         self.floor = floor # "instance attributes" because it targeted the ojectet which is instance_of_class(baccha_of_class)
#         self.rooms = rooms
#         self.price = price
#     def dekhoji(self):
#         print(f"According to you choice your floor is {self.floor},you have {self.rooms} rooms at {self.price}/-")
#     @classmethod
#     def decorator_1(cls):
#           print("Hey i iam a one of the method from decorators , My name is CLASS METHOD!")# "cls" target the class's location and "self" target the object's location. The difference is you can call that like object but you can not access the details or data or attributes as self can!
#     @staticmethod
#     def decorator_2():
#         print("Hey! iam the second decorator , STATIC METHODS!!")
          
# ojc = Houses("second",4,"40,00,000")
# print(ojc.floor,ojc.rooms,ojc.price)
# ojc.dekhoji()
# ojc.decorator_1()
# ojc.decorator_2()
# print(ojc.friends)

# self practice question :
# class bank:
#     def __init__(self,branch,placeholder,balance):
#         self.branch = branch
#         self.placeholder = placeholder
#         self.balance = balance
#     def user(self):
#          print(f"The name of your branch is {self.branch}")  
#          print(f"The name of the placeholder is {self.placeholder}")
#          print(f"{self.placeholder} , you have {self.balance}/- in your account")
#     def deposit(self,add_bal):
#        self.add_bal = add_bal
#        self.balance = self.balance + self.add_bal
#        print(f"After depositing {self.add_bal}/- amount the total balance in your account is {self.balance}/-")
#     def withdrawn(self,amt_with):
#         self.amt_with = amt_with
#         if self.balance < self.amt_with:
#             print("Sorry you can't coz of insufficient balance .")
#         else:
#             self.balance = self.balance - self.amt_with
#             print(f"After withdrawing {self.amt_with}/- amount the total amount in your account is {self.balance}/-")

# obj = bank("SBI" , "Monika Gupta" , 500)
# obj.user()
# obj.deposit(50000)
# obj.withdrawn(0)
# print("CONGRATS! CODE EXECUTED SUCCESSFULY")

# INHERITENCE PRACTICE CODE --------------

# class Father:
#     def __init__(self,name):
#         self.name = name
#         print(f"Hey! my name is {self.name} and iam your parent class")
# class Child(Father):
#     def __init__(self,age):
#         self.age = age
#         print(f"The age of my Father is {self.age} and by the way this a child class")
# ojc = Father("Ramesh")
# ojc2 = Child(45)


# class Baap:
#     a = "baap baap hota hai beta beta hota hai"
#     def __init__(self,name):
#         self.name = name
#         print(f"The name of the dadaa ji is : {self.name}")

# class Beta(Baap):
#     def __init__(self, name):
#        self.name = name
#        print(f"The name of the papa ji is : {self.name}")
#     b =  "baap bada n bhaiya , the all thing is that ke bhaiya sbse bada rupeeya!...."
# class Pota(Beta):
#     def __init__(self,name):
#         self.name = name
#         print(f"The name of the pota is : {self.name}")
#     pass


# ojc1 = Baap("Mahesh")
# ojc2 = Beta("Mannu")
# ojc3= Pota("muchu")
# print({ojc3.b} ,"^ -_- ^" ,{ojc2.a} )


# class Zoo:
#     def __init__(self ,animal= "Lion"):
#         self.animal = animal
#         print(f"your animal is : {self.animal}")
        
# class Animal(Zoo):
#     def __init__(self, animal = "Dog" , name = "tommy"):
#         super().__init__(animal)
#         self.name = name
#         print(f"The name of your animal is : {self.name}")


# # obj = Zoo("Cat")
# ojb2 = Animal(33)


# class Factory:
#     def __init__(self , material , zip):
#         self.material = material
#         self.zip = zip
#         # print()

# class Bhopal_fac(Factory):
#     def __init__(self, material, zip , colour):
#         super().__init__(material, zip)
#         self.colour = colour
      

# class Pune_fac(Bhopal_fac,Factory):
#     def __init__(self, material, zip, colour , pocket):
#         super().__init__(material, zip, colour)
#         self.pocket = pocket
#         print(f"The material of the bag is {self.material} and the zip will be in your bag is {self.zip}",f"and the colour of your bag is {self.colour} and the pocket will be in your bag is {self.pocket}")
    

# # buyer1 = Factory("leder" , 4)
# # buyer2 = Bhopal_fac("nylon" , 45, "black")
# buyer3 = Pune_fac("Nylon" , 3 ,"white" , 6)
# # main point is agr tum agr tum multilevel inheritence kr rahe ho bss sbse neeche wali class ka object  banao aur usko call kro toh vo saare parameters khud hi maang lega !!

# POLYMORPHISMS LEARNINGS -----------

# so the polymorphism means when the parent class and the child class have the name method which means iam writing a method 1 in parent calss with name of "show" and iam writing this same name "show" in child class as method!!!!ufff that's the whole concept of polymorphism :)

# class parent:
#     def show(self):
#         print("Ima the parent class.")

# class child(parent):
#     def show(self):
#         print("Iam the child class.")

# obj = child()
# obj.show() # output : iam the child class

# It means there is one more concept which kNown as "METHOD OVERRIDING" it means pahele parent ke show kw pass output mein aane ka tha lekin child classs inheritence mei hai toh vo jo show hoga vo child ka hoga.

# "METHOD OVERLOADING" IS NOT ALLOWED IN PYHTON
#  Method overloading means having same name methods inside a class but parameters will be different but in python the latest definition will overwrite the previous one.


# ENCAPSULATION LEARNING --------------


# It only means that we wanted to protct our attributes and the method from accessing by any ojection and calls for this we have to use the "ENCAPSULATION".
# for better understanding go to the pyhton books of shreiyans

# class Factory:
#     _a = print("Iam the suprerior")
#     def show(self):
#         print("IAm the factory class")
# class Fac(Factory):
#     def show (self):
#         print("IAm show statement")
#         print(super()._a)

# obj = Fac()
# obj.show()
# there are three types of encapsulation:
# 1. public 2. protected 3. private 
# 
# 3.(PROTECTED) 

# class Demo:
#     a = 45000 
#     def __init__(self):
#         self.name = "sheriyans"
#         self._age = 45
#         self.__salary = 20000

#     def show(self):
#         print("Inside the class : ")
#         print("Public:" , self.name)
#         print("PROTECTED :" , self._age)
#         print("Private:" , self.__salary)

#     def show(self):
#         self.__salary = "a"     
# obj = Demo()
# obj.show()

# ABSTRACTION ------------------

# means if you wanted while making a class some set o rules should be follow you put that rules into the abstration  method let's see howw!!!!
# from abc import ABC ,abstractmethod
# class Abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Abstract):
#     def perimeter(self,side):
#         self.side = side 
#         print("The perimeter of the square is :", 4*side)
#     def area(self , side):
#         self.side = side
#         print("The area of the square is :", side*side)

# class Rectangle(Abstract):
#     def perimeter(self , length , wide):
#         self.length = length
#         self.wide =  wide
#         print("The perimeter of the rectangle is :", 2*(length+wide))
#     def area (self , length ,wide):
#         self.length = length
#         self.wide =  wide
#         print("The area of the rectangle is :", length*wide)

# obj = Square()
# obj.perimeter(3)
# obj.area(3)
# obj2 = Rectangle()
# obj2.perimeter(4,5)
# obj2.area(4,5)


# DUNDER METHOD ----------------

# class Animal :
#     def __init__(self , name ,age):
#         self.age = age
#         self.name = name
        
    
#     def __str__(self):
#         return f"Hey my name is {self.name}" , f"Hey my age is {self.age}"
        
#     def __add__(self , other):#self is the first thing jisko add krna or other is the another thing jisko self ke ander jodna hai ..
#         sum =0
#         for i in other:
#             sum = sum+i.age
#         return f"The sum of the ages is : {self.age + sum}"

# obj = Animal("Lion" , 45)
# obj2 = Animal("dolphin" , 24)
# obj3 = Animal("tiger" , 21)

# print(obj+(obj2 ,obj3))



# class Count:
#     def __init__(self , num1 , num2):
#         self.num1 = num1
#         self.num2 = num2
#     def check(self):
#         if self.num1 %2 == 0:
#             print(f"{self.num1} is Even.")
#         else:
#             print(f"{self.num1} is odd.")
#         if self.num2 %2 == 0:
#             print(f"{self.num2} is Even.")
#         else:
#             print(f"{self.num2} is odd.")

#     def __add__(self,other):
#         # even_sum =0
#         # odd_sum = 0
#         for i in other:
#             # if self.num1 %2 == 0:
#             #     True
#                 even_sum = even_sum + i.num1
#             # else:
#             #     odd_sum = odd_sum + i.num1

#         return f"The sum of the even number is {self.num1 + even_sum}"           
           
# obj = Count(2,5)
# # print(obj.check())
# obj2 = Count(4,5)
# obj3 = Count(3,1)
# print(obj +( obj2 , obj3))


# # DECORATORS ------------

# class Animal :
#     @property
#     def show(self):
#         print("nothing")
# obj = Animal()
# obj.show

# def decorate(func):
#     def wrapper():
#         print("I will print my self before the function.")
#         func()
#         print("I will print after.")
#     return wrapper

# @decorate
# def hello():
#     print("HEy iam monika gupta")
# hello()
# def sum(*agrs):
#     sum = 0
#     for i in agrs:
#         sum = sum + i
#     print(sum)
# sum(12,3,5,6,4,8,9)


# def info(**kagrs):
#     for i in kagrs:
#         print(f"{i} : {kagrs[i]}") 
# info(name="monika",age = 18,language = "python")

# BUILD LOGICS -----------

# user = [1,2,3,4,5,6,7]
# root = map(lambda user: user**2,user) 
# # print(list(root))
# # print(list(user()
# a = [2333,35,3,42]
# result = filter(lambda x : x%2==0,a)
# print(list(result))


# # Write a program to find the area of a Rectangle.
# length = int(input("Enter the length of a rectangle : "))
# width = int(input("Enter the width of a rectangle :"))
# area = (length*width)
# print(f"The area of rectangle is :",area)

# #  Write a program to swap the values of two variables.
# num1 = int(input("Enter a number :"))
# num2 = int(input("Enter a number :"))
# num1,num2 = num2,num1
# print("num1 = ",num1)
# print("num2 = ",num2)

# # Write a program to find whether a number is even or odd.
# n = int(input("Enter a number :"))
# if n %2 ==0:
#     print("The number is even.")

# else:
#     print("The number is odd.")
        
# #  Write a program to check the largest among the given three numbers.
# num1 = int(input("Enter a number :"))
# num2 = int(input("Enter a number :"))
# num3 = int(input("Enter a number :"))
# if (num1>=num2) and (num1>=num3):
#     print(f"The {num1} is largest among the three.")
# elif (num2>=num1) and (num2>=num3):
#     print(f"The {num2} is largest among the three.")
# elif (num3>=num1) and (num3>=num2):
#     print(f"The {num3} is largest among the three.")

# Write a Python program to check if the input year is a leap year or not.
# year =int(input("Enter a year which you want to check : "))
# if (year%4) ==0:
#  if (year%100)==0:
#         if(year%400)==0:
#             print("yes ! it's a leap year")
#         else:
#             print("no ! it's not a leap year")
# else:
#      print("no ! it's not a leap year yes") 

#  Write a program to demonstrate While loop with else:
# count =int(input("Enter a number :"))
# while count >3:
#     print("Inside the while loop")
#     print(count)
    
# else:
#     print("Outside the while loop.")


# #  Write a Python program to print the prime numbers for a user provided range.
# low = int(input("Enter lower range for prime numbe : "))
# upper = int(input("Enter upper range for rime number :"))
# for n in range(low , upper+1):
#    if n>1:
#     for i in range(2 , n):
#       if (n%i)==0:
#             break
#       else:
#         print(n)
         
# def data(student,fee=2500):
#     print("Name of the student is :",student)
#     print("Fee of the student is :",fee)

# data("monika")


# Write a function which accepts two numbers and returns their sum :
# sum1 = int(input("Enter number 1 :"))
# sum2 = int(input("Enter number 2 :"))
# def sum():
#     print("Number 1 is :", sum1)
#     print("Number 2 is :", sum2)
#     total = sum1+sum2
#     print("The the sum of both numbers is :",total)

# sum()

# # Calculate the sum of two numbers entered by the user.
# a = int(input("Enter a number a :"))
# b = int(input("Enter number b :"))
# sum = a+b
# print( "The sum of both number is : " ,sum)

# # Write a Python program to check if a given number is even or odd.
# num = int(input("Enter a number : "))
# if num % 2 == 0:
#     print("The given is even number")
# else:
#     print("THe given number is odd")

# Calculate the factorial of a given number.

# n = int(input("Which number's factorial you want , Enter here : "))
# def factorial(n):
#    if n == 1 or n == 0:
#           return 1
#    else:
#        return( n * factorial(n-1))
   
# print("The factorial of your given number is :" , factorial(n))


#  Find the largest among three numbers entered by the user.

# x = int(input("Enter first number : "))
# y = int(input("Enter second number : "))
# z = int(input("Enter third number : "))
# if (x>=y and x>=z):
#     print("'x' is largest among three numbers. ")
# elif (y>=x and y>=z):
#      print("'y' is largest among three numbers. ")  
# elif (z>=x and z>=y):
#      print("'z' is largest among three numbers. ") 
# else:    
#      print("PROGRAMME ENDED")    

# Write a Python program to print all even numbers from 1 to 20
# for i in range(1,21,2):
#     print("This are the all even number." , i)


# Calculate the sum of all numbers from 1 to a given number.

# n = int(input("Enter a number :"))
# sum = 0
# for i in range(1,n+1):
#    sum+=i
# print("The sum of all number from 1 to 10 is : ",sum)

# # Calculate the sum of all even numbers from 1 to a given number.
# n = int(input("Enter a number : "))
# sum= 0
# for i in range (2,n+1,2):
#    sum+=i
# print("THe sum of n even number will be : ",sum)


# # Write a Python program to check if a given string is a palindrome.
# a = input("Enter something : ")
# a= a.lower()
# b = a[::-1]   #[start:stop:step] 
# # start:kahan se shuru  karnahai (default = 0)
# # stop: kahan tak jaana hai (default = end tak)
# # step: kitne step mein aage badhna hai (default = 1)
# if (a==b):
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")

# Count the number of vowels in a given string.
# str = input("Enter a something alphabetical :")
# vowels ="aeiouAEIOU"
# count = 0
# for i in str:
#     if i in vowels:
#         count+=1
# if count>0:
#     print("The number of vowels present in a given string is :", count)
# else:
#     print("There is no vowel present in the string")


# # Reverse a given list in-place.
# l = ["monika",4,5,5]
# l.reverse()
# print(l)

# #  Remove duplicates from a list.
# l = ["monika",5,6,8]
# l.remove("monika")
# print(l)

# #  Convert a string to uppercase.
# a = "string"
# b = a.upper()
# print(b)


# # Calculate the area of a circle with a given radius.
# radius = int(input("Enter any number of radius :"))
# area = 3.1416*radius*radius
# print(f"The area of circle with radius {radius} is",area)

# #  Replace all occurrences of a character in a string.
# s = "monika gupta"
# new_str = s.replace('m','M').replace('g','G')
# print(new_str)

#  Write a Python program to find the maximum element in a list.
# l =[1 , 2 , 1 ,5 ,7]
# l_max = max(l)
# print("the maximum element in this list is : " , l_max)

# l1 = ["n" , "krikufhorhoncsh" , "kimonikai"]
# l2 = max(l1, key = len)
# print(l2)

# # Calculate the square root of a given number.
# n = int(input("Enter a number : "))
# if n==1 :
#      print("1")
# elif n==0:
#         print("0") 
# a = n**0.5
# print("The square root of the number is :" , a)


# # Check if two strings are anagrams.
# str1 = input("Enter something alphabatical 1 : ")
# str2 = input("Enter something alphabatical 2 : ")
# if sorted(str1) ==sorted(str2):
#     print("It's an anagram !")
# else:
#     print("It's not an anamgram !")


# # Check if a list is empty.
# l = []
# if not l:
#     print("The list is empty")
# else:
#     print("The list is not empty")

# # Calculate the power of a number.
# base = int(input("Enter a number :"))
# power = int(input("Enter an exponental(you want) number :"))
# calc = base**power
# print(calc)

#  Find the length of the longest word in a given sentence.
# sentence = input("Enter a sentence : ")
# words = sentence.split()
# max_length = 0
# for word in words:
#     if len(word)>max_length:
#         max_length = len(word)
# print("The longest word in thi sentence is : ",max_length)
# print(word)

# # Check if a given number is a perfect square.
# num = int(input("Enter a number : "))
# if int(num**0.5)==num**0.5:
#     print("This number is a perfect square")
# else:
#     print("This number is not a perfect square")

# # Find the common elements between two lists.
# l1 = ["monika" , 5,6,89,"krishna"]
# l2 = ["monika", 5 ,7,98,"krishna"]
# common = list(set(l1) & set(l2))
# print("The common in both the list : ", common)

# # capitalize the first letter of each word in a sentence.
# a = input("Enter a sentence :")
# cap = a.title()
# print(cap)


# Print the Fibonacci sequence up to a given number of terms.
# n = int(input("Enter the number of terms: "))

# a, b = 0, 1
# count = 0

# if n <= 0:
#     print("Please enter a positive integer")
# elif n == 1:
#     print("Fibonacci sequence:")
#     print(a)
# else:
#     print("Fibonacci sequence:")
#     while count < n:
#         print(a, end=' ')
#         a, b = b, a + b
#         count += 1



# # MCQS:
# 1.B
# 2.B
#3.a
#4.c
#5.c and d
#6.a
#7.b
#8.a
#9.c
#10.a
#SECTION - "B"
#ques1 :
# num = int(input("Enter a number : "))
# if num %2==0:
#     print(f"{num} is Even.")
# else:
#     print(f"{num} is Odd.")

# ques2:
# str = input("Enter a string : ")
# vowels = "AEIOUaeiou"
# vowels_count = 0
# for i in str:
#     if i in vowels:
#         vowels_count = vowels_count + 1
# print(f"The total number of vowels in {str} is : " , vowels_count)
# ques - 3:5*4*3*2*1
# num = int(input("Enter number : "))
# factorial = 1
# for i in range(num,0,-1):
#     factorial = factorial * i
#     print(i)
# print(f"The factorial of {num} is : ",factorial)
#ques - 4 :
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         True
#         print(i)
# ques -5:
# l = [4,5,6,1,2,3,7,8]
# largest = l[0]
# sec_largest = l[0]
# for i in range(len(l)-1):
#     if l[i+1]>largest:
#         sec_largest = largest   
#         largest = l[i+1]
#     elif l[i+1]>sec_largest or l[i+1]<largest:
#         sec_largest = l[i+1]
# print(largest)
# print(sec_largest)
# ques - 8 : monika
# str = input("Enter an item : ")
# rev = ""
# for i in range(len(str)-1,-1,-1):
#     rev = rev + str[i]
# if str == rev :
#     print("Its a pallinrome")
# else:
#     print("Its not a pallindrome")
# ques - 6:
# str = input("Enter a number : ")
# rev = ""
# for i in range(len(str)-1,-1,-1):
#     rev = rev+str[i]
# print(rev)
# que - 7:
# students = {}
# n = int(input("How many students? "))
# for i in range(n):
#     name = input("Enter student name: ")
#     mark = int(input("Enter marks: "))
#     students[name] = mark   

# topper = max(students, key=students.get)

# print("Student Marks:", students)
# print("Topper is:", topper, "with", students[topper], "marks")


# def func(num1):
#     if num1%2==0:
#         print(f"{num1} is even!")
#     else:
#        print(f"{num1} is odd!")
  
# func(5)
# func(4)

# def func(str):
#     print(f"The legnth of {str} is : ",len(str))

# func("monika")
# func("neelakshi")

# def func(num1 , num2):
#     sum  = num1 + num2
#     print("The sum of the both number is : " ,sum)

# func(5,4)

# def func(num):
#     even = []
#     for n in num : 
#         if n % 2 == 0:
#             even.append(n)
#         return even
# num = [3,5,6,1,2,3,7,8]
# print("Even numbers:", func(num))

# def print_even(numbers):
#     evens = []
#     for n in numbers:
#         if n % 2 == 0:
#             evens.append(n)
#     return evens

# # Example
# num = [3,5,6,1,2,3,7,8]
# print("Even numbers:", print_even(num))

# def func(s=""): 
#     return s.upper()   
# print(func("monika"))

# def func(str):
#     return str.upper() , str.lower()
# # print(f"The uppercase will be : {str.upper} and the lower will be {str.lower}")

# print(func("monika"))
# list = [1,2,3,4,5,6]
# def func(numbers = []):
#     add= 0
#     for i in numbers:
#        add = add+i
#     print("the sum of the given number is :" , add)
#     return numbers , add ,len(numbers),(add)/len(numbers)

# print(func([5,3,4,5,6,7,8,9]))
# list = [1,2,3,3,4,5,5,6]
# def func(list = []):
#     new_list = []
#     for i in list:
#         for j in new_list:
#             if i != j:
#                 new_list.append(i)
#     print(new_list)

# print(func([1,2,3,3,4,5,5,6]))


# n = input("How many pairs you want : ")
# num = input("Enter number : ")
# array = list(num)
# print(array)
# dict1 = {}
# for i in array:
#     if i in dict1.keys():
#       dict1[i]+=1
#     else:
#        dict1[i] = 1
# for i in dict1:
#     if dict1[i]%2==0:
#       print("True")
#       continue
#     else:
#        print("False")
# print(dict1)

# list = [2,2,3,3,5,5] output : (2,2),(3,3),(5,5)
# # for i in array:
# if len(array)-1 == n*2:
#     print("True")
# else: 
#     print("False")
