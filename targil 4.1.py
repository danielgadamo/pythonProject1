from random import randint
num=randint(0,100)
# usernum=int(input("enter number:"))
# while(num!=usernum):
#     num=randint(0,10)
#     if(num>usernum):
#         print("hige")
#         print(num)
#     else:
#         print("low")
#         print(num)
# print("correct")
userans="false"
c=0
while(userans!="correct"):
   num = randint(0, 100)
   print(num)
   userans=input("enter your answer")
   c+=1

print(c)
print(num)













# num=int(input("enter number:"))
# num1=int(input("enter number:"))
#
# for i in range(num,num1,1):
#        if(i%2==0):
#           print(i)
#
# else:
#     for i in range(num1,num,1):
#         if(i%2==0):
#             print(i)
