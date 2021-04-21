# sum=0
# for i in range(1,6):
#  num=int(input("enter numbers"))
#  sum+=num%10




# print(sum)
# a=int(input("enter numbers"))
# for i in range(1,a):
#   if(i%5==0):
#       print(i)


# sum=0
# a=int(input("enter numbers"))
# for i in range(2,a):
#   sum=i
#   print(i)
#   if(sum/2==0):
#    print(i)
#
# print("end")


#
# count=0
# a=int(input("enter the number of times:"))
#
# for i in range(3,a):
#     num=int(input("enter a number:"))
#     if num==0:
#         break
#     elif(num%3==0 or num%7==0):
#         count+=1
# print(count)
c=0
min=101
max=1
sum=0
grade=0
while 0<=grade and grade<=100:

  grade=int(input("enter grade:"))
  if (grade <= 100 and grade >= 0):
    sum+=grade
    c+=1
    if(grade>=max):
        max=grade
    elif (grade<=min):
        min=grade
  else: print("erorr")
print(max,sum/c,max-min)