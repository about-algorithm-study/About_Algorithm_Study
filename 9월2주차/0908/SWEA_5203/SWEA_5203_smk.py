def my_run(lst):
    if len(lst) < 3:
        return False 
    
    sorted_lst = sorted(set(lst))
    
    for i in range(len(sorted_lst)-2):
        if sorted_lst[i] + 1 == sorted_lst[i + 1] and sorted_lst[i + 1] + 1 == sorted_lst[i + 2]:
            return True
    
    return False

def triplet(lst, n):
    if len(lst) < 3:
        return False
    
    if lst.count(n) >= 3:
        return True
    
    return False

T = int(input())

for t in range(1, T + 1):
    nums_lst = list(map(int, input().split()))

    per1 = []
    per2 = []

    winner = 0

    for i in range(12):
        j = i // 2
        if i % 2 == 0:
            per1.append(nums_lst[i])
            if my_run(per1) or triplet(per1, nums_lst[i]):
                winner = 1
                break
        else:
            per2.append(nums_lst[i])
            if my_run(per2) or triplet(per2, nums_lst[i]):
                winner = 2
                break
    
    print(f"#{t} {winner}")