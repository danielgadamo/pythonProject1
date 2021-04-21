#
# for i in range(5):
#     num=int(input("enter number"))
#     if(i==0):
#         min = num
#     for j in range(2,num,1):
#         if num % j == 0:
#            print("lo rishoni")
#            break
#     else:
#      print('rishoni')
#      if(num<min):
#         min=num
# print(min)

# num=int(input("enter number"))
# c=0
# new_num=0
# num2=num
# while(num>0):
#
#     num=num//10
#     c+=1
#
# for i in range(c,0,-1):
#     new_num= new_num+(num2%10)*(10**(i-1))
#     num2=num2//10
#     print(new_num)
# print(new_num*2)

num=int(input("enter number"))
num1=0
while(num>0):
    num1=(num%10)*10+num1*10
    num=num//10
    if(num<10):
      print(num1+num)
      break
