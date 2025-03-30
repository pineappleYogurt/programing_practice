# -*- coding: utf-8 -*-

"""
Two Pointers (2つのポインタ) パターン

## 説明
Two Pointersは、データ構造（主にソート済みの配列や連結リスト）を2つのポインタを使って効率的に走査するアルゴリズムパターンです。
2つのポインタは、通常、配列の両端（開始と終了）または異なる開始点から始まり、特定の条件を満たすまで互いに向かって、または同じ方向に移動します。
このパターンは、特にソートされたデータ構造内でペアやサブ配列を探す問題に適しています。

## なぜ使うのか？
単純な1つのポインタ（イテレータ）だけを使用する場合、配列の各要素を他のすべての要素と比較する必要があり、ネストしたループが発生しがちです。
これにより、計算量がO(n^2)になることがよくあります（nは要素数）。
Two Pointersを使用すると、多くの場合、計算量をO(n)に削減でき、空間計算量もO(1)またはO(n)（結果を格納する場合）に抑えることができます。

## Two Pointersパターンの見分け方
- 問題がソート済みの配列や連結リストを扱う場合。
- 特定の制約を満たす要素のペア、トリプレット、またはサブ配列を見つける必要がある場合。

## 具体例：ソート済み配列から特定の合計値を持つペアを見つける (Two Sum II - Input array is sorted)

問題：ソート済みの整数配列 `numbers` と整数 `target` が与えられます。
`numbers` の中で、合計すると `target` になる2つの要素のインデックス（1-based）を返してください。
解は必ず1つ存在し、同じ要素を2回使用することはできません。

例：
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
説明: 2 + 7 = 9 なので、インデックス1と2を返します。

Input: numbers = [2, 3, 4], target = 6
Output: [1, 3]
説明: 2 + 4 = 6 なので、インデックス1と3を返します。

Input: numbers = [-1, 0], target = -1
Output: [1, 2]
説明: -1 + 0 = -1 なので、インデックス1と2を返します。

## 実装
"""

from typing import List

def find_pair_with_target_sum(numbers: List[int], target: int) -> List[int]:
    """
    ソート済み配列内で、指定されたターゲット値になる2つの要素のインデックス（1-based）を見つけます。

    Args:
        numbers (List[int]): 昇順にソートされた整数のリスト。
        target (int): 目標とする合計値。

    Returns:
        List[int]: 合計がターゲット値になる2つの要素のインデックス（1-based）のリスト。
                   解が見つからない場合は空のリストを返しますが、この問題設定では解は必ず存在します。

    時間計算量 (Time Complexity): O(n)
        - leftポインタとrightポインタはそれぞれ最大でn回移動します。
        - 各ステップでの比較とポインタの移動はO(1)です。
        - 全体として、配列を1回走査するのと同等なのでO(n)となります。

    空間計算量 (Space Complexity): O(1)
        - ポインタ変数（left, right）と合計値を格納する変数以外に追加のメモリを使用しません。
        - 結果を格納するためのスペースは通常、空間計算量に含まれませんが、もし含める場合はO(1)またはO(2)であり、定数です。
    """
    left = 0  # 配列の開始地点を指すポインタ
    right = len(numbers) - 1  # 配列の終了地点を指すポインタ

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # 合計がターゲットと一致した場合、インデックス（1-based）を返す
            # インデックスは0-basedなので、+1する
            return [left + 1, right + 1]
        elif current_sum < target:
            # 合計がターゲットより小さい場合、より大きな値が必要
            # leftポインタを右に移動して、合計を増やす
            left += 1
        else: # current_sum > target
            # 合計がターゲットより大きい場合、より小さな値が必要
            # rightポインタを左に移動して、合計を減らす
            right -= 1

    # 問題の制約により、このループは必ずターゲットを見つけて終了するはずです。
    # したがって、以下の行には到達しない想定です。
    assert False, "解が必ず存在するはずですが、見つかりませんでした。"
    # 型チェッカーを満たすために形式的にreturn文を記述しますが、実行されることはありません。
    return [] # 到達不能コード (Unreachable code)

# --- テストコード ---
if __name__ == '__main__':
    # テストケース1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    result1 = find_pair_with_target_sum(numbers1, target1)
    print(f"Input: numbers = {numbers1}, target = {target1}")
    print(f"Output: {result1}") # Expected: [1, 2]
    print("-" * 20)

    # テストケース2
    numbers2 = [2, 3, 4]
    target2 = 6
    result2 = find_pair_with_target_sum(numbers2, target2)
    print(f"Input: numbers = {numbers2}, target = {target2}")
    print(f"Output: {result2}") # Expected: [1, 3]
    print("-" * 20)

    # テストケース3
    numbers3 = [-1, 0]
    target3 = -1
    result3 = find_pair_with_target_sum(numbers3, target3)
    print(f"Input: numbers = {numbers3}, target = {target3}")
    print(f"Output: {result3}") # Expected: [1, 2]
    print("-" * 20)

    # テストケース4 (重複する値がある場合)
    numbers4 = [0, 0, 3, 4]
    target4 = 0
    result4 = find_pair_with_target_sum(numbers4, target4)
    print(f"Input: numbers = {numbers4}, target = {target4}")
    print(f"Output: {result4}") # Expected: [1, 2]
    print("-" * 20)
