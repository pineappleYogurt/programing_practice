"""
Sliding Window パターン

Sliding Window パターンは、配列や連結リストなどの線形データ構造の特定サイズのウィンドウ（部分配列や部分リスト）に対して
操作を行う際に使用されます。例えば、「すべてが1である最長の部分配列を見つける」といった問題に適用できます。

ウィンドウは通常、最初の要素から始まり、要素を1つずつ右にシフトしていきます。
問題に応じて、ウィンドウのサイズは固定の場合もあれば、拡大・縮小する場合もあります。

Sliding Window パターンが適用できる可能性のある問題の特徴:
- 入力が線形データ構造（配列、連結リスト、文字列など）である。
- 最長/最短の部分文字列、部分配列、または特定の値を求める必要がある。

一般的な問題例:
- サイズ 'K' の最大和サブ配列 (Maximum sum subarray of size ‘K’) (Easy)
- 'K' 個の異なる文字を持つ最長の部分文字列 (Longest substring with ‘K’ distinct characters) (Medium)
- 文字列アナグラム (String anagrams) (Hard)
"""

def max_sub_array_of_size_k(k, arr):
    """
    与えられた配列の中で、サイズ 'k' の連続する部分配列の最大和を求める関数 (Sliding Window パターン使用)

    引数:
    k (int): 部分配列のサイズ
    arr (list[int]): 整数の配列

    戻り値:
    int: サイズ 'k' の部分配列の中で最大の和。該当する部分配列がない場合は 0 を返す。

    例:
    入力: k=3, arr=[2, 1, 5, 1, 3, 2]
    出力: 9  # 部分配列 [5, 1, 3] の和が最大

    入力: k=2, arr=[2, 3, 4, 1, 5]
    出力: 7  # 部分配列 [3, 4] の和が最大

    時間計算量: O(n)  # n は配列 arr の長さ。配列を一度だけ走査するため。
    空間計算量: O(1)  # 定数空間。追加のデータ構造を使用しないため。

    アルゴリズム:
    1. 最初の k 個の要素の和を計算し、これを現在の最大和とする。
    2. ウィンドウを1つずつ右にスライドさせる。
    3. スライドごとに、ウィンドウの左端の要素を和から引き、右端の新しい要素を和に加える。
    4. 各ステップで現在の和と最大和を比較し、最大和を更新する。
    """
    if not arr or k <= 0 or k > len(arr):
        return 0  # 不正な入力や、k が配列長より大きい場合

    max_sum = 0
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # ウィンドウの右端の要素を加える

        # ウィンドウサイズが k に達したら、最大和を更新し、ウィンドウをスライドさせる
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)  # 最大和を更新
            window_sum -= arr[window_start]  # ウィンドウの左端の要素を引く
            window_start += 1  # ウィンドウの開始位置を右にずらす

    return max_sum

# Example Usage:
if __name__ == "__main__":
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    print(f"Input: k={k1}, arr={arr1}")
    print(f"Output: {max_sub_array_of_size_k(k1, arr1)}")  # Expected output: 9

    arr2 = [2, 3, 4, 1, 5]
    k2 = 2
    print(f"\nInput: k={k2}, arr={arr2}")
    print(f"Output: {max_sub_array_of_size_k(k2, arr2)}")  # Expected output: 7

    arr3 = [1, 1, 1, 1, 1]
    k3 = 4
    print(f"\nInput: k={k3}, arr={arr3}")
    print(f"Output: {max_sub_array_of_size_k(k3, arr3)}") # Expected output: 4

    arr4 = [1, 2, 3]
    k4 = 5
    print(f"\nInput: k={k4}, arr={arr4}")
    print(f"Output: {max_sub_array_of_size_k(k4, arr4)}") # Expected output: 0 (k > len(arr))
