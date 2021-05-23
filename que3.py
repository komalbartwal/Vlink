Number = int(input(" Please Enter any Number: "))

for i in range(2, Number + 1):
    if(Number % i == 0):
        isprime = 2
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                isprime = 0
                break
            
        if (isprime == 2):
            print(" %d is a Prime Factor of a Given Number %d" %(i, Number))
        if (isprime == 1):
            print("invalid number")
'''
n=int(input("enter a prime number:"))
i=1
while(i<=number):
     count=0
     if(number%i==0):
         j=1
         while(j<=i):
             if(i%j==0):
                 count=count+1
                 j=j+1
                 if(count==2):
                     print("%d is a Prime Factor of a given number %d"%(i,number))
    
'''
