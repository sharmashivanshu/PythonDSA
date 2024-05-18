from queue_linked_list.queue import Queue


class BST:
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None


def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.value)
    pre_order_traversal(root_node.leftNode)
    pre_order_traversal(root_node.rightNode)


def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.leftNode)
    print(root_node.value)
    in_order_traversal(root_node.rightNode)


def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.leftNode)
    post_order_traversal(root_node.rightNode)
    print(root_node.value)


def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        my_que = Queue()
        my_que.enqueue(root_node)
        while not(my_que.is_empty()):
            root = my_que.deque()
            print(root.value.value)
            if root.value.leftNode is not None:
                my_que.enqueue(root.value.leftNode)
            if root.value.rightNode is not None:
                my_que.enqueue(root.value.rightNode)


def insert_node(root_node, value):
    if root_node.value is None:
        root_node.value = value
    elif root_node.value >= value:
        if root_node.leftNode is None:
            root_node.leftNode = BST(value)
            print(f"Inserted to left: {value}")
        else:
            insert_node(root_node.leftNode, value)
    else:
        if root_node.value < value:
            if root_node.rightNode is None:
                root_node.rightNode = BST(value)
                print(f"Inserted to right: {value}")
            else:
                insert_node(root_node.rightNode, value)
    return f"Node with {value} is inserted"


def search_bst(root_node, value):
    if root_node.value == value:
        print("Value found as root node.")
    elif value <= root_node.value:
        if value == root_node.leftNode.value:
            print("Value found in left node.")
        else:
            search_bst(root_node.leftNode, value)
    else:
        if value == root_node.rightNode.value:
            print("Value found in left node.")
        else:
            search_bst(root_node.rightNode, value)


bst = BST(None)
print(insert_node(bst, 90))
print(insert_node(bst, 70))
print(insert_node(bst, 100))
print(insert_node(bst, 80))
# print(bst.value)
# print(bst.leftNode.value)
# print(bst.rightNode.value)
# print("Pre Order Traversal")
# pre_order_traversal(bst)
# print("In Order Traversal")
# in_order_traversal(bst)
# print("Post Order Traversal")
# post_order_traversal(bst)
print("Level Order Traversal")
level_order_traversal(bst)
