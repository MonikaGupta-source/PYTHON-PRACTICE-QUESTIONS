#false
# true
# true
# false

# input1 = int(input("Enter a number : "))
# input2 = int(input("Enter a number : "))
# greatest = input1>input2
# if input1 > input2:
#     print("Input1 is greater than input2",f"which is {input1} ")
# else:
#     print("input2 is greater",f"which is {input2}")



# user = input("Enter your gender (please tell me your gender in male or female) : ")
# if user == "female" or user == "FEMALE":
#     print("Good morning ma'am .")
# elif user == "male" or user == "MALE":
#     print("Good morning sir.")

# else:
#     print("Undefined gender !!")


# num = int(input("Enter a number : "))
# if (num % 2 ==0 ):
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# name = input("Enter your name.")
# age = int(input("Enter your age :"))
# if age > 18 :
#     print(f" Hello {name} you can vote as your age is {age}.")
# else :
#     print(f" Hello {name} you cannot vote as your age is {age}.")


# MOST IMPORTANT LEAP YEAR WALA QUES ::
# LOGIC DO HAI :-
# 1:leap year mei do type ke year aate hai normal year or century year :
# toh 1 - century year jaise 2000 , 3000 , 4000 etc inko chekc krte hai 400 se divide krke agr divide hue toh leap hai varna nahi 
# aur 2 - jo normal hote hain jaise ki 2004,2008,2012,etc vo hote hain 4 se divede krke check 
# sbse pahele 100 se check kiya kyuki century years 100 se divisible hote hai (for 1 wala case)
# dursa ki bhaii vo agr 100 se divisible nahi hai toh 4 se hona chiye (for dusra case) 

# year = int(input("Enter a year :"))
# if (year%100==0) and (year% 400==0) :
#     print("IT's a leap year!!")
# elif  (year%100!=0) and (year%4==0):
#     print("IT's a leap year!!")
# else:
#     print("IT's not a leap year !!")



# tem = int(input("Enter your room temperature :"))
# if tem == 0:
#     print("Freezing cool")
# elif (tem <= 10):
#     print("very cold")
# elif(tem <= 20):
#     print("cold")
# elif (tem <= 30):
#     print("pleasant")
# elif tem <= 40:
#     print("hot")
# elif tem >= 40:
#     print("Very hot")


# loop's questions :

# n = int(input("Enter a number : "))
# for i in range (1,n+1):
#     print("hello word")

# n = int(input("Enter a number : "))
# for i in range(1,n+1):
#     # if i > n:
#     #     break
#     print(i)


# n = int(input("Enter a number : "))
# for i in range(n,0,-1):
#     print(i)

# n= int(input("Enter a number : "))
# for i in range (1,11):
#     print(f" {n} X {i} = ",n*i)

# n = int(input("Enter a number : "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum+i
#     print(f"The sum upto {i} term is :" , sum)
# print("The final answer is" , sum)


# # 5! = 5x4x3x2x1
# n= int(input("Enter a number : "))
# factorial = 1
# for i in range(n,0,-1):
#     factorial = factorial*(i)
# print(f"The factorial of {n} is" ,factorial ,"." )

# n = 10 , even = 2,4,6,8,10 sum = 30  and odd = 1,3,5,7,9 , sum = 25
# n= int(input("Enter a number : "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if (i % 2==0):
#         even = even+i
#     if (i % 2!=0):        
#         odd = odd+i

# print("The total number of even is : ",even)
# print("The total number of odd is : ",odd)
    
# 12 = 1,2,3,4,6,12
# n = int(input("Enter a number : "))
# for i in range(1,n+1):
#     if n % i ==  0:
#         print(i)

# n = int(input("Enter a number : "))
# print("GIVEN BELOWS ARE THE FACTORS :-")
# factor = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)
#         factor = factor+i
#         if factor == n :
        
#          print("The sum of factor is :",factor)
#          print("SO , It is a perfect numbmer.")
#          break
     
