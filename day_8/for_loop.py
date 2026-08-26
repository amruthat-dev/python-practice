for i in range (1,11):
    print (i , end=" ")


for i in range(10,0,-1):
    print( i )

for i in range(2,21,2):
    print( i )

for i in range(1,20,):
    if i % 2 !=0:
        print(i)


num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num}X{i}={num*i}") 