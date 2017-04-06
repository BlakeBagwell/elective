str = '1,,234,,,4   ,5,, 6,,103,  5'

arr = str.split(',')
highest = 0

for i in range(len(arr)):
    arr[i] = arr[i].strip()


for j in range(len(arr)):
    if len(j) != 0:
        n = int(j)
        if n > highest:
            highest = n

print(highest)
