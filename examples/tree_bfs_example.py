# coding: utf-8
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
7. Tree BFS (木の幅優先探索)

このパターンは、幅優先探索 (BFS) 技術に基づいて木を走査し、キューを使用して、
次のレベルに進む前に現在のレベルのすべてのノードを追跡します。
木をレベルごとに走査する問題は、このアプローチを使用して効率的に解決できます。

Tree BFS パターンの仕組み:
1. ルートノードをキューに追加します。
2. キューが空になるまで反復処理を続けます。
3. 各反復で、キューの先頭にあるノードを取り出し、そのノードを「訪問」します。
4. キューから各ノードを取り出した後、そのすべての子ノードをキューに挿入します。

Tree BFS パターンを識別する方法:
- 木をレベルごとに (レベルオーダートラバーサル) 走査するように求められた場合。

Tree BFS パターンを使用する問題例:
- Binary Tree Level Order Traversal (easy): 各レベルのノードを左から右へリスト化する。
- Zigzag Traversal (medium): レベルごとに走査方向を交互（左→右、右→左）に変える。
- Minimum Depth of Binary Tree (easy): ルートから最も近い葉までのノード数を求める。
- Level Averages in a Binary Tree (easy): 各レベルのノードの値の平均値を計算する。
- Connect Level Order Siblings (medium): 同じレベルにある隣接ノード同士を接続する。
"""

# --- 基本的なレベルオーダートラバーサル ---
def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    二分木のレベルオーダートラバーサルを実行します。

    Args:
        root: 二分木のルートノード。

    Returns:
        各レベルのノードの値を含むリストのリスト。
        例: [[3], [9, 20], [15, 7]]

    入力:
        root: 二分木のルートノード (TreeNode オブジェクト) または None。
              TreeNode は val (値), left (左の子), right (右の子) を持ちます。

    出力:
        List[List[int]]: レベルごとにノードの値を格納したリスト。
                         木が空の場合は空のリスト [] を返します。

    時間計算量: O(N)
        N は木のノード数です。各ノードを正確に 1 回訪問し、キューに追加/削除するため。
        キューへの追加 (append) と削除 (popleft) は O(1) です。

    空間計算量: O(W) または O(N)
        W は木の最大の幅 (あるレベルでの最大ノード数) です。
        キューには最大で 1 つのレベルのすべてのノードが格納されるため、空間計算量は O(W) です。
        最悪の場合 (完全二分木など)、最後のレベルには約 N/2 個のノードが含まれる可能性があるため、
        空間計算量は O(N) とも言えます。結果を格納するリストも最悪 O(N) の空間を必要とします。
    """
    result: List[List[int]] = []
    if not root:
        return result

    queue = deque([root]) # 探索対象のノードを格納するキュー
    while queue:
        level_size = len(queue) # 現在のレベルのノード数
        current_level: list[int] = [] # 現在のレベルのノード値を格納するリスト
        # 現在のレベルのノードをすべて処理する
        for _ in range(level_size):
            node: TreeNode = queue.popleft() # キューの先頭からノードを取り出す
            current_level.append(node.val) # ノードの値を現在のレベルのリストに追加
            # 子ノードが存在すればキューに追加する
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level) # 現在のレベルのリストを結果リストに追加
    return result

