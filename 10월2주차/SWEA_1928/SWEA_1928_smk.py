T = int(input())
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

for t in range(1, T + 1):
    my_str = input()
    bit6_str = ""

    for i in my_str:
        now = table.index(i)
        now_bits = f"{now:06b}"

        bit6_str += now_bits

    byte_lst = []
    decoded = ""

    for j in range(0, len(bit6_str), 8):
        byte = bit6_str[j:j+8]
        byte_lst.append(byte)    
    
    for b in byte_lst:
        deco = chr(int(b, 2))
        decoded += deco

    print(f"#{t} {decoded}")
    
