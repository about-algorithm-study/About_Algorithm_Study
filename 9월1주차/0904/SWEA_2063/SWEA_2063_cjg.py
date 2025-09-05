N = int(input())
arr = list(map(int, input().split()))

arr.sort()

middle = N//2
print(arr[middle])