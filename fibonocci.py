n=int(input("enter the number"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    
    
    
    
    
    
n=int(input("enter the number of terms"))
a,b = 0,1
for i  in range(n):
    print(a,end=" ")
    temp_a = a
    a=b
    b=temp_a+b
      