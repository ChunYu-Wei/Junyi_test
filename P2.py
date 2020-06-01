num = int(input())


arr = [0]*num

for i in range(num):
    arr[i] = i

cnt = num

for i in range(num):
    if(arr[i]%15 != 0 and (arr[i]%3 == 0 or arr[i]%5 == 0)):
        cnt = cnt - 1

print (cnt)