# else:
#     print("It is not a perfect number.")

# prime no. = 2,3,7 jinke factor 2 hote hai
# n = int(input("Enter a number : "))
# factor = 0
# for i in range(1,n+1):
#     if (n%i) == 0:
#      factor = factor + 1
#      print(i)
# print("The total factors are ", factor)

# if factor == 2:
#     print("It's a prime number.")
# else:
#     print("It's not a prime number")


# n = int(input("Enter a number : "))
# factor = 0
# for i in range(2,n+1):
#     if (n%i) == 0:
#      factor = factor + 1
#      print(i)
#      if factor == 2:        
#         print("The total factors are ", factor)    
#     print("It's a prime number.")
# else:
#     print("It's not a prime number")

# checking 2 se leke 500 tk kitne prime number hote hai :
# prime_count = 0
# for i in range(2,501):
#     is_prime = True
#     for j in range(2,int(i**0.5)+1):
#         is_prime = False
#         break
# if is_prime:
#     prime_count = prime_count+1
# print(prime_count)

# n = 500
# prime_count = 0
# for num in range(1,n+1):
#     count = 0 
#     for i in range(1,num+1):
#         if num%i == 0:
#             count +=1
#     if count == 2 :
#         prime_count+=1
#         print(i)
# print("Total number of primes are : ", prime_count)


# n = 500
# prime_count = 0
# for num in range(2,n+1):
#     count = 0 
#     for i in range(2,num+1):
#         if 2%i != 0:
#             count +=1
#     if count == 2 :
#         prime_count+=1
#         print(i)
# print("Total number of primes are : ", prime_count)



# str1 =  input("Enter something :")
# rev = ""
# for i in range(len(str1)-1,-1,-1):
#     rev = rev + str1[i]
    
# if rev ==str1:
#         print(f"{rev} It's a pallindrome.")
# else:
#      print(f"{rev} It's not a pallindrom.")        


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

# list ques :

# l1 = [1,-2,-3,5,-6]
# positive = 0
# negative= 0
# for i in l1:
#     if i <0:
#         negative = negative + 1
#         print("This one is the negative value of l1 :" , i)
#     else:
#         positive = positive + 1
#         print("This one is the positive value of l1 : " , i)
# print("Total positve value : ", positive)
# print("Total negative values : ",negative)

# l = [1,2,3,4,5,6,7,8,9]
# sum = 0
# for i in l :
#     sum = sum +i
#     mean=(sum)/len(l)

# print("The mean of the l is : " ,mean)


# l = [1,2,2,3,4,5,58936,7,8,9,10]
# greatest = l[0]
# index = 0
# for i in range(len(l)-1):
#     if l[i+1]>greatest:
#         greatest = l[i+1]
#         index= i + 1

# print("Greatest element is : " ,  greatest)
# print("Index of greatest element is : " ,  index)



# l = [1,2,2,3,4,5,36,35,8,9,63]
# print(l[10])
# greatest = l[0]
# second_largest = l[0]
# index1 = 0
# index2 = 0
# for i in range(len(l)-1):
#     if l[i+1]>greatest:
#         second_largest = greatest
#         greatest = l[i+1]
#         index1 = i+1
#     elif l[i+1]>second_largest and l[i+1]<greatest:
#         second_largest = l[i+1]
#         index2= i + 1

# print(f"The greatest element is {greatest} at {index1}")
# print(f"The second greatest element is {second_largest} at {index2}")


# l = [5,6,7,8,9]
# for i in range(len(l)-1):
#     if l[i] <l[i+1]:
#         continue
#     else:
#         print("not")
#         break
# else:
#     print("YOur list is sorted")

# d = {1:10,2:20,3:30,4:40}
# d[1] = 100 #updating
# d[50] = 500 #creating
# del d[3] # deleting
# print(d)


# d = {1:10,2:20,3:30,4:40}
# for i in d.values():
#     print(i) 

