import sys
sys.stdin = open('input.txt')

decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/']
T = int(input())
for tc in range(1, 1+T):
    S = input()
    bin_list  = ""
    for i in S:
        change = decode.index(i)
        bin_change = format(change,'06b') #06b 이진수로 바꾸고 부족한자리 6자리까지 0으로 채워라
        bin_list += bin_change
    result=''
    for i in range(0,len(bin_list),8):
        ch = int(bin_list[i:i+8],2)
        result += chr(ch)
    print(f'#{tc}',result)

'''
from base64 import b64decode

T = int(input())

for tc in range(1, T + 1):
    word = input()
    res = b64decode(word).decode('UTF-8')
    print(f'#{tc}',res)
'''