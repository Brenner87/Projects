num=int(input())
result=[]
for i in range(num):
    a,b,c=map(int, input().split())
    my_sum=sum([int(j) for j in str(a*b+c)])
    result.append(my_sum)
print (*result)
