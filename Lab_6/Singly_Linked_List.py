# Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Create the LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None

    # Step 3: Implement the Append Method
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Step 4: Implement the Display Method
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    # Step 5: Implement the Insert Method
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # Step 6: Implement the Delete Method
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # Step 7: Implement the Search Method
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    # Step 8: Implement the Reverse Method
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head

        # Move fast by two steps and slow by one step until fast reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now pointing to the middle node
        if slow:
            return slow.data
        return None

    def has_cycle(self):
        slow = self.head
        fast = self.head

        # Traverse the list with two pointers
        while fast and fast.next:
            slow = slow.next          # Move slow by 1 step
            fast = fast.next.next     # Move fast by 2 steps

            # If slow and fast meet, there is a cycle
            if slow == fast:
                return True

        # If we reach here, there is no cycle
        return False

    def remove_duplicates(self):
        current = self.head
        previous = None
        seen_data = set()

        while current:
            if current.data in seen_data:
                # Duplicate found; remove it by skipping the node
                previous.next = current.next
            else:
                # New data found; add it to the set
                seen_data.add(current.data)
                previous = current
            current = current.next

    @staticmethod
    def merge_sorted_recursive(l1, l2):
        # Base cases
        if not l1:
            return l2
        if not l2:
            return l1
        
        # Compare and merge
        if l1.data < l2.data:
            l1.next = LinkedList.merge_sorted_recursive(l1.next, l2)
            return l1
        else:
            l2.next = LinkedList.merge_sorted_recursive(l1, l2.next)
            return l2
        
    @staticmethod
    def merge_sorted(list1, list2):
        merged_head = LinkedList.merge_sorted_recursive(list1.head, list2.head)
        merged_list = LinkedList()
        merged_list.head = merged_head
        return merged_list

# Test the LinkedList class
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3

ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3

ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3

print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1

ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Middle element:", ll.find_middle())  # Output: Middle element: 3

# Creating a LinkedList with a cycle for testing
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# Manually creating a cycle for testing (linking the last node back to the second node)
ll.head.next.next.next.next = ll.head.next

print("Has cycle:", ll.has_cycle())  # Output: Has cycle: True

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(4)

print("Before removing duplicates:")
ll.display()  # Output: 1 -> 2 -> 2 -> 3 -> 3 -> 4

ll.remove_duplicates()

print("After removing duplicates:")
ll.display()  # Output: 1 -> 2 -> 3 -> 4

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

merged_list = LinkedList.merge_sorted(list1, list2)
print("Merged sorted list:")
merged_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
