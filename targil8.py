# pas1=input("enter the password:")
# c=0
# for i in range(1,6):
#  pas = input("enter the password:")
#  c+=1
#  if(pas1==pas):
#      print("correct password")
#      break
#
#  else: print("uncorrect password")
#
# if(c==5):
#     print("to much chries")

# num=int(input("enter a number"))
# c=1
# while(num>9):
#     num=num//10
#     c+=1
# print(c)

# 3.
# num=int(input("enter a number"))
# sum=0
# while(num>0):
#     sum+= num % 10
#     num=num//10
#
# print(sum)

# targil rishoni
# c=0
# num=int(input("enter number"))
# for i in range(2,num,1):
#     if(num%i==0):
#         print(" lo rishoni")
#         c+=1
#         break
#         c+=1
# if(c==0):
#  print("rishoni")

# 3.
# num=int(input("enter number"))
# min=num
# while num!=0:
#     num = int(input("enter number"))
#
#     if(0<num):
#
#      if(num<min):
#         min=num
#
# print(min)
# 5.
# num=int(input("enter a number"))
# while(num>9):
#     num=num//10
# print(num)
#
#
#
#
#
#5.
# max=0
# c=0
# for i in range(7):
#     num = int(input("enter number"))
#     if(num>max):
#         max=num
#         c=i
#     if(num<0):
#         if(num>max2):
#           max2=num
#           c=i
# print(c)
# 8.
c=1
min=0
num = int(input("enter number"))
for i in range(2,num,1):
    while c < 5:


     if(num%i==0):
       if(num<min):
        min=num

     num = int(input("enter number"))
     c+=1