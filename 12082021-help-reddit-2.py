## TASK 1 (a)
class node:
    def __init__(self, data: int, nextNode: int):
        self.data = data
        self.next = nextNode

## TASK 1 (b)
def main():
    linkedList = [
        node(1, 1),     # 0
        node(5, 4),     # 1
        node(6, 7),     # 2
        node(7, -1),    # 3
        node(2, 2),     # 4
        node(0, 6),     # 5
        node(0, 8),     # 6
        node(56, 3),    # 7
        node(0, 9),     # 8
        node(0, -1)     # 9
    ]

    outputNodes(linkedList, 0)  ## TASK 1 (c)(ii)

## TASK 1 (c)(i)
def outputNodes(linkedListArray, startPointer):
    
    while startPointer != -1:
        print(linkedListArray[startPointer].data)
        startPointer = linkedListArray[startPointer].next

class test():
    def __init__(self):
        test.name = "orange"
        test.__height = 3

testObject = test()
print(testObject.name)
print(testObject.__height)



## Run the main program
main()