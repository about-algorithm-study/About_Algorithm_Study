count = 0


def recursion(s, l, r):
    global count
    count += 1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


T = int(input())

for tc in range(1, T + 1):
    count = 0
    string = input()
    result = 0
    if isPalindrome(string) == 0:
        print(result, count)
    else:
        result = 1
        print(result, count)

"""
헷갈리기 쉬운 부분: count 변수를 전역변수로 선언하고 재귀함수에서 이를 증가시키는 부분이 있습니다.

이 때 재귀 호출이 일어날 때마다 count가 증가하므로, 최종적으로 몇 번의 비교가 이루어졌는지를 알 수 있습니다.

하지만 count 변수를 함수 내부에서 초기화하지 않으면, 이전 테스트 케이스의 값이 남아있을 수 있습니다.
"""
