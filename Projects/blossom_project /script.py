from class_HashMap_LinkedList_Chaining import HashMap
from blossom_lib import flower_definitions

blossom = HashMap(len(flower_definitions))
for item in flower_definitions:
  blossom.assign(item[0], item[1])

print(blossom.retrieve('daisy'))