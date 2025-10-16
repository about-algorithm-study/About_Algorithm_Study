import sys
sys.stdin = open('input.txt')

callender = {"1":31, "2":28, "3":31, "4":30, "5":31, "6":30,
             "7":31, "8":31, "9":30, "10":31, "11":30, "12":31 }

T = int(input())
for tc in range(1, 1+T):
    MX,DX,MY,DY = map(str,input().split())
    result = (-int(DX) + 1) + int(DY) + callender[MX]
    month = []
    for i in range(int(MX)+1,int(MY)):
        month.append(str(i))

    if len(month) > 0:
        for j in range(len(month)):
            result += callender[month[j]]
    else:
        result -= callender[MX]
    print(f'#{tc}',result)