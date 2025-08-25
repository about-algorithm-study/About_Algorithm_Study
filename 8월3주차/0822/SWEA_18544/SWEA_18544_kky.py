V = int(input())

nodes = list(map(int, input().split()))

tree = {}
children = set()

for i in range(1, V+1): # 트리 구조 초기화 , tree = {1: [None, None], 2: [None, None], 3: [None, None], 4: [None, None], 5: [None, None], 6: [None, None], 7: [None, None]}
    tree[i] = [None, None]

for i in range(0, len(nodes), 2): # 0, 2, 4, 6...으로 2씩 증가
    parent = nodes[i] # 부모 - 자식 쌍 추출
    child = nodes[i+1]
    children.add(child) # 자식 노드를 집합에 추가

    if tree[parent][0] is None: # 왼쪽 자식이 비어있으면 추가, 아니면 오른쪽에 추가
        tree[parent][0] = child
    else:
        tree[parent][1] = child

# 루트 노드 찾기(자식이 아닌 노드)
root = None
for i in range(1, V+1):
    if i not in children:
        root = i
        break

# 전위 순회 함수
def preorder(node):
    if node is None:
        return

    print(node, end=' ')
    preorder(tree[node][0]) # 왼쪽 자식
    preorder(tree[node][1]) # 오른쪽 자식

preorder(root)