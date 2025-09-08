T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def backtracking(index, current_sum, selected_count):
        if index == N:
            if selected_count > 0 and current_sum == K:
                return 1
            else:
                return 0

        count = backtracking(index + 1, current_sum, selected_count)

        count += backtracking(index + 1, current_sum + A[index], selected_count + 1)

        return count

    result = backtracking(0, 0, 0)

    print(f"#{tc} {result}")