# help(dict)
# def print_info(name, fees=25000):
#     print( "Name:",name)
#     print ("fees:", fees)
#     return

# print_info("monika")

# 5! = 5*43*2*1
# def fact(n):
#     factorial = 1
#     for i in range(n,0,-1):
#         factorial = factorial*i
#     print(factorial)

# fact(5)


# WEEK 1: Basics – Variables, Data Types, Input/Output, Loops, Conditionals
# a = 5 
# b = 10
# a = b
# print(a)

# user = input("Enter something ")
# print(user)

# num = int(input("Enter a number :"))
# if num%2 == 0:
#     print("Num is even")
# else:
# n = int(input("Enter a number : "))
# for i in range(1,11):
#     table = n*i
#     print(f"{n} x {i} = ",table)

# num1 = int(input("Enter a number :"))
# num2 = int(input("Enter a number 2  :"))
# num3 = int(input("Enter a number 3  :"))
# if num1 >num2 or num1>num3:
#     print("Num 1 is greatest.")
# elif num2 > num1 or num2> num3:
#     print("Num 2 is greatest")
# elif num3 > num1 or num3> num2:
#     print("Num 3 is greatest")

# To convert Celsius (°C) to Fahrenheit (°F), use this formula
# °F=(°C×9//5​)+32
# celsius = int(input("Enter temperature in celsius °C:"))
# # fahrenheit = int(input("Enter temperature in fahrenheit : "))
# cel_to_feh = (celsius * 9//5)+32
# print("The conversion of celsius to fahrenhneit : ",cel_to_feh,"°F")


# 5*4*3*2*1
# n = int(input("Enter a number : "))
# factorial = 1
# for i in range(n,0,-1):
#     factorial = factorial*i
# print("The factorial of the given number is : " , factorial)


# monika
# user = input("Enter a string that consist multiple vowels : ")
# vowels = "aeiouAEIOU"
# vowel_count = 0
# for i in user:
#     if i in vowels:
#         vowel_count+=1
#     else:
#         continue
# print("The total vowels in the string is : ", vowel_count)
# user = input("Enter a string : ")
# rev = ""
# # for i in range(len(user)-1,-1,-1):
# #     rev += user[i]    
# print(rev)


# 123321 = 123321 : yes 
# user = input("Enter a string : ")
# rev = ""
# for i in range(len(user)-1,-1,-1):
#     rev += user[i]
# if user == rev:
#         print("palindrome")
# else:
#         print("NOt")
# n = int(input("Enter number : "))
# n_sum = 0
# for i in range(1,n+1):
#     n_sum+=i
# print(n_sum)

# import random 
# print("WE ARE GOING TO PLAY A GAME!")
# print("ENTER IF U WANT TO PLAY ! ")
# com_guess = random.randint(1,100)
# print(com_guess)
# a= -1
# while(a!=com_guess) :
#     user =  int(input("Enter any one number from 1 to 100 : "))
#     if user > com_guess:
#         print("Go lower!")
    # elif user<com_guess:
#         print("Go higher!")
#     else:
#         print("Perfect u win!")
# 2,3,5,
# prime_count = 0
# for i in range(2,101):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#         prime_count+=1
# print("Total prime numbers:",prime_count)

# year = int(input("Enter a number : "))
# if (year%100==0) and (year% 400==0) :
#     print("IT's a leap year!!")
# elif  (year%100!=0) and (year%4==0):
#     print("IT's a leap year!!")
# else:
#     print("IT's not a leap year !!")

# Fibonacci series ---> 0, 1, 2, 3, 5, 8, 13, 21, 34, ...
# n = int(input("Enter a number  : "))
# a = 0
# b =1
# for i in range (0,n):
#         c = a+b
#         a = b
#         b = c 
#         print(a)


