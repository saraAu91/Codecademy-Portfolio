from Nodes_linklist_template import LinkedList

# Create a method that returns the nth last element of a singly linked list.

# Two Pointers Moving in Parallel

def nth_last_node(linked_list, n):
    current = None
    tail_seeker = linked_list.head_node
    count = 1
    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1
    if count >= n + 1:
        if current is None:  # if current:
            current = linked_list.head_node
        else:
            current = current.get_next_node()
    return current

# Create a method that returns the middle node of a linked list.

# Pointers at Different Speeds


def find_middle(linked_list):
    fast_pointer = linked_list.head_node
    slow_pointer = linked_list.head_node
    while fast_pointer is not None:
        fast_pointer = fast_pointer.get_next_node()
        if fast_pointer is not None:  # if fast_pointer:
            fast_pointer = fast_pointer.get_next_node()
            slow_pointer = slow_pointer.get_next_node()
    return slow_pointer

# alternative: move the fast pointer once with each loop iteration but only move the slow pointer every-other iteration


def find_middle_alt(linked_list):
    count = 0
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
    if count % 2 != 0:
        slow = slow.get_next_node()
        count += 1
    return slow


def generate_test_linked_list(lenght):
    linked_list = LinkedList()
    for i in range(lenght, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

#test 1

test_list = generate_test_linked_list(50)
print(test_list.stringify_list())
#nth_last = nth_last_node(test_list, 4)
#print(nth_last.value)

# test 2 

#test_list = generate_test_linked_list(7)
#print(test_list.stringify_list())
#middle_node = find_middle(test_list)
#print(middle_node.value)

