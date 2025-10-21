import sys
sys.stdin = open('input.txt')

# Base64 테이블
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

T = int(input())
for tc in range(1, T+1):
    encoded = input().strip()
    result = []
    
    # Base64 문자 4개씩 처리 (4문자 = 24비트 → 3바이트 문자)
    for i in range(0, len(encoded), 4):
        # 24비트 버퍼 (임시 저장 공간)
        buffer = 0
        
        # 6비트씩 4개를 버퍼에 넣기
        for j in range(4):
            char = encoded[i + j]
            value = base64_chars.index(char)  # 문자를 6비트 숫자로 변환
            buffer = buffer * 64 + value       # 버퍼에 추가 (64 = 2^6)
        
        # 버퍼에서 8비트씩 3개 꺼내기
        char1 = buffer // (256 * 256)    # 맨 앞 8비트 (256 = 2^8)
        char2 = (buffer // 256) % 256     # 중간 8비트
        char3 = buffer % 256              # 맨 뒤 8비트
        
        result.append(chr(char1))
        result.append(chr(char2))
        result.append(chr(char3))
    
    print(f"#{tc}", ''.join(result))