path = [i + 20 for i in range(10)]
print(path)
node1 = path.index(22)
node2 = path.index(26)

# new path receives path, but swapps node1 + 1 and node 2
new_path = path.copy()
new_path.pop(node2)
new_path.insert(node1 + 1, path[node2])
print(new_path)