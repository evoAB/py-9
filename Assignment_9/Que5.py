n=int(input("Enter input "))
if(n%2==0):
    n-=1
while 2*n>0:
    print(n,end=' ')
    n-=2