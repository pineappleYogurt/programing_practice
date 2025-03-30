class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    """
    連結リストをインプレースで反転する関数

    引数:
    head (Node): 連結リストの先頭ノード

    戻り値:
    Node: 反転された連結リストの先頭ノード

    例:
    入力: 1 -> 2 -> 3 -> 4 -> 5 -> None
    出力: 5 -> 4 -> 3 -> 2 -> 1 -> None

    時間計算量: O(n)  # nは連結リストのノード数。リストを一度走査するため
    空間計算量: O(1)  # 定数空間。追加のデータ構造を使用しないため

    """
    prev = None
    current = head
    while(current is not None):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example Usage:
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Print the original linked list
    print("Original Linked List:")
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

    # Reverse the linked list
    reversed_head = reverse_linked_list(head)

    # Print the reversed linked list
    print("\nReversed Linked List:")
    current = reversed_head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
