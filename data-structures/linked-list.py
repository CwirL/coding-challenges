class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Append nodes to linked list
def insertNodeAtTail(head, data):
    nnode = SinglyLinkedListNode(data)
    if head is None:
        head = nnode
        return head
    current = head
    while current.next is not None:
        current = current.next
    current.next = nnode
    return head


# Pre-append nodes to linked list
def insertNodeAtHead(head, data):
    nnode = SinglyLinkedListNode(data)
    if head is None:
        head = nnode
        return head
    nnode.next = head
    head = nnode
    return head


if __name__ == '__main__':
    fptr = open('./output', 'w')
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()