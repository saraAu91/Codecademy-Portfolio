#This function, sum_digits(), 
# produces the sum of all the digits in a positive number as if they were each a single number:

def sum_digits(n):
  if n < 0:
     print("Inputs 0 or greater only!")
  if n <= 9: # if the number has just one digit 
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit


# test cases

print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)

# Calculate the min  of a list 
def find_min(my_list, min = None):
  if not my_list:
    return min 
  else: 
    if not min or my_list[0] < min:
      min = my_list[0]
    return  find_min(my_list[1:], min)
  

# check if a word is palindrome 

def is_palindrome(my_string):
  if len(my_string) <= 1:
      return True
  else:
    if my_string[0] == my_string[-1]:
      return is_palindrome(my_string[1: -1])


# multiplication

def multiplication(num_a, num_b):
  if num_a == 0 or num_b == 0:
    return 0

  return num_a + multiplication(num_a, num_b - 1)


# depth of tree

def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 


print(tree_level_2)

def depth(tree_node):
  if tree_node is None:
    return 0
  else: 
    left_depth = depth(tree_node["left_child"])
    right_depth = depth(tree_node["right_child"] )
    if left_depth > right_depth:
      return left_depth + 1
    else:
      return right_depth + 1

#Move items to the end of a list

def move_to_end(lst, val):
  result = []
  if len(lst) == 0:
    return []
 
  if lst[0] == val:
    result += move_to_end(lst[1:], val)
    result.append(lst[0])
  else:
    result.append(lst[0])
    result += move_to_end(lst[1:], val)
 
  return result


#remove node from a linked list
def remove_node(head, i):
    if i < 0:
        return head
    if head is None:
        return None
    if i == 0:
        return head.next_node
        
    head.next_node = remove_node(head.next_node, i - 1)
    return head

#Prepend and append to a string

def wrap_string(str, n):
  result = ""
  if n <= 0:
    return str
  else:
    result = "<" + result
    result = result + wrap_string(str, n-1)
    result = result +">"
  return result

# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)