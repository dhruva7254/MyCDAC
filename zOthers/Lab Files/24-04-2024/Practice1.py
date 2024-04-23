

cAR
def sum_list(items):
    total = 0
    for x in items:
        total += x
    return total

my_list = [1, 2, 3, 4, 5]
print("Sum of list:", sum_list(my_list))
-----------------------------------------
def multiply_list(items):
    result = 1
    for x in items:
        result *= x
    return result

my_list = [1, 2, 3, 4, 5]
print("Product of list:", multiply_list(my_list))
--------------------------------------------------
def largest_number(items):
    return max(items)

my_list = [10, 20, 30, 40, 50]
print("Largest number:", largest_number(my_list))
-------------------------------------------------
def smallest_number(items):
    return min(items)

my_list = [10, 20, 30, 40, 50]
print("Smallest number:", smallest_number(my_list))

---------------------------------------------------
def count_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

my_list = ['abc', 'xyz', 'aba', '1221']
print("Count of strings:", count_strings(my_list))
--------------------------------------------------
def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[-1])

my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted list:", sort_tuples(my_list))
---------------------------------------------------
def remove_duplicates(items):
    unique_list = []
    for item in items:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = [1, 2, 3, 2, 4, 3, 5]
print("List after removing duplicates:", remove_duplicates(my_list))
----------------------------------------------------------------------
def is_empty(items):
    return len(items) == 0

my_list = []
print("Is list empty?", is_empty(my_list))
----------------------------------------------
def clone_list(items):
    return items[:]

my_list = [1, 2, 3, 4, 5]
clone = clone_list(my_list)
print("Original list:", my_list)
print("Cloned list:", clone)
-----------------------------------
def find_long_words(words, n):
    return [word for word in words if len(word) > n]

word_list = ['apple', 'banana', 'orange', 'kiwi', 'strawberry']
n = 5
print("Words longer than", n, "characters:", find_long_words(word_list, n))
------------------------------------------------------------------------------
def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print("Do lists have at least one common member?", has_common_member(list1, list2))
------------------------------------------------------------------------------------
def remove_elements(items, indices):
    return [item for index, item in enumerate(items) if index not in indices]

my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
indices = [0, 4, 5]
print("List after removing specified elements:", remove_elements(my_list, indices))
-------------------------------------------------------------------------------------
array_3d = [[['*' for k in range(6)] for j in range(4)] for i in range(3)]
print("3D array:", array_3d)
--------------------------------
def remove_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List after removing even numbers:", remove_even_numbers(numbers_list))
-------------------------------------------------------------------------------
import random

def shuffle_list(items):
    random.shuffle(items)
    return items

my_list = [1, 2, 3, 4, 5]
print("Shuffled list:", shuffle_list(my_list))
--------------------------------------------------
