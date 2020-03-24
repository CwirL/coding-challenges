class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Append nodes to linked listuhb
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

# Insert node at given position
def insertNodeAtPosition(head, data, position):
    if head is None:
        return head
    current = head
    nnode = SinglyLinkedListNode(data)
    for i in range(position-1):
        current = current.next
    nnode.next = current.next
    current.next = nnode
    return head


def deleteNode(head, position):
    if head is None:
        return head
    if position == 0:
        head = head.next
        return head
    current = head
    for i in range(position - 1):
        current = current.next
    current.next = current.next.next
    return head


# Print link list in reversed  orderss
def reversePrint(head):
    if head is None:
        return None
    reversePrint(head.next)
    print(head.data)


def reverse(head):
    if head is None:
        return None
    nhead = reverse(head.next)
    head.next = None
    if nhead is None:
        return head
    else:
        current = nhead
        while current.next is not None:
            current = current.next
        current.next = head
        return nhead


def compare_lists(llist1, llist2):
    if llist1 is None and llist2 is None:
        return 1
    elif llist1 is None or llist2 is None:
        return 0
    currentllist1 = llist1
    currentllist2 = llist2
    while currentllist1.next is not None:
        if currentllist2.next is None:
            return 0
        if currentllist1.data != currentllist2.data:
            return 0
        currentllist1 = currentllist1.next
        currentllist2 = currentllist2.next
    return 1


def mergeLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1 is None and head2 is None:
        return None
    if head1.data < head2.data:
        current1 = head1
        current2 = head2
        head = head1
    else:
        current1 = head2
        current2 = head1
        head = head2
    current = head
    while current1.next is not None and current2.next is not None:
        if current1.next is None:
            current = current2.next
            return head
        if current2.next is None:
            current = current1.next
            return head
        if current1.next.data < current2.next.data:
            current = current1.next
            current1 = current1.next
        else:
            current = current2.next
            current2 = current2.next
        print(current.data)
    return head

def getNode(head, positionFromTail):
    if head is None:
        return head
    n = 0
    tail = head
    while tail.next is not None:
        tail = tail.next
        n = n+1
    positionFromHead = n-positionFromTail
    node = head
    for i in range(positionFromHead):
        if node.next is None:
            return node
        node = node.next
    return node.data


if __name__ == '__main__':
    fptr = open('../output', 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        fptr.write(str(result) + '\n')
    fptr.close()
