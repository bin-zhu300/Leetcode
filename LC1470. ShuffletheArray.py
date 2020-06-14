
arr = [5,5,4]
k = 1


dic={}
for i in range(len(arr)):
    if arr[i] in dic.keys():
        dic[arr[i]]+=1
    else:
        dic[arr[i]]=1

temp=dic.values()
temp.sort()
while k>0:
    temp.pop
    k-=1
print(sum(temp))