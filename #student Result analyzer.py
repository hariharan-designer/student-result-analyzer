#student Result analyzer

name=input('enter student name')

mark1=int(input("enter tamil mark"))
mark2=int(input("enter eng mark"))
mark3=int(input("enter maths mark"))

total=mark1+mark2+mark3
average= total /3

print ('\n------Result-----')
print('Name:',name)
print("total:",total)
print("average",average)

if mark1<35 or mark2<35 or mark3<35:
    print('status:fail')
else:
    print('status pass')

if average >=90:
    print('grade:a+')
elif average>=75:
    print("gradeA")
elif average>=60:
    print('grade:A')
else:
    print("grade:C")