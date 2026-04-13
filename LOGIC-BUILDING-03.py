# LISTS 
# l = [10,20,30,40,50]
# sum = 0
# for i in l:
#     sum+=i
# print("sum : ",sum)
# print("avg : ",sum/len(l))

# a = [10,20,3,5,1,4,2,3,6,50]
# greatest = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i]>greatest:
#         greatest = a[i]
#         index = i
# print(f"greatest {greatest} at index {index}")

# a = [10,20,3,5,1,4,2,3,6,50,51]
# greatest = a[0]
# sec_greatest = a[0]
# greatest_index = 0
# sec_greatest_index = 0

# for i in range(len(a)):
#     if a[i]>greatest:
#         sec_greatest = greatest
#         greatest = a[i]
#         sec_greatest_index = greatest_index
#         greatest_index = i
#     elif a[i] > sec_greatest_index:
#         sec_greatest_index = i

        
# print(f"greatest {greatest} at {greatest_index}, second greatest {sec_greatest} at {sec_greatest_index}")

# a = [10,20,3,5,1,4,2,3,6,50,51]

# max1 = a[0]
# max2 = a[0]
# index1 = 0
# index2 = 0
# for i in range(len(a)):
#     if a[i]> max1:
#         max2 = max1
#         max1 = a[i]
#         index2 = index1
#         index1 = i
#     elif a[i]> max2:
#         max2 = a[i]
#         index2 = i

# print(f"greatest {max1} at {index1}, second greatest {max2} at {index2}")

# l = [15,2,4,5,6,7,8,9,10]
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         continue
#     else:
#         print("List is not sorted")
#         break
# else:
#     print("List is sorted")
# # rotation of elements ---> rightward
# l = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(l)-1,0,-1):
#     l[i],l[i-1] = l[i-1],l[i]

# print(l)
# # rotation of elements ---> leftward
# l = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(l)-1):
#     l[i],l[i+1] = l[i+1],l[i]

# print(l)

# # rotation of elements ---> k-time
# k =int(input("How many time you want to rotate : "))
# l = [1,2,3,4,5,6,7,8,9,10]

# for i in range(k):
#     for i in range(len(l)-1):
#         l[i],l[i+1] = l[i+1],l[i]

# print(l)

# k =int(input("How many time you want to rotate : "))
# l = [1,2,3,4,5,6,7,8,9,10]

# for i in range(k):
#     for i in range(len(l)-1,0,-1):
#         l[i],l[i-1] = l[i-1],l[i]

# print(l)

# a =[1,2,3,4,5,6,7,89]
# rev = []
# for i in range(len(a)-1,0,-1):
#     rev.append(a[i])
# print(rev)

# a =[1,2,3,4,5,6,7,89]
# b = len(a)-1
# for i in range(len(a)//2):
#     a[i],a[b] = a[b],a[i]
#     b = b-1
# print(a)

# linear search : search an element in the given list by one by one

# search  = int(input("Enter a number you want to search : "))
# l = [10,20,30,40,50,60,70]
# for i in range(len(l)-1):

#     if l[i] == search:
#         print(f"Yes this number is in a list at this {i}")
#         break
# else:
#     print("No,this number not found in the list")

# BINARY SEARCH : efficiently search for an element in a sorted list using the divided and conquer approach 


# l = [10,20,30,40,50,60,70]
# search = int(input("Enter you a number ou want : "))
# start = 0
# last = len(l)-1
# mid = (start+last)//2

# while start <= last:
#     if l[mid] == search:
#         print(f"you number is found at index {mid}")
#         break 
#     elif l[mid] < search:
#         start = mid+1
#         mid = (start+last)//2

#     elif l[mid]> search:
#         last = mid-1
#         mid = (start+last)//2

# else:
#     print("no number found")


# bubble sort : 
# l = [12,23,145,544,126,48,1452,0,452,1522,452,14]
# for j in range(len(l)-1):
#     for i in range(len(l)-1-j):
#         if l[i]>l[i+1]:
#             l[i],l[i+1] = l[i+1],l[i]
# print(l)

# selection sort 
# l = [12,23,145,544,126,48,1452,0,452,1522,452,14]
# for i in range(len(l)-1):
#     j = i+1
#     min = i

#     for k in range(j,len(l)):
#         if l[k] < l[min]:
#             min = k

#     l[i],l[min] = l[min],l[i]

# print(l)

# QUESTION OF LIST : 
# l = [10,20,30,40,50,60]
# for i in range(len(l)):
#     if len(l)%2 == 0:
#         for j in range(0,len(l)//2):
#             print(l[j])
    
#     elif len(l)%2 != 0:
#         for j in range(0,(len(l)//2)-1):
#             print(l[j])

# print(l)

# l = [10,20,30,40,50,60]

