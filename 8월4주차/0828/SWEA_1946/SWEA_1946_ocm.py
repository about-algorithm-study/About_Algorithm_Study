import sys
sys.stdin = open('input (1).txt')

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    data = []
    for _ in range(N):
        apb,ea = input().split()
        data.append((apb,int(ea)))
    # [('A', 10), ('B', 7), ('C', 5)]
    # [('B', 20), ('C', 19), ('E', 18), ('R', 17)]
    lst=[]
    for i in range(N):
        lst.append(data[i][0] * data[i][1]) #['AAAAAAAAAA', 'BBBBBBB', 'CCCCC']

    s = ''.join(lst) #'AAAAAAAAAABBBBBBBCCCCC'

    print(f'#{tc}')
    for i in range(0,len(s),10): #range(0,22,10)
        print(s[i:i+10]) #s[0:10] s[10:20] ...