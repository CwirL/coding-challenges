class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        new_node.next = None
        if head is None:
            head = new_node
        else:
            current_node = head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        return head
    def removeDuplicates(self, head):
        current = head
        while current:
            previous = current
            current = current.next
            if previous is None or current is None:
                continue
            if current.data == previous.data:
                previous.next = current.next
                current = previous
        self.display(head)
        return None

myList = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = myList.insert(head, data)
myList.removeDuplicates(head)