# if len(l) % 2 == 0:
#     for j in range(0, len(l)//2):
#         print(l[j])
# else:
#     for j in range(0, len(l)//2 + 1):
#         print(l[j])
# elements = [10,20,30,40,50,60,70] remove = 30
# n = int(input("Entr a number of element you want : "))
# elements = list(int(input("Enter the element you want :" )))
# remove = int(input("Enter a number you want to remove: "))
# start = 0
# last = len(elements)-1
# mid = (start+last)//2
# while start<=last:
#     if elements[mid] == remove:
#         elements[mid].remove
#         break
#     elif elements[mid] > remove:
#         start = mid+1
#         mid = (start+last)//2
#     elif elements[mid]< remove:
#         last = mid-1
#         mid = (start+last)//2

# else:
#     print("no number found")
        

# elements = list(map(int, input("Enter elements separated by space: ").split()))
# remove = int(input("Enter a number you want to remove: "))

# start = 0
# last = len(elements) - 1

# while start <= last:
#     mid = (start + last) // 2

#     if elements[mid] == remove:
#         elements.pop(mid)
#         print("Number removed")
#         break

#     elif elements[mid] > remove:
#         last = mid - 1

#     else:
#         start = mid + 1

# else:
#     print("No number found")

# print(elements)


# def average_of_list_elements(numbers):
#    sum = 0
#    for i in range(len(numbers)):
#     sum += numbers[i]

#     return (sum/len(numbers))
   
# average_of_list_elements(10)


# l = [10,20,30,40,50,60,7]
# print(l)
# sum = 0
# count = 0
# for i in range(len(l)):
#     sum+=l[i]
# avg = sum / len(l)

# count = 0
# for j in range(len(l)):   
#     if l[j] > avg:
#         count+=1
# print(avg)
# print(count)
    

# print("chl gya")
# l =  [12,1,4,5,1]
# product = 1
# for i in range(len(l)):
#     product = product*l[i]

# print(product)

# list1 = [10,20,30]
# list2 = [40,50,60]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         merge = list1[i] + list2[j]
#     print(merge)


# tuple
# remove = 30
# tuple1 = (10,20,30,40,50)
# remove = 30
# updated = ()
# for i in tuple1:
#     updated.append(i)
#     if i == remove:
#         break
# s1 = {10,20,30,40}
# s2 = {30,40,50,60}
# s1>=s2
# s2<=s1

# print(s2)
# print(s1)

# def remove_duplicates_using_set(n, elements):
#     s = set(elements)
#     return list(s)
# l = [1,1,1,1,2,2,3,3,4,4,5,6,6,6,5,2,2,1,1,12,3,3,2,1,2,2,1]
# d = {}
# for i in l:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i] = 1
# print(d)
# print(d.keys())

# jweles = "aA"
# sotnes = "aAAbbbb"
# d = {}
# for i in sotnes:
#     if i in  d.keys():
#         d[i]+=1
#     else:
#         d[i] = 1
# count = 0
# for i in d.keys():
#     if i in jweles:
#         count+=d[i]

# print(count)
# print(d)

# sentence = "thequickbrownfoxjumpsoverthelazydog"
# d = {}
# for i in sentence:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i] = 1
# print(d)
# print(len(d.keys())
# nums = [1,2,3,2]
# d = {}
# for i in nums :
#         if i in d.keys():
#             d[i]+=1
#         else:
#             d[i] = 1
# print(d)
# # 1: 1, 2: 2, 3: 1}
# sum = 0
# for i in d.keys():
#     if d.values == 1:
#         sum+=d[i]
# print(sum)

# names = ["Mary","John","Emma"]
# heights = [180,165,170]

# # d = {}

# for i in range(len(names)):
#     d[heights[i]] = names[i]

# sort = sorted(d.keys(), reverse=True)

# output = []

# for j in sort:
#     output.append(d[j])

# print(output)

# s1 = "aabbcc"
# s2 = "baccab"
# if len(s1) == len(s2):
#     d = {}
#     for i in s1:
#         if i in d.keys():
#             d[i]+=1
#         else:
#             d[i] = 1 
#     for i in s2:
#         if i in d.keys():
#             d[i]-=1
#         else:
#             print("An extra element was found")
#     for i in d:
#         if d[i]!= 0:
#             print("Sorry your element are not same")
#             break
#     else:
#         print("Your strings are same")
# else:
#     print("Sorry the length is not same")

# arr = [1,1,1,1,1,1,1,1,1,7,7,7,7,7,7,1,2,3,4,5,2,1,2,3,2,1,4,51,2,1,2,4,1,0,2,2,2,2,1,1,1,4,41,0,0,0,2,4,2,3,6,6,4,5,2,2,1,1,0,2,1]
# d = {}
# for i in arr:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]= 1 
# print(d)
# for i in d.keys():
#     if d[i] > 2:
#        print(i)

# l1 =[1,2,3,4,5,6]
# l2 =[1,2,8,9,5,6]
# d = {}
# for i in l1:
#     if i in d.keys():
#         d[i]+=1
#     else: 
#         d[i] = 1
# j = []
# for i in d.keys():
#     if i in l2:
#         j.append(i)

# print(j)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6}
# for i in dict1:
#     for j in dict2:
#         if i == j:
#             print(list(i))