# # Fibonacci series ---> 0, 1,1, 2, 3, 5, 8, 13, 21, 34, ...
# n = int(input("Enter a number till you want series : "))
# a =0
# b = 1
# for i in range(n):
#     c = a+b
#     a = b
#     b =c
#     print(a)



# 12 -> 1,2,3,4,6,,12 ,, 18-> 1,2,3,6,9,18 ,, common -> 1,2,3,6 ,, greatest -> 6 (greatest common divisor )
# num1 = int(input("Enter num1 : "))
# num2 = int(input("Enter num2 : "))
# GCD = 1
# for i in range(1,min(num1 , num2)+1):
#     if num1%i == 0 and  num2%i == 0:
#         GCD = i
# print(GCD)


# num1 = 12 , num2 = 18
# num1 = int(input("Enter num1 : "))
# num2 = int(input("Enter num2 : "))
# if num1> num2:
#     greatest = num1
# else:
#     greatest = num2
# for i in range(greatest,(num1*num2)+1):
#     if (i%num1 == 0) and (i%num2 ==0 ):
#         print("LCM is : ", i)
#         break


# vowels = aeiouAEIOU or other all consonants 
# char = a 
# vowels = "aeiouAEIOU"
# char = input("Enter any character : ")
# for i in char:
#     if i not in vowels:
#         print("It is a consonant")
#     else:
#         print("It is a vowels")


# 1234 = 1+2+3+4 , 4521 = 4+5+2+1 = 12
# num =input("Enter any number of digit : ")
# digi_sum = 0
# for i in num:
#     digi_sum+=int(i)
# print(digi_sum)

# l = [1,2,3,5,8,9,6,7,10,45]
# greatest= l[0]
# sec_lar = l[0]
# for i in range(1,len(l)):
#     if l[i]> greatest:
#         sec_lar = greatest
#         greatest = l[i]
#     elif l[i]>sec_lar and l[i]!=greatest:
#         sec_lar = l[i]
# print("The greatest number is:", greatest)
# print("The second largest number is:", sec_lar)

# 123654 =6 digit number h 
# num = (input("Enter a number : "))
# print(len(num))
# # Armstrong number wo hota hai bhai jisme digits ke cube (ya power of digits count) ka sum same hota hai number ke barabar.

# num = int(input("Enter a number : "))
# digit = len(str(num))
# sum = 0
# for i in str(num):
# for i in str(num): iska matlab hai — number ke har digit ko ek-ek karke loop me lena
#         sum+= int(i)**digit
# if sum == num :
#         print(num, "is an Armstrong number.")
# else:
#     print(num, "is not an Armstrong number.")

# NOTE : TRIANGLE PATTERN HUMESHA ODD MEI HI CHALATA HAI LIKE 1,3,5,7,9,11,ETC  
 
# n =  int(input("Enter number of space you want in first line : "))
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     print("*"*(2*i-1),end=" ")#for odd values..
#     print(" ")
#    *  
#   ***  
#  *****  
# *******  
#********* 

# n =  int(input("Enter number of star in last line u want : "))
# for i in range(1,n+1):
#     print("",end="")
#     print("*"*i,end="")
#     print(" ")
# *
# **
# ***
# ****
# n =  int(input("Enter number of star in last line u want : "))
# for i in range(1,n+1):  
#     print("*"*(n-i),end="")
#     print("",end="")
#     print(" ")
# ******* 
# ****** 
# ***** 
# **** 
# *** 
# ** 
# * 
# CALCULATOR APP :-)
# print("press 1 if you want to ADD.")
# print("press 2 if you want to SUBTRACT.")
# print("press 3 if you want to MULTIPLICATION.")
# print("press 4 if you want to DIVISION.")
# print("press 5 if you want to EXPONANTIAL.")
# user = int(input("Enter your choice : "))
# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# if user == 1:
#     print(f"The addition of {num1} and {num2} is : " ,num1+num2)
# elif user == 2:
#      print(f"The subtraction of {num1} and {num2} is : " ,num1-num2)
# elif user == 3:
#       print(f"The multiplication of {num1} and {num2} is : " ,num1*num2)
# elif user == 4:
#       print(f"The division of {num1} and {num2} is : " ,num1//num2)
     
