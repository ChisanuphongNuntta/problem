#Binary Tree Nodes
def node_type(nodes, parents, value):
    if value not in nodes:
        return 'Not exist'
    if parents[nodes.index(value)] == -1:
        return 'Root'
    if value not in parents:
        return 'Leaf'
    return 'Inner'

print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5))