# def count_pairs(d):
#     count = 0
#     for i in d:
#         count+=1
#     # print(count)
#         # count_pair = 0
#         if type(d[i]) == dict:
#             count += count_pairs(d[i])
#     return count
# d = {1:"monika",2:{3:"krishna",4:"kirti"},5:"shikha"}
# print(count_pairs(d))
# print(len(key))



# l =[1,2,3,5,4]
# l2 =["moniks" , "lrijd"]
# comb = zip(l,l2)
# print(dict((list(comb))))

# file = open(r"C:\Users\Kirti Gupta\Desktop\data_science\main.py","r")
# print(file.read())

# create = open("monika.txt","a")
# create.write("hye everyone,happy learning , enjoying learning")
# print(create)


# def factory(material,zips,pockets):
#     pass

# factory()

# n = int(input("Enter anumber :"))
# fact = 1
# for i in range(n,1,-1):
#     fact = fact*i
# print(fact)

# s = input("Enter a string : ")
# vowels = "aeiouAEIOU"
# vol_count = 0
# for i in s :
#     if i in vowels:
#         vol_count+=1
# print(vol_count)

# s = input("Enter a string : ")
# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# print(rev)

# s = input("Enter a string : ")
# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# if rev == s:
#     print("it's a palindrom")
# else:
#     print("It's not")
# print(rev)
# prime_count = 0
# for i in range(2,101):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#         prime_count+=1
# print("Total prime numbers:",prime_count)

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
# #         break

# # n = input("num : ")
# # digit_sum = 0
# # for i in n :
# #     digit_sum+=int(i)
# # print(digit_sum)

# # l = [1,2,3,5,8,9,6,7,10,45]
# # greatest= l[0]
# # sec_lar = l[0]
# # for i in range(1,len(l)):
# #     if l[i] > greatest:
# #         sec_lar = greatest
# #         greatest = l[i]
# #     elif l[i]>sec_lar and l[i]!=greatest:
# #         sec_lar = l[i]

# # num = int(input("Enter a decimal number: "))
# # binary = ""
# # temp = num
# # for i in range(num):
# #     if temp > 0:
# #         binary = str(temp % 2) + binary
# #         temp //= 2
# #     else:
# #         break
# # print("Binary number is:", binary) 
# # n =  int(input("Enter number of star in last line u want : "))
# # for i in range(1,n+1):
# #     print("",end="")
# #     print("*"*i,end="")
# #     print("")
# #     n =  int(input("Enter number of star in last line u want : "))
# # for i in range(1,n+1):
# #     print("",end="")
# #     print("*"*i,end="")
#     # print(" ")


# l = [1,2,3,3,5,4,5,4,5,6,3,3,6,5,2]  
# unique =list(set(l))
# print(unique)


# l = [0,20,3,0,4,0,5,0,6,0,3,0,2 ]

# maximum = l[0]
# minimum =l[0]
# for i in range(len(l)):
#     if l[i] > maximum :
#         maximum = l[i]
#     elif l[i]<minimum and l[i]!=maximum:
#         minimum = l[i]
# print(minimum)
# print(maximum)

# t = (1,2,3,4,5,6,7)
# for i in range(len(t)):
#     print(t[i])





# # student resgistration system :
# class Student:
#     def __init__(self,name,age,number,blood_group):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.blood_group = blood_group
#     def show_details(self):
#         print("Name of the student is : ",self.name)
#         print("Age of the student is :",self.age)
#         print("Number of the student is :",self.number)
#         print("Blood group of the student is :",self.blood_group)


# regisration1 = Student("Monika",18,9540525632,"A+")
# regisration2 = Student("Krish",28,95402344145,"B+")
# regisration3 = Student("Kirti",19,95402341123,"A+")

# print()
# print(f"STUDENT 1 REGISTER NAMED {regisration1.name}")
# regisration1.show_details()
# print()

# print(f"STUDENT 2 REGISTER NAMED {regisration2.name}")
# regisration2.show_details()
# print()

# print(f"STUDENT 3 REGISTER NAMED {regisration3.name}")
# regisration3.show_details()
# print()


# Student Registration System

# class Student:
#     def __init__(self, name, age, number, blood_group):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.blood_group = blood_group

#     def show_details(self):
#         print(f"  Name        : {self.name}")
#         print(f"  Age         : {self.age}")
#         print(f"  Number      : {self.number}")
#         print(f"  Blood Group : {self.blood_group}")

#     def __str__(self):
#         return f"Student({self.name}, Age: {self.age})"


# registration1 = Student("Monika", 18, 9540525632, "A+")
# registration2 = Student("Krish", 28, 95402344145, "B+")
# registration3 = Student("Kirti", 19, 95402341123, "A+")

# students = [registration1, registration2, registration3]

# for i, student in enumerate(students, start=1):
#     print(f"\n{'='*35}")
#     print(f"  STUDENT {i} REGISTERED : {student.name}")
#     print(f"{'='*35}")
#     student.show_details()

# print(f"\n{'='*35}")
# print("  All students registered successfully!")
# print(f"{'='*35}\n")

