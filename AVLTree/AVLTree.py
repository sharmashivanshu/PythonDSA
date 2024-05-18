# from queue_linked_list.queue import Queue
from queue_linked_list.QueuseLinkedList import Queue


class AVLNode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.depth = 1


def pre_order_traversal(avl_node):
    if not avl_node:
        return
    print(avl_node.value)
    pre_order_traversal(avl_node.leftChild)
    pre_order_traversal(avl_node.rightChild)


def in_order_traversal(avl_node):
    if not avl_node:
        return
    in_order_traversal(avl_node.leftChild)
    print(avl_node.value)
    in_order_traversal(avl_node.rightChild)


def post_order_traversal(avl_node):
    if not avl_node:
        return
    post_order_traversal(avl_node.leftChild)
    post_order_traversal(avl_node.rightChild)
    print(avl_node.value)


def level_order_traversal(avl_node):
    if not avl_node:
        return
    else:
        my_queue = Queue()
        my_queue.enqueue(avl_node)
        while not (my_queue.isEmpty()):
            mynode = my_queue.dequeue()
            print(mynode.value.data)
            if mynode.value.leftChild is not None:
                my_queue.enqueue(mynode.value.leftChild)
            if mynode.value.rightChild is not None:
                my_queue.enqueue(mynode.value.rightChild)


def get_depth(unbalanced):
    if not unbalanced:
        return 0
    return unbalanced.depth


def right_rotation(unbalanced):
    new_node = unbalanced.leftChild
    unbalanced.leftChild = unbalanced.leftChild.rightChild
    unbalanced.leftChild = unbalanced
    unbalanced.depth = 1 + max(get_depth(unbalanced.leftChild), get_depth(unbalanced.rightChild))
    new_node.depth = 1 + max(get_depth(new_node.leftChild), get_depth(new_node.rightChild))
    return new_node


def left_rotation(unbalanced):
    new_node = unbalanced.rightChild
    unbalanced.rightChild = unbalanced.rightChild.leftChild
    new_node.leftChild = unbalanced
    unbalanced.depth = 1 + max(get_depth(unbalanced.leftChild), get_depth(unbalanced.rightChild))
    new_node.depth = 1 + max(get_depth(new_node.leftChild), get_depth(new_node.rightChild))
    return new_node


def get_balance(avl_node):
    if not avl_node:
        return 0
    return get_depth(avl_node.leftChild) - get_depth(avl_node.rightChild)


def insert_node(avl_node, val):
    if not avl_node:
        return AVLNode(val)
    elif val < avl_node.data:
        avl_node.leftChild = insert_node(avl_node.leftChild, val)
    else:
        avl_node.rightChild = insert_node(avl_node.rightChild, val)

    avl_node.depth = 1 + max(get_depth(avl_node.leftChild), get_depth(avl_node.rightChild))
    balance = get_balance(avl_node)
    if balance > 1 and val < avl_node.leftChild.data:
        return right_rotation(avl_node)
    if balance > 1 and val > avl_node.leftChild.data:
        avl_node.leftChild = left_rotation(avl_node.leftChild)
        return right_rotation(avl_node)
    if balance < -1 and val > avl_node.rightChild.data:
        return left_rotation(avl_node)
    if balance < -1 and val < avl_node.rightChild.data:
        avl_node.rightChild = right_rotation(avl_node.rightChild)
        return left_rotation(avl_node)
    return avl_node


def get_mini_value(avl_node):
    if avl_node is None or avl_node.leftChild is None:
        return avl_node
    return get_mini_value(avl_node.leftChild)


def delete_node(avl_node, value):
    if avl_node is None:
        return avl_node
    elif value < avl_node.data:
        avl_node.leftChild = delete_node(avl_node.leftChild, value)
    elif value > avl_node.data:
        avl_node.rightChild = delete_node(avl_node.rightChild, value)
    else:
        if avl_node.leftChild is None:
            temp = avl_node.rightChild
            avl_node = None
            return temp
        elif avl_node.rightChild is None:
            temp = avl_node.leftChild
            avl_node = None
            return temp
        temp = get_mini_value(avl_node.rightChild)
        avl_node.data = temp.data
        avl_node.rightChild = delete_node(avl_node.rightChild, temp.data)
    balance = get_balance(avl_node)
    if balance > 1 and get_balance(avl_node.leftChild) >= 0:
        return right_rotation(avl_node)
    if balance < -1 and get_balance(avl_node.rightChild) <= 0:
        return left_rotation(avl_node)
    if balance > 1 and get_balance(avl_node.leftChild) < 0:
        avl_node.leftChild = left_rotation(avl_node.leftChild)
        return right_rotation(avl_node)
    if balance < -1 and get_balance(avl_node.rightChild) > 0:
        avl_node.rightChild = right_rotation(avl_node.rightChild)
        return left_rotation(avl_node)
    return avl_node


newAVL = AVLNode(5)
newAVL = insert_node(newAVL, 10)
newAVL = insert_node(newAVL, 15)
newAVL = insert_node(newAVL, 20)
level_order_traversal(newAVL)
newAVL = delete_node(newAVL, 15)
print("Deleted node:")
level_order_traversal(newAVL)
newAVL = None
print("Deleted Entire")
level_order_traversal(newAVL)
