# examples/tree_dfs_example.py

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Tree DFS (Depth First Search - 深さ優先探索)

Tree DFSは、木構造を探索するための基本的なアルゴリズムの一つです。
根ノードから始まり、可能な限り深く探索を進め、行き止まりに達したらバックトラックして別の経路を探索します。

基本的な考え方:
1. 根ノードから探索を開始します。
2. 現在のノードを処理します（処理のタイミングは順序によって異なります）。
3. 左の子が存在する場合、左の子に対して再帰的にDFSを実行します。
4. 右の子が存在する場合、右の子に対して再帰的にDFSを実行します。
5. スタック（再帰呼び出しスタックまたは明示的なスタック）を使用して、親ノードを追跡します。

探索の順序:
- Pre-order (先行順): 現在のノード -> 左の子 -> 右の子
- In-order (中間順): 左の子 -> 現在のノード -> 右の子 (主に二分探索木で使われる)
- Post-order (後行順): 左の子 -> 右の子 -> 現在のノード

Tree DFSが適している問題:
- 葉に近いノードを探索する必要がある問題。
- パスに関する問題（例: 根から葉までのパスの合計、特定の合計値を持つパスの探索）。
- 木の構造に関する問題（例: 木の高さ、直径）。

時間計算量:
- O(N): Nは木のノード数。各ノードを1回ずつ訪問するため。

