from Structures import *

"""
Notion of neighborhoods:
    - We have a starting situation
    - You can take an element and put it elsewhere (Pick'n'Drop)
    - You can either take two elements and exchange them (Swap)
    - You can do a circular permutation (Sweep)

Naming convention :
    - XXX_one: returns one item
    - delta_XXX: returns the elementary movement
    - XXX_name_YYY: name is the neighborhood name
    - XXX_gen: returns an iterator
"""
