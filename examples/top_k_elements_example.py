import heapq

# Top K Elements パターン
#
# 問題のタイプ:
# 与えられた集合の中から、上位/下位/頻出の 'K' 個の要素を見つける問題。
#
# アプローチ:
# このパターンでは、ヒープ (Heap) データ構造を使用して、
# 効率的に 'K' 個の要素を追跡します。
#
# 1. 問題に応じて、最小ヒープ (Min-Heap) または最大ヒープ (Max-Heap) に
#    最初の 'K' 個の要素を挿入します。
# 2. 残りの要素を順に見ていきます。
# 3. 新しい要素がヒープの要素と比較して、問題の条件
#    (例: より大きい、より小さい、より頻度が高い) を満たす場合、
#    ヒープから条件に合わない要素を削除し、新しい要素を挿入します。
#
# なぜヒープか？:
# ヒープは、常に最小値 (最小ヒープ) または最大値 (最大ヒープ) に
# O(1) でアクセスでき、要素の挿入と削除を O(log K) で行えるため、
# K 個の要素を効率的に管理するのに適しています。
# ソートアルゴリズム (例: O(N log N)) よりも効率的な場合があります。
#
# パターンの見分け方:
# - 上位/下位/頻出の 'K' 個の要素を求める問題。
# - 特定の要素を見つけるために配列をソートする必要があると感じる問題 (ヒープが代替手段となりうる)。
#
# 例題: Top 'K' Numbers (上位 K 個の数値)

def find_k_largest_numbers(nums, k):
  """
  与えられた数値のリストから上位 K 個の数値を効率的に見つけます。

  Args:
    nums: 数値のリスト (例: [3, 1, 5, 12, 2, 11])
    k: 見つけたい上位要素の数 (例: 3)

  Returns:
    上位 K 個の数値を含むリスト (順不同) (例: [5, 12, 11])
    もし k がリストの長さ以上なら、リスト全体を返します。
    もし k が 0 以下なら、空のリストを返します。

  時間計算量:
    O(N log K)
    - 最初の K 個の要素でヒープを構築するのに O(K)。
    - 残りの N-K 個の要素について、それぞれヒープへの挿入/削除 (pushpop) が
      O(log K) かかるため、(N-K) * log K。
    - 全体として O(K + (N-K)log K) となり、N が K より大きい場合、
      O(N log K) と近似できます。
    - もし K >= N なら、O(N log N) (リスト全体をヒープに入れるため)。

  空間計算量:
    O(K)
    - ヒープに最大 K 個の要素を格納するため。
  """
  if k <= 0:
    return []
  if k >= len(nums):
    return nums

  # 最小ヒープ (min-heap) を使用します。
  # ヒープには常に K 個の要素が格納され、ヒープのルート (最小値) が
  # これまでに見つかった K 個の要素の中で最も小さい値になります。
  min_heap = []

  # 最初の K 個の要素をヒープに追加
  for i in range(k):
    heapq.heappush(min_heap, nums[i])

  # 残りの要素を処理
  for i in range(k, len(nums)):
    # 現在の要素がヒープの最小値 (ルート) より大きい場合
    if nums[i] > min_heap[0]:
      # ヒープの最小値を削除し、現在の要素を追加
      # heappushpop は push と pop を効率的に行う
      heapq.heappushpop(min_heap, nums[i])

  # ヒープに残っている K 個の要素が上位 K 個の数値
  return list(min_heap)

# --- 実行例 ---
nums1 = [3, 1, 5, 12, 2, 11]
k1 = 3
print(f"リスト: {nums1}, K={k1}")
print(f"上位 K 個の数値: {find_k_largest_numbers(nums1, k1)}") # 出力例: [5, 11, 12] (順不同)

nums2 = [5, 12, 11, -1, 12]
k2 = 3
print(f"\nリスト: {nums2}, K={k2}")
print(f"上位 K 個の数値: {find_k_largest_numbers(nums2, k2)}") # 出力例: [11, 12, 12] (順不同)