空間計算量:
- 再帰的アプローチ: O(H) または O(log N) (平衡木の場合) から O(N) (歪んだ木の場合)。Hは木の高さ。再帰呼び出しスタックの深さに依存します。
- 反復的アプローチ (スタック使用): O(H) または O(log N) (平衡木の場合) から O(N) (歪んだ木の場合)。スタックに格納されるノードの最大数に依存します。
'''

# --- 再帰的な実装例 ---

def dfs_pre_order_recursive(root: TreeNode):
    """
    再帰的な先行順 (Pre-order) DFS
    Input: 木の根ノード (TreeNode)
    Output: 訪問したノードの値のリスト (List[int])
    """
    result = []
    def traverse(node):
        if not node:
            return
        result.append(node.val)  # 現在のノードを処理
        traverse(node.left)      # 左の子を探索
        traverse(node.right)     # 右の子を探索
    traverse(root)
    return result

def dfs_in_order_recursive(root: TreeNode):
    """
    再帰的な中間順 (In-order) DFS
    Input: 木の根ノード (TreeNode)
    Output: 訪問したノードの値のリスト (List[int])
    """
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)      # 左の子を探索
        result.append(node.val)  # 現在のノードを処理
        traverse(node.right)     # 右の子を探索
    traverse(root)
    return result

def dfs_post_order_recursive(root: TreeNode):
    """
    再帰的な後行順 (Post-order) DFS
    Input: 木の根ノード (TreeNode)
    Output: 訪問したノードの値のリスト (List[int])
    """
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)      # 左の子を探索
        traverse(node.right)     # 右の子を探索
        result.append(node.val)  # 現在のノードを処理
    traverse(root)
    return result

# --- 反復的な実装例 (スタック使用) ---

def dfs_pre_order_iterative(root: TreeNode):
    """
    反復的な先行順 (Pre-order) DFS (スタック使用)
    Input: 木の根ノード (TreeNode)
    Output: 訪問したノードの値のリスト (List[int])
    """
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)  # 現在のノードを処理
        # スタックはLIFOなので、右の子を先に入れる
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def dfs_in_order_iterative(root: TreeNode):
    """
    反復的な中間順 (In-order) DFS (スタック使用)
    Input: 木の根ノード (TreeNode)
    Output: 訪問したノードの値のリスト (List[int])
    """
    result: list[int] = []
    stack: list[TreeNode] = []
    current: TreeNode | None = root
    while current or stack:
        # 左端まで進む
        while current:
            stack.append(current)
            current = current.left
        # 左端に到達したら、スタックから取り出して処理
        current = stack.pop()
        result.append(current.val) # 現在のノードを処理
        # 右の子へ移動
        current = current.right
    return result

def dfs_post_order_iterative(root: TreeNode):
    """
    反復的な後行順 (Post-order) DFS (スタック使用)
    Input: 木の根ノード (TreeNode)
    Output: 訪問したノードの値のリスト (List[int])
    """
    if not root:
        return []
    result: collections.deque[int] = collections.deque() # 結果を逆順で追加するためdequeを使用
    stack: list[TreeNode] = [root]
    while stack:
        node: TreeNode = stack.pop()
        result.appendleft(node.val) # 結果の先頭に追加 (Pre-orderの逆順)
        # Pre-orderとは逆で、左の子を先にスタックに入れる
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return list(result)


# --- 例題1: Sum of Path Numbers (medium) ---
def sum_numbers(root: TreeNode) -> int:
    '''
    問題:
    根から葉までの各パスを数値として解釈し、それらすべての数値の合計を計算します。
    各パスは、根から葉までのノードの値を連結して形成されます。

    例:
        1
       / \
      2   3
    パス 1->2 は 12 と解釈されます。
    パス 1->3 は 13 と解釈されます。
    合計は 12 + 13 = 25 です。

    Input: 木の根ノード (TreeNode)
    Output: すべての根から葉へのパスの数値の合計 (int)

    時間計算量: O(N) - 各ノードを1回訪問します。
    空間計算量: O(H) - 再帰呼び出しスタックの深さ（木の高さ）。最悪O(N)。
    '''
    total_sum = 0

    def dfs(node, current_sum):
        nonlocal total_sum
        if not node:
            return

        current_sum = current_sum * 10 + node.val

        # 葉ノードに到達した場合
        if not node.left and not node.right:
            total_sum += current_sum
            return

        # 再帰的に子ノードを探索
        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

    dfs(root, 0)
    return total_sum

# --- 例題2: All Paths for a Sum (medium) ---
def path_sum(root: TreeNode, targetSum: int) -> list[list[int]]:
    '''
    問題:
    根から葉までのパスのうち、ノードの値の合計が指定された `targetSum` と等しくなるすべてのパスを見つけます。

    例:
    targetSum = 22
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1

    パス:
    [5, 4, 11, 2] (合計 22)
    [5, 8, 4, 5] (合計 22)

    Input: 木の根ノード (TreeNode), 目標合計値 (int)
    Output: 条件を満たすすべてのパスのリスト (List[List[int]])

    時間計算量: O(N^2) - 最悪の場合、N個のノードがあり、各パスの長さがNになる可能性があるため、パスのコピーにO(N)かかります。葉ノードの数をLとすると、より厳密には O(N*L) とも言えますが、Lは最悪N/2程度なのでO(N^2)となります。
    空間計算量: O(H) または O(N) - 再帰呼び出しスタックの深さ（木の高さ）と、パスを格納するための領域。最悪の場合、すべてのパスを保持する必要があるためO(N^2)になる可能性もあります（パスのリストの合計サイズ）。
    '''
    all_paths = []

    def find_paths_recursive(node, current_sum, current_path):
        if not node:
            return

        # 現在のノードをパスに追加し、合計を更新
        current_path.append(node.val)
        current_sum += node.val

        # 葉ノードであり、合計がtargetSumと一致する場合
        if not node.left and not node.right and current_sum == targetSum:
            # パスのコピーを結果に追加 (重要: current_pathは変更されるためコピーが必要)
            all_paths.append(list(current_path))
        else:
            # 再帰的に子ノードを探索
            find_paths_recursive(node.left, current_sum, current_path)
            find_paths_recursive(node.right, current_sum, current_path)

        # バックトラック: 現在のノードをパスから削除 (他のパスの探索のため)
        # このpop()は非常に重要です。これにより、現在のノードを含まない他の兄弟パスを正しく探索できます。
        current_path.pop()

    find_paths_recursive(root, 0, [])
    return all_paths


# --- 実行例 ---
if __name__ == '__main__':
    # テスト用の木を作成
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("--- Recursive DFS ---")
    print("Pre-order:", dfs_pre_order_recursive(root))  # Expected: [1, 2, 4, 5, 3, 6]
    print("In-order:", dfs_in_order_recursive(root))    # Expected: [4, 2, 5, 1, 3, 6]
    print("Post-order:", dfs_post_order_recursive(root)) # Expected: [4, 5, 2, 6, 3, 1]

    print("\n--- Iterative DFS ---")
    print("Pre-order:", dfs_pre_order_iterative(root))  # Expected: [1, 2, 4, 5, 3, 6]
    print("In-order:", dfs_in_order_iterative(root))    # Expected: [4, 2, 5, 1, 3, 6]
    print("Post-order:", dfs_post_order_iterative(root)) # Expected: [4, 5, 2, 6, 3, 1]

    # 例題1: Sum of Path Numbers
    #     1
    #    / \
    #   0   3
    root_sum = TreeNode(1)
    root_sum.left = TreeNode(0)
    root_sum.right = TreeNode(3)
    # Paths: 1->0 (10), 1->3 (13). Sum = 10 + 13 = 23
    print("\n--- Example 1: Sum of Path Numbers ---")
    print("Sum:", sum_numbers(root_sum)) # Expected: 23

    #     4
    #    / \
    #   9   0
    #  / \
    # 5   1
    root_sum2 = TreeNode(4)
    root_sum2.left = TreeNode(9)
    root_sum2.right = TreeNode(0)
    root_sum2.left.left = TreeNode(5)
    root_sum2.left.right = TreeNode(1)
    # Paths: 4->9->5 (495), 4->9->1 (491), 4->0 (40). Sum = 495 + 491 + 40 = 1026
    print("Sum:", sum_numbers(root_sum2)) # Expected: 1026


    # 例題2: All Paths for a Sum
    # targetSum = 22
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \    / \
    # 7    2  5   1
    root_path = TreeNode(5)
    root_path.left = TreeNode(4)
    root_path.right = TreeNode(8)
    root_path.left.left = TreeNode(11)
    root_path.left.left.left = TreeNode(7)
    root_path.left.left.right = TreeNode(2)
    root_path.right.left = TreeNode(13)
    root_path.right.right = TreeNode(4)
    root_path.right.right.left = TreeNode(5)
    root_path.right.right.right = TreeNode(1)
    targetSum = 22
    print("\n--- Example 2: All Paths for a Sum ---")
    print(f"Paths with sum {targetSum}:", path_sum(root_path, targetSum))
    # Expected: [[5, 4, 11, 2], [5, 8, 4, 5]]
