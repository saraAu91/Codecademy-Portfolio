
#binary search tree

#The “left” child of the tree must contain a value lesser than its parent
#The “right” child of the tree must contain a value greater than its parent.


bst_tree_node = {"data": 42}
bst_tree_node["left_child"] = {"data": 36}
bst_tree_node["right_child"] = {"data": 73}
 
bst_tree_node["data"] > bst_tree_node["left_child"]["data"]
# True
bst_tree_node["data"] < bst_tree_node["right_child"]["data"]
# True

#We can also assume our function will receive a sorted list of values as input.

#Base case: The input list is empty
#Return "No Child" to represent the lack of node

def build_bst(my_list):
    if my_list == []:
        return "No Child"


#Recursive step: The input list must be divided into two halves

#Find the middle index of the list
#Store the value located at the middle index
#Make a tree node with a "data" key set to the value
#Assign tree node’s "left child" to a recursive call using the left half of the list
#Assign tree node’s "right child" to a recursive call using the right half of the list
#Return the tree node

def build_bst(my_list):
    if len(my_list) == 0:
        return "No Child"

    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]
    
    print("Middle index: {0}".format(middle_idx))
    print("Middle value: {0}".format(middle_value))

  
    tree_node = {"data": middle_value}
    tree_node["left_child"] = build_bst(my_list[ : middle_idx])
    tree_node["right_child"] = build_bst(my_list[middle_idx + 1 : ])
    return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
#print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"