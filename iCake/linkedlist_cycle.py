'''
Write a function contains_cycle() 
that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.

Solution
We keep two pointers to nodes (we'll call these “runners”), both starting at the first node. 
Every time slow_runner moves one node ahead, fast_runner moves two nodes ahead.

If the linked list has a cycle, fast_runner will "lap" (catch up with) slow_runner, and they will momentarily equal each other.

If the list does not have a cycle, fast_runner will reach the end.
'''
class Node:
  # constructor
  def __init__(self, data, next=None): 
    self.data = data
    self.next = next

def contains_cycle(first_node):
      # Start both runners at the beginning
      slow_runner = first_node
      fast_runner = first_node
      # Until we hit the end of the list
      while fast_runner is not None and fast_runner.next is not None:
          slow_runner = slow_runner.next
          fast_runner = fast_runner.next.next
          # Case: fast_runner is about to "lap" slow_runner
          if fast_runner is slow_runner:
              return True
      # Case: fast_runner hit the end of the list
      return False

    

def main():
    
    first_node = Node(3) 
    second_node = Node(4)
    third_node = Node(5)
    fourth_node = Node(6)

    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = first_node

    print("Cycle or not in linked list = "+ str(bool(contains_cycle(first_node))))
   
main()
