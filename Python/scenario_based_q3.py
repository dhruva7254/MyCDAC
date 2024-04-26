
# Problem 3:

# Take a list of integers. Every time you can select the first element or last element.
# Always next number selected should be less than or equal to the currently selected number. If no number can be selected to fulfill all conditions then return False. If all elements are completed using the selection criteria then print True. You have to try all the combinations possible before conclusion.

# Ex. 
# L=[1,2,3,4,5]

# We can select 1 or 5 at step 1
# Assume, First 5 is selected (last element)
# Then, [1,2,3,4]we can select 1 or 4,  we will select 4 because 4<5
# Then [1,2,3] we can select 1 or 3, so select 3 because 3<5

# Like this we can select 5,4,3,2,1 and all elements are selected so print True
# But if we select 1 then we cannot select further elements
# Because, after selecting 1 list will be [2,3,4,5] and first 2 and last 5 both are greater than 1

# So, when selecting first element use the right choice so that there can be possibility of selection of all elements

# L=[1,3,2]

# We can select 1 or 2 at step1
# Assume we select 1,
# Then [3,2] so we can select 3 or 2 but both are greater than 1
# So, there is no way we can completely select all elements

# Assume we select 2,
# Then [1,3], so we can select 1 or 3, we select 1 because 1<2,
# Then [3], so we can ONLY select 3 but 3 is greater than 1

# So print False, because in all options we cannot select all elements from the list

def can_select_all(L):
    def helper(left, right, prev):
        if not left and not right:
            return True
        if left and left[0] <= prev:
            if helper(left[1:], right, left[0]):
                return True
        if right and right[-1] <= prev:
            if helper(left, right[:-1], right[-1]):
                return True
        return False

    if not L:
        return False
    return helper(L[1:], L[:-1], L[0]) or helper(L[:-1], L[1:], L[-1])

# Example usage:
L1 = [1, 2, 3, 4, 5]
print(can_select_all(L1))  # Output: True

L2 = [1, 3, 2]
print(can_select_all(L2))  # Output: False