nums3 = [1, 2, 3, 4, 5]
k3 = 5
print(f"\nリスト: {nums3}, K={k3}")
print(f"上位 K 個の数値: {find_k_largest_numbers(nums3, k3)}") # 出力例: [1, 2, 3, 4, 5]

nums4 = [1, 2, 3]
k4 = 0
print(f"\nリスト: {nums4}, K={k4}")
print(f"上位 K 個の数値: {find_k_largest_numbers(nums4, k4)}") # 出力例: []


# 例題: Top 'K' Frequent Numbers (頻出上位 K 個の数値)
from collections import Counter

def find_k_frequent_numbers(nums, k):
  """
  与えられた数値のリストから頻出上位 K 個の数値を効率的に見つけます。

  Args:
    nums: 数値のリスト (例: [1, 3, 5, 12, 11, 12, 11])
    k: 見つけたい頻出上位要素の数 (例: 2)

  Returns:
    頻出上位 K 個の数値を含むリスト (順不同) (例: [11, 12])
    もし k がユニークな要素数以上なら、全てのユニークな要素を返します。
    もし k が 0 以下なら、空のリストを返します。

  時間計算量:
    O(N + N log K) または O(N log K)
    - 頻度マップの作成: O(N)
    - ヒープ操作:
      - ユニークな要素数を U とすると、最大 U 個の要素をヒープに入れる。
      - 各要素のヒープへの挿入/削除は O(log K)。
      - 全体で O(U log K)。U は最大 N なので、最悪 O(N log K)。
    - 全体として O(N + N log K) となり、O(N log K) と近似できます。
    - Counterを使う場合、内部実装によっては O(N) で頻度計算が終わる。

  空間計算量:
    O(N + K)
    - 頻度マップ: O(N) (最悪の場合、全ての要素がユニーク)
    - ヒープ: O(K)
  """
  if k <= 0:
    return []

  # 1. 各数値の出現頻度を数える
  freq_map = Counter(nums)

  # ユニークな要素数が k より少ない場合は、全てのユニークな要素を返す
  if k >= len(freq_map):
      return list(freq_map.keys())

  # 2. 最小ヒープを使って頻度上位 K 個を保持する
  # ヒープには (頻度, 数値) のタプルを格納する
  min_heap = []

  # 頻度マップの各要素を処理
  for num, freq in freq_map.items():
    if len(min_heap) < k:
      # ヒープが K 個未満なら、とりあえず追加
      heapq.heappush(min_heap, (freq, num))
    else:
      # ヒープが K 個ある場合、現在の要素の頻度が
      # ヒープ内の最小頻度 (ルート) より大きいか比較
      if freq > min_heap[0][0]:
        # 現在の要素の方が頻度が高い場合、最小頻度の要素を削除し、現在の要素を追加
        heapq.heappushpop(min_heap, (freq, num))

  # 3. ヒープに残った要素の数値部分を取り出す
  top_k = [num for freq, num in min_heap]
  return top_k

# --- 実行例 ---
nums_freq1 = [1, 3, 5, 12, 11, 12, 11]
k_freq1 = 2
print(f"\nリスト: {nums_freq1}, K={k_freq1}")
print(f"頻出上位 K 個の数値: {find_k_frequent_numbers(nums_freq1, k_freq1)}") # 出力例: [11, 12] (順不同)

nums_freq2 = [1, 1, 1, 2, 2, 3]
k_freq2 = 2
print(f"\nリスト: {nums_freq2}, K={k_freq2}")
print(f"頻出上位 K 個の数値: {find_k_frequent_numbers(nums_freq2, k_freq2)}") # 出力例: [1, 2] (順不同)

nums_freq3 = [1]
k_freq3 = 1
print(f"\nリスト: {nums_freq3}, K={k_freq3}")
print(f"頻出上位 K 個の数値: {find_k_frequent_numbers(nums_freq3, k_freq3)}") # 出力例: [1]

nums_freq4 = [1, 2, 3]
k_freq4 = 4
print(f"\nリスト: {nums_freq4}, K={k_freq4}")
print(f"頻出上位 K 個の数値: {find_k_frequent_numbers(nums_freq4, k_freq4)}") # 出力例: [1, 2, 3]
