"""

SLL creation
add node
delete node
print SLL

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def add(self, new_node: Node):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        else:
            self.head = new_node

    def remove(self, data):
        if self.head:
            # check if first node
            if self.head.data == data:
                self.head = self.head.next
            else:
                curr = self.head
                prev = None
                while curr:
                    if curr.data == data:
                        break

                    prev = curr
                    curr = curr.next

                if curr is None:
                    print(f"{data} does not exist in the SLL")
                else:
                    # delete the prev
                    prev.next = curr.next
                    del curr
        else:
            print("SLL is empty nothing to delete")

    def print(self):
        if self.head:
            curr = self.head
            while curr:
                print(f"{curr.data} ->", end=" ")
                curr = curr.next
            print()
        else:
            print("SLL is empty")


if __name__ == '__main__':
    sll = SLL()
    sll.print()
    sll.add(Node(1))
    sll.add(Node(2))
    sll.add(Node(1))
    sll.add(Node(4))
    sll.print()
    sll.remove(2)
    sll.print()
    sll.remove(5)
    sll.print()
    sll.remove(4)
    sll.print()
    sll.remove(1)
    sll.print()
    sll.remove(1)
    sll.print()
    sll.remove(3)
    sll.print()