# elif user == 5:
#       print(f"The exponantial of {num1} and {num2} is : " ,num1**num2)
# else:
#      print("Please enter your choice!")


# root x = 144
# x = 144**0.5
# n = int(input("Enter  number : "))
# print(n**0.5)

# l = [1,2,3,4,5,6]
# even_sum =0
# for i in l:
#     if i%2 ==0:
#         print(i)
#         even_sum+=i
# print(even_sum)

# n=8
# n = int(input("Enter a number :"))
# factor = 0
# for i in range(1,n+1):
#     if n%i == 0 :
#         factor+=1
#         print(i)
# if factor ==2:
#     print("It is a prime number.")
# else:
#     print("It is not a prime number.")
      
# print(factor) 
# Armstrong wala ques:   
# for i in range(1, 1001):
#     digits = str(i)
#     power = len(digits)
#     sum = 0
#     for d in digits:
#         sum += int(i) ** power
#     if i == sum:
#         print(i)
    
# for i in range(1,1001):
#     digit = str(i)
#     power =len(digit)
#     sum = 0
#     for d in digit:
#         sum+= int(d)**power 
#     if i == sum:
#         print(i)
# CH TO ascii
# ch = input("Enter a character: ")
# print("The ASCII value of", ch, "is", ord(ch))
# # ASCII TO CHARACTER
# num = int(input("Enter an ASCII value: "))
# print("The character for ASCII value", num, "is", chr(num))


# DECIMAL NUMBER LETE HAI USER SE : 10(EXAMPLE)
#10%2 = 5(quotient)-->0(remainder)-->"0"
#5%2 = 2(quotient)-->1(remainder)-->"01"
#2%2 = 1(quotient)-->0(remainder)-->"010"
#1%2 = 0(quotient)-->1(remainder)-->"0101"(ANS ISKA ULTA HOTA HAI)
# SO BINARY NUMBER IS ==> 1010 OF 10

# num = int(input("Enter a decimal number: "))
# binary = ""
# temp = num
# for i in range(num):
#     if temp > 0:
#         binary = str(temp % 2) + binary
#         temp //= 2
#     else:
#         break
# print("Binary number is:", binary) 


# n = int(input("Enter number : "))
# for i in range(1,n+1):
#    print("Number:", i, "Cube:", i**3)

WEEK 2: Functions, Lists, Tuples, Dictionaries, Sets
# def even(n):
#         if n%2==0:
#             print("The given number is even.")
#         else:
#             print("The given number is odd.")
# even(2)
# even(16)
# even(7)

# l = [1,2,3,45,5,6,7]
# sum = 0
# for i in l:
# #     sum+=i
# # print(sum)

# l =[2,5,4,7,8,9,6,2,4,5,5,5,45]
# # print(len(l))

# maximum = l[0]
# minimum =l[0]
# for i in range(len(l)):
#     if l[i] > maximum :
#         maximum = l[i]
#     elif l[i]<minimum and l[i]!=maximum:
#         minimum = l[i]
# print(minimum)
# print(maximum)

# l = [1,2,3,3,5,4,5,4,5,6,3,3,6,5,2]  
# l1 = []
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

# def reverse(list):
#     rev = []
#     for i in range(len(list)-1,-1 ,-1):
#         rev.append(list[i])
#     print(rev)
# reverse([1,2,3,4,4,5])#-6 # 5

# t = (1,2,3,6,5,4)
# for i in range(len(t)):
#     print(t[i])

# l = [1,2,3,6,5,4]
# t = tuple(l)
# l1 = list(t)
# print(l1)
# print(t)


