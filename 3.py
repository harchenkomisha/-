n = int(input())
for i in range(1,n + 1):
    y = 1
    for _ in range(n-1,i+1):
        print(y, end=' ')
        y += 1
    print()