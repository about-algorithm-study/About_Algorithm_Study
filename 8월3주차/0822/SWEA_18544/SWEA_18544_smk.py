V = int(input())

num_lst = list(map(int, input().split()))

tree = [[] for _ in range(V+1)]

for i in range(0, len(num_lst), 2):
    tree[num_lst[i]].append(num_lst[i + 1])


def preorder(tree, node):
    print(node, end=" ")
    for child in tree[node]:
        preorder(tree, child)

start = min(num_lst)

preorder(tree, start)