# dict1 = {"monika" : 50,
#          "krishna" : 80,
#          "daksh" : 70,
#          "neelakshi" : 60,
#          }
# dict2 = {"gupta" : 50,
#          "goswami" : 70,
#          "yadav" : 60,
#          }
# for i in dict2:
#     dict1[i] = dict2[i]
# print(dict1)

# l = [1,2,3,2,14,5,6,4,5,20,2,3,4,5,8,5,12,2,3,6,5,4,7,8]
# d ={}
# for i in l:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
# {1:1,2:4,3:9}
# d ={}
# # for i in range(1,11):
# #     d[i] = i*i
# print(d)
# l = [1,2,4,5,8,7,9,6,3,2,1,4,5]
# for i in range(len(l)):         
#     for j in range(i + 1, len(l)):  
#         if l[i] > l[j]:         
#             l[i], l[j] = l[j], l[i]  
# print(l)

# d = {"monka":50,"krishna":80,"radhey":70}
# for i in d:
#     if d.keys() in d:
#         print("yes")
#     else:
#         print("no")

# s1 = {1,2,3,4,5,6,8,9,5,4}
# s2 = {12,45,63,21,7,8,96,5}
# print("UNION = ",s1|s2)
# # print("ITERSECTION",s1&s2)
# # print("DIFFERENCE BTW SI TO S2",s1.difference(s2))
# # print("DIFFERENCE BTW S2 TO S1",s2.difference(s1))

# d = {"a": 1, "b": 2, "c": 3}
# key = input("Enter key to check: ")
# if key in d:
#     print("Key exists!")
# else:
#     print("Key not found!")

# union = | intersection =& difference = -
# s1 = {1,2,3,6,5,4,5,4,2,3,1}
# s2 = {1,2,3,6,1}
# print("The union of the given sets : ",s1|s2)
# print("The intersection of the given sets : ",s1&s2)
# print("The diffrence of the given sets : ",s1-s2)
# l1 = [1,2,3,4,5,6]
# l2 = [1,2,5,6]
# def common (list(a) , list(b)):
#     for i in range(len(l1)):
#         for j in range(i+1,len(l2)):
#             if l1[i] in l2[j]:
#                 print
#                 print("commons are ",i)

# def common(a,b):
#     common = []
#     for i in range(len(l1)):
#         if l1[i] == l2[i]:
#             common.append(i)
#             print(common)
# l1 = [1,2,3,4,5,6]
# l2=  [1,2,5,6,7,5]
# common(l1,l2)


# def common():
#     for i in range(len(l1)):
#         if l1[i] in l2[i]:
#             print(l1[i])
# 5! = 5* 4 * 3 * 2 * 1
# def factorial(n):
#     factorial = 1
#     for i in range(n,0,-1):
#       factorial = factorial*i  
#     print(factorial)
# factorial(5)
# # monika = akinom
# def palindrome(user = ""):
#     rev = ""
#     for i in range(len(user)-1,-1,-1):
#         rev = rev+user[i]
#     if rev ==user:
#         print("Yes it's a palindrome")
#     else:
#         print("No its not a palindrome")  
#     print(rev)  

# palindrome(user="naman")

# def count(user = ""):
#     vowels = "aeiouAEIOU"
#     vowel_count = 0
#     char =""
#     for i in range(0,len(user)):
#         if user[i] in vowels:
#             vowel_count+=1
#             char+=user[i]
#     print("you entered : ",user)
#     print("total numbers of vowels are : ",vowel_count)
#     print("vowels characters are : ", char)
# count(user="krishna")
# count(user="monika")
# count(user="aeiou")
# # dict = {
# #     "name" : "monika",
# #     "language" : "python",
# #     "post"  : "data analysis",
# #     "package" : "15LPA"

# # }
# # for i in dict:
# #     print(i ,":" , dict[i])

# # def punctuation(user=""):
# #     punc = ",.':;"
# #     for i in range(0,len(user)):
#         if user[i] in punc:
#             del()
#         else:
#             continue
#     print(user)
# # user = "my name is : monika.and my father's name is : ajay gupta,we've a shop."
# punctuation(user="moni.ka!',")


