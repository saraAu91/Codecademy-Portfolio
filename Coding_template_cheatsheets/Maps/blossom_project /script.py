from class_HashMap_LinkedList_Chaining import HashMap
from blossom_lib import flower_definitions

blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))