def binary_search_with_path(arr, target):
    left, right = 0, len(arr) - 1
    directions = []

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True, directions
        elif arr[mid] < target:
            directions.append("right")
            left = mid + 1
        else:
            directions.append("left")
            right = mid - 1

    return False, directions


def is_alternating(directions):
    if len(directions) <= 1:
        return True

    for i in range(1, len(directions)):
        if directions[i - 1] == directions[i]:
            return False

    return True


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()

    count = 0
    for target in B:
        found, directions = binary_search_with_path(A, target)

        if found and is_alternating(directions):
            count += 1

    print(f"#{tc} {count}")