# sci_marks = data[0:6, 2:] 
# print(sci_marks)
# for i in sci_marks :
#     if i < 75 :
#         sci_marks[i] = 0
#     else:
#         continue
# print(sci_marks)

# a = "hello iam a data scientist"
# print(a[0:5])
# s = input("Enter a string : ")
# reverse_str = ""
# for i in range(len(s)-1,-1,-1):
#     reverse_str = reverse_str + s[i]
# print(reverse_str)

# n = input("Enter a num : ")
# rev = ""
# invalid = "+-*/.!@#$%^&*()_=~`"
# for i in range(len(n)-1,-1,-1):
#     if i in invalid:
#         pass
#     rev+=n[i]
# print(rev)
#23
# n = input("Entera num : ")
# sum = 0
# for i in n:
#     sum = sum+int(i)
# print(sum)


# num1 = int(input("Enter a num"))
# num2 = int(input("Enter a num"))
# found = False 
# for i in range(num1,num2+1):
#     if num1>1:
#         count = 0 
#     for num in range(1,i+1):
#         if i%num==0:
#             count+=1
#     if count == 2:
#         print(i)
#         found = True

# if not found:
#     print("No prime numbers")

# num1, num2 = map(int, input().split())

# found = False 
# for i in range(num1,num2+1):
#     if num1>1:
#         count = 0 
#         for num in range(1,i+1):
#             if i%num==0:
#                 count = count+1
#             if count == 2:
#                 print(i)
#                 found = True

# if not found:
#     print("No prime numbers")

# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter a number: "))
# found =False 
# for num in range(num1,num2+1):
#     if num1>1:
#         count = 0 
#     for i in range(1,i+1):
#         if i%num == 0:
#             count = count+1
#         found = True
#         if count == 2: 
#                 print(i)
# n = input().replace('-', '')
# even_sum = 0
# odd_sum = 0
# for i in n : 
#     if int(i) % 2==0:
#         even_sum+=1
#     else:
#         odd_sum+=1
# print("Even:",even_sum)
# print("Odd:",odd_sum)

# n = input().replace('-', '')

# even_sum = 0
# odd_sum = 0

# for i in n:
#     if int(i) % 2 == 0:
#         even_sum += 1
#     else:
#         odd_sum += 1

# print("Even:", even_sum)
# print("Odd:", odd_sum)

# n1 = int(input())
# n2 = int(input())
# found = False 

# for i in range(n1,n2+1):
#     rev_digit = ""
#     for digit in str(i):
#         rev_digit = digit+rev_digit
#         if i == int(rev_digit):
#             print(i,end=" ")
#             found = True 


# if not found:
#     print("No palindrome numbers")

# monika
# s = input()
# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev = rev+s[i]
# print(rev)

#   n = int(input())
# for i in range(1,n+1):
#     if n>1:
#         count = 0 
#     for j in range(1,i+1):
#         if n%i == 0:
#             count+=1 
#     if count == 2:
#         print(i*i,end=" ")

# n = int(input())
# for i in range(1,n+1):
#     if n>1:
#         count = 0 
#     for j in range(1,i+1):
#         if n%j == 0:
#             count+=1 
#     if count == 2:
#         print(i*i,end=" ")



# num = int(input("Enter a number : "))
# digit = len(str(num))
# sum = 0
# for i in str(num):
# #for i in str(num): iska matlab hai — number ke har digit ko ek-ek karke loop me lena
#         sum+= int(i)**digit
# if sum == num :
#         print(num, "is an Armstrong number.")
# else:
    # print(num, "is not an Armstrong number.")
# 153 = 1+25+9 = 153 


# n = int(input("Enter a number: "))
# power = len(str(n))
# armstrng = 0
# for i in str(n):
#     armstrng += int(i)**power
# if armstrng == n :
#       print("Amrstrong")
# else:
#       print("not")

