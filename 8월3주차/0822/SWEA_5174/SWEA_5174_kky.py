T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))

    tree = {}
    children = set()

    for i in range(1, E + 2):
        tree[i] = [None, None]

    for i in range(0, len(nodes), 2):
        parent = nodes[i]
        child = nodes[i+1]
        children.add(child)

        if tree[parent][0] is None:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

    def count_sub_tree(node):
        if node is None:
            return 0

        else:
            return 1 + count_sub_tree(tree[node][0]) + count_sub_tree(tree[node][1])

    result = count_sub_tree(N)

    print(f"#{tc} {result}")