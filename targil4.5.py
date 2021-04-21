# num_of_digits=int(input("enter the number"))
# num=0
# sum=1
# c=0
# for i in range(num_of_digits):
#     sum+=num
#     print(sum)
#     c+=1
#     if(c >=num_of_digits):
#         break
#     num+=sum
#     print(num)
#     c+=1
#     if (c >= num_of_digits):
#      break
# for i in range(1,5):
#   c=1*10**(i)
#   print(c)
# num=int(input("enter number:"))
#
# num1=""
# while num>0:
#     digit=num%10
#     num=num//10
#     num1+=str(digit)
# print(num1)
# print(int(num1)*2)

num=input(input("enter number:"))
num1=input(input("enter number1:"))
min=0
c=0
if(num1>num):
    min=num
    num=num1
    num1=min
while(num>num1):
    num-=num1
    c+=1
