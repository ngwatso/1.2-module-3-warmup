# Challenge
# Write a logarithmic expression that is identical to this exponential expression:

# 2^n = 64

# log_2 64 = n

# Write an exponential expression that is identical to this logarithmic expression:

# log_2 128 = n

# 2^n = 128

# What keywords should you look out for that might alert you that logarithms are involved?

# halves, doubles

# ===============

"""
Rewrite the implementation of linear search below so that the algorithm searches from the end of the list to the beginning.
"""
'''
def linear_search(arr, target):
    # loop through each item in the input array
    for idx in range(-1, len(arr)):
        # check if the item at the current index is equal to the target
        if arr[idx] == target:
            # return the current index as the match
            return idx
    # if we were able to loop through the entire array, the target is not present
    return -1

print(linear_search([1, 3, 6, 8, 9, 4, 2], 3))
'''

# ===============

Challenge
Write a recursive search function that receives as input an array of integers and a target integer value. This function should return True if the target element exists in the array, and False otherwise.
What would be the base case(s) we'd have to consider for implementing this function?
def checkArr(items, n):
  if n in items:
    return True
  else:
    return 
How should our recursive solution converge on our base case(s)?
In your own words, write out the three rules for recursion and how you can identify when a problem is amenable to using a recursive method.