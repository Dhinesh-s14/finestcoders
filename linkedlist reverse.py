class Node:
    def __init__(self, data):
        self.data = data
        self.add = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.add is not None:
                temp = temp.add
            temp.add = newnode

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.add
        print("None")

    def reversekgroup(self, head, k):
        prev = None
        curr = head
        count = 0

        # reverse k nodes
        while curr and count < k:
            nxt = curr.add
            curr.add = prev
            prev = curr
            curr = nxt
            count += 1

        # recursively reverse the remaining list
        if curr:
            head.add = self.reversekgroup(curr, k)

        return prev


# --- Driver code ---
l1 = Linkedlist()
for num in [1, 2, 3, 4, 5, 6]:
    l1.append(num)

print("Original List:")
l1.display()

k = 4
l1.head = l1.reversekgroup(l1.head, k)

print(f"Reversed in groups of {k}:")
l1.display()
