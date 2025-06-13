import sys
from collections import Counter

def solution(tree_list: list) -> None:
    most_of_tree = Counter(tree_list)
    total = len(tree_list)

    for name in sorted(most_of_tree.keys()):
        percent = (most_of_tree[name] / total) * 100
        print(f"{name} {percent:.4f}")

tree_list = []
for line in sys.stdin:
    name = line.strip()
    if name:
        tree_list.append(name)

solution(tree_list)