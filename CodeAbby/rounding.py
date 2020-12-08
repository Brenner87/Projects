result=[]
for i in range(int(input())):
    a,b=map(float,input().split())
    answer = int(a / b + 0.5) if a/b>=0 else int(a/b-0.5)
    result.append(answer)
print (*result)