# n = int(input("Enter a number : "))
# sqrt = n**2
# print(f"the sqrt of your number is {sqrt}")
# 1,4,9,16...
# n = int(input())
# sqrt = ""
# for i in range(1,n+1):
#     for j in range(1,i+1):

# n = int(input())
# for i in range(n,-1,-1):
#     for j in range(1,i+1):
#         print("*",end = "")
#     print()

# str1 = input("Emter a str : ")
# str2 = input("Enter a str2 : ")
# # for i in str1:
# n1,n2 = map(int, input().split())
# for i in range(n1,n2+1):
#     if i>=0:
#         sqrt = int(i**0.5)
#         if sqrt*sqrt == i :
# #             print(i,end = " ")
# s = input()
# print(len(s))
# char_count = 0
# for i in range(0,len(s)):
#     char_count+=i 
# print(char_count)

# n = input()
# greatest = n[0]
# for i in range(1,len(n)):
#     if n[i]>greatest:
#         greatest = n[i] 
# print(greatest)


# 145
# a = int(input())
# while a>0:
#     print(a%10) 
#     a = a // 10
# print(a)

# a = int(input("Enter anumbet : "))
# while a>0:
#     print(a%10)
#     a = a//10
# a = int(input("Enter a number : "))
# sum = 0
# while a>0:
#     sum = sum + a%10
#     a = a//10
# print(sum)

# a = int(input("Enter a number : "))
# rev = 0
# while a>0:
#     rev = rev*10 + a%10
#     a = a//10
# print(rev)

# sum = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     sum = sum + n
# # print(sum)
# n = int(input())
# product = 1
# while n>0:
#     product = product*n%10
#     n = n//10
# print(product)

# n = abs(int(input()))
# copy = n
# sum = 0
# while n>0:
#     sum = sum + n%10
#     n = n//10
# if copy % sum==0:
#     print("Harshad Number")
# else:
#     print("Not Harshad Number")

# number guesing game
# tries ,count,






# # LOGIC BUILD BY ME
# import random
# computer_guess = random.randint(1,100)
# # print(computer_guess)
# tries = 0
# while True:
#     user_guess = int(input("guess the number : "))
#     tries+=1
#     if user_guess<computer_guess:
#         print("guess higher")
#     elif user_guess>computer_guess:
#         print("Guess lower")
#     elif user_guess == computer_guess:
#         print(f"You guess correct number in {tries} tries.")
#         break





# # STONE PAPER SCISSOR USING ELIF-LADDER
# import random
# com_score = 0 
# user_score = 0

# while True:
#     print(f"CURRENT SCORES : YOU --> {user_score} , COMPUTER --> {com_score}")
#     user = int(input("1 for stone, 2 for paper, 3 for scissors :   "))
#     com = random.randint(1,3)

#     if user == 1 and com == 3:
#         print("You won the match")
#         user_score+=1
#     elif user == 2 and com == 1:
#         print("You won the match")
#         user_score+=1
#     elif user == 3 and com == 2:
#         print("You won the match")
#         user_score+=1
#     elif user == com :
#         print("It's a draw")
#     else:
#         print("Computer won this round")
#         com_score+=1

#     if com_score == 5 :
#         print("COMPUTER WON THIS GAME")
#         break
#     elif user_score == 5:
#         print("CONGRATS YOU WON THIS GAME")
#         break


# def welcome_message(name):
#     print(f"Welcome, {name}!")

# welcome_message("Monika")

# def print_table(n):
#    for i in range(1,11):
#     tables = f"{n} X {i} = {n*i}"
#     return tables

# print(print_table(5))

# def count_digits(n):
#     if n == 0:
#         return 1
    
#     count = 0
#     while n > 0:
#         count += 1
#         n = n // 10
#     return count
# print(count_digits(12365458))
Monika954025







