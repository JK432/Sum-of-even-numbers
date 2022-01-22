#Write a Python program to find the sum of even numbers from N given numbers
lst=[]
sum=0
n=int(input())
for i in range (0,n+1):
  w=int(input())
  lst.append(w)


for i in lst:
  if(i%2==0):
    sum=sum+i

print(sum)