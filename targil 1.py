# sum=0
# for i in range(1,6):
#     a=int(input("enter numbers"))
#     sum+=a
# print(sum/5)

# c=0
# sum=0
# for i in range(1,7):
#     a=int(input("enter numbers"))
#     if a%2==0 :
#      sum+=a
#      c+=1
# print(sum/c)


# c=0
# sum=0
# for i in range(10,100):
#     if i%10==7 :
#      print(i)

#
# sum=0
# for i in range(10,100):
#     if i%10==0 :
#       print(i)
#       sum+=i
# print(sum)




# sum=0
# c=0
# a=int(input("enter number:"))
#
# for i in range(a):
#  grade=int(input("enter grades"))
#  if 0>grade or grade>100:
#     print("error")
#     break
#  if grade>=60:
#   sum+=grade
#   c+=1
# print("the average is",sum/c)



sum=0
sum1=0
c=0
c1=0
a=int(input("enter number:"))

for i in range(a):
 grade=int(input("enter grades"))
 if 0>grade or grade>100:
    print("error")
    break
 if grade>=60:
  sum+=grade
  c+=1
 else:
     sum1+=grade
     c1+=1

print("the averages is", sum/c, sum1/c1)