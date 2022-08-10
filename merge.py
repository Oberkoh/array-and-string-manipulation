"""
In order to win the prize for most cookies 
sold, my friend Alice and I are going to 
merge our Girl Scout Cookies orders and 
enter as one unit.
"""

def merge_lists(list1, list2):
    return sorted(list1 + list2)

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))