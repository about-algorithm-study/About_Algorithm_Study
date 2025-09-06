T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort()

    middle = arr[1:-1]
    
    avg = sum(middle) / len(middle)
    
    result = round(avg)

    print(f"#{tc} {result}")