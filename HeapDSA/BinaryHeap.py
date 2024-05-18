
class Heap:
    def __init__(self, size):
        self.customList = (size+1)*[None]
        self.heapSize = 0
        self.maxSize = size + 1


def peak(heapNode):
    if not heapNode.customList:
        return
    return heapNode.customList[1]

def sizeOfHeap(heapNode):
    if not heapNode:
        return
    return heapNode.heapSize

def levelOrderTraversal(heapNode):
    if not heapNode:
        return
    else:
        for i in range(1, heapNode.heapSize+1):
            print(heapNode.customList[i])

def heapifyInsert(heapNode, index, type):
    parent = int(index/2)
    if index <= 1:
        return
    if type == "Min":
        if heapNode.customList[index] < heapNode.customList[parent]:
            temp = heapNode.customList[index]
            heapNode.customList[index] = heapNode.customList[parent]
            heapNode.customList[parent] = temp
        heapifyInsert(heapNode, parent, type)
    elif type == "Max":
        if heapNode.customList[index] > heapNode.customList[parent]:
            temp = heapNode.customList[index]
            heapNode.customList[index] = heapNode.customList[parent]
            heapNode.customList[parent] = temp
        heapifyInsert(heapNode, parent, type)

def insertNode(heapNode, value, type):
    if heapNode.heapSize + 1 == heapNode.maxSize:
        print(f"Heap is full, can not add {value}")
    else:
        heapNode.customList[heapNode.heapSize + 1] = value
        heapNode.heapSize += 1
        heapifyInsert(heapNode, heapNode.heapSize, type)
        print(f"Heap {value} added successfully")

def heapifyTreeExtract(heapNode, index, value):
    leftIndex = index*2
    rightIndex = index * 2 + 1
    swap = 0
    # Check if tree has no left and right leg
    if heapNode.heapSize < leftIndex:
        return
    # Check if tree has only left leg
    elif heapNode.heapSize == leftIndex:
        if type == "Min":
            if heapNode.customList[index] > heapNode.customList[leftIndex]:
                temp = heapNode.customList[index]
                heapNode.customList[index] = heapNode.customList[leftIndex]
                heapNode.customList[leftIndex] = temp
            return
        else:
            if heapNode.customList[index] < heapNode.customList[leftIndex]:
                temp = heapNode.customList[index]
                heapNode.customList[index] = heapNode.customList[leftIndex]
                heapNode.customList[leftIndex] = temp
            return
    # Check if tree has only right leg
    else:
        if type == "Min":
            if heapNode.customList[leftIndex] < heapNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if heapNode.customList[index] > heapNode.customList[swapChild]:
                temp = heapNode.customList[index]
                heapNode.customList[index] = heapNode.customList[swapChild]
                heapNode.customList[swapChild] = temp
        else:
            if heapNode.customList[leftIndex]  > heapNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if heapNode.customList[index] < heapNode.customList[swapChild]:
                temp = heapNode.customList[index]
                heapNode.customList[index] = heapNode.customList[swapChild]
                heapNode.customList[swapChild] = temp
        heapifyTreeExtract(heapNode, swapChild, type)


def extractNode(heapNode, type):
    if heapNode.heapSize == 0:
        return
    else:
        extractNode = heapNode.customList[1]
        heapNode.customList[1] = heapNode.customList[heapNode.heapSize]
        heapNode.customList[heapNode.heapSize] = None
        heapNode.heapSize -= 1
        heapifyTreeExtract(heapNode, 1, type)
        return extractNode



newHeap = Heap(5)
print(newHeap)
print(peak(newHeap))
print(sizeOfHeap(newHeap))
insertNode(newHeap, 3, "Min")
insertNode(newHeap, 4, "Min")
insertNode(newHeap, 5, "Min")
insertNode(newHeap, 2, "Min")
insertNode(newHeap, 1, "Min")
# insertNode(newHeap, 6, "Max")
levelOrderTraversal(newHeap)
extractNode(newHeap, "Min")
print("After extract")
levelOrderTraversal(newHeap)