# --- 例題 1: Zigzag Traversal ---
def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    二分木のジグザグレベルオーダートラバーサルを実行します。
    レベルごとに左から右、次に右から左へと交互に走査します。

    Args:
        root: 二分木のルートノード。

    Returns:
        ジグザグ順に各レベルのノードの値を含むリストのリスト。
        例: [[3], [20, 9], [15, 7]]

    入力:
        root: 二分木のルートノード (TreeNode オブジェクト) または None。

    出力:
        List[List[int]]: ジグザグ順にレベルごとにノードの値を格納したリスト。
                         木が空の場合は空のリスト [] を返します。

    時間計算量: O(N)
        N は木のノード数です。各ノードを正確に 1 回訪問するため。
        deque への append/appendleft は O(1) です。

    空間計算量: O(W) または O(N)
        W は木の最大の幅です。キューと current_level (deque) のサイズに依存します。
        最悪の場合 O(N)。結果リストも O(N) の空間を必要とします。
    """
    result: List[List[int]] = []
    if not root:
        return result

    queue = deque([root])
    left_to_right = True # 最初のレベルは左から右へ
    while queue:
        level_size = len(queue)
        current_level: deque[int] = deque() # deque を使うと効率的に先頭/末尾に追加できる
        for _ in range(level_size):
            node = queue.popleft()
            # 走査方向に応じて deque の先頭または末尾に追加
            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val) # 右から左の場合は先頭に追加

            # 子ノードをキューに追加 (順序は常に左、右)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(current_level)) # deque をリストに変換して結果に追加
        left_to_right = not left_to_right # 次のレベルのために方向を反転

    return result

# --- 例題 2: Minimum Depth of Binary Tree ---
def min_depth(root: Optional[TreeNode]) -> int:
    """
    二分木の最小の深さ（ルートから最も近い葉までのパス上のノード数）を見つけます。
    葉ノードとは、左右両方の子を持たないノードのことです。

    Args:
        root: 二分木のルートノード。

    Returns:
        最小の深さ (int)。ルートノードのみの場合は 1。

    入力:
        root: 二分木のルートノード (TreeNode オブジェクト) または None。

    出力:
        int: 最小の深さ。木が空の場合は 0。

    時間計算量: O(N)
        N は木のノード数です。最悪の場合、すべてのノードを訪問する必要があります
        (例えば、すべてのノードが一直線に並んでいる場合)。
        しかし、BFS はレベルごとに探索するため、最初に見つかった葉ノードまでのパスが
        最短であることが保証されます。そのため、平均的には O(N) より速く完了することが多いです。

    空間計算量: O(W) または O(N)
        W は木の最大の幅です。キューのサイズに依存します。
        最悪の場合 O(N)。
    """
    if not root:
        return 0

    queue = deque([(root, 1)]) # (ノード, 現在の深さ) のタプルを格納
    while queue:
        node, depth = queue.popleft()

        # 葉ノードかどうかをチェック (左右の子が両方ない)
        if not node.left and not node.right:
            return depth # 最初に見つかった葉ノードの深さが最小

        # 子ノードがあれば、深さを増やしてキューに追加
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    # この部分は、理論上は到達しないはずです。
    # なぜなら、空でない木には必ず葉ノードが存在し、BFS はそれを見つけるためです。
    # しかし、関数のシグネチャ上、int を返す必要があるため、形式的に 0 を返します。
    return 0


# --- 実行例 ---
if __name__ == '__main__':
    # テスト用の木の構築 例1
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    print("--- 木 1 ---")
    print("     3")
    print("    / \\")
    print("   9  20")
    print("     /  \\")
    print("    15   7")
    print("-" * 30)

    print("--- Level Order Traversal ---")
    print("期待される出力: [[3], [9, 20], [15, 7]]")
    print("実際の出力:", level_order_traversal(root1))
    print("-" * 30)

    print("--- Zigzag Level Order Traversal ---")
    print("期待される出力: [[3], [20, 9], [15, 7]]")
    print("実際の出力:", zigzag_level_order(root1))
    print("-" * 30)

    print("--- Minimum Depth of Binary Tree ---")
    print("期待される出力: 2 (ノード 9 が最も近い葉)")
    print("実際の出力:", min_depth(root1))
    print("-" * 30)

    # テスト用の木の構築 例2 (最小深さ用)
    #     2
    #      \
    #       3
    #        \
    #         4
    #          \
    #           5
    #            \
    #             6 (葉)
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)

    print("--- 木 2 ---")
    print("     2")
    print("      \\")
    print("       3")
    print("        \\")
    print("         4")
    print("          \\")
    print("           5")
    print("            \\")
    print("             6")
    print("-" * 30)
    print("--- Minimum Depth of Binary Tree ---")
    print("期待される出力: 5 (ノード 6 が唯一の葉)")
    print("実際の出力:", min_depth(root2))
    print("-" * 30)

    # テスト用の木の構築 例3 (最小深さ用)
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5 (葉)
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3) # 葉
    root3.left.left = TreeNode(4) # 葉
    root3.left.right = TreeNode(5) # 葉

    print("--- 木 3 ---")
    print("     1")
    print("    / \\")
    print("   2   3")
    print("  / \\")
    print(" 4   5")
    print("-" * 30)
    print("--- Minimum Depth of Binary Tree ---")
    print("期待される出力: 2 (ノード 3 が最も近い葉)")
    print("実際の出力:", min_depth(root3))
    print("-" * 30)


    # 空の木のテスト
    print("--- 空の木のテスト ---")
    print("Level Order Traversal (空):", level_order_traversal(None))
    print("Zigzag Level Order Traversal (空):", zigzag_level_order(None))
    print("Minimum Depth (空):", min_depth(None))
    print("-" * 30)
