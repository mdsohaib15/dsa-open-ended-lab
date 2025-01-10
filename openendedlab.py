class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def isempty(self):
        return self.top == None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            return None
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def size(self):
        count = 0
        temp = self.top
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def reverse_linked_list(self, head):
        if head is None:
            return None
        
        # Push all nodes onto the stack
        s = Stack()
        current = head
        while current:
            s.push(current.data)
            current = current.next
        
        # Now pop from the stack and rebuild the linked list in reverse order
        new_head = Node(s.pop())
        current = new_head
        while not s.isempty():
            current.next = Node(s.pop())
            current = current.next
        
        return new_head

    def print_linked_list(self, head):
        current = head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Example Usage
# Create a linked list from a list of values
head = create_linked_list([1, 2, 3, 4, 5])

# Print the original linked list
print("Original Linked List:")
s = Stack()
s.print_linked_list(head)

# Reverse the linked list using the stack
reversed_head = s.reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:")
s.print_linked_list(reversed_head)
