apple=[10,5,30]
print(apple)
print(apple[1])
print(apple[-1])
print(apple[-3])
#print(apple[4])
print("for iteration via access elements")
for i in apple:
    print(i)
print("after changed")
apple[1]=-100
print(apple)
apple[1:3]=(-10,19,-11)
print(apple)
apple[2]=34,37,8
print(apple[2])
print(apple[3])
print(apple[2])
print(apple[0])
print(apple[1])

apple[1:4]=(1,-3,4)
print(apple)