# binary search uses divide and conquer! We will leverage the fact that our list is SORTED
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0                 # lowest possible index
    
    if high is None:
        high = len(l) - 1               # highest possible index

    if high is None or high < low:
        return -1               # Return -1 if target is not found

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        # Search in the left half
        return binary_search(l, target, low, midpoint - 1)
    else:
        # Search in the right half
        return binary_search(l, target, midpoint + 1, high)

# if __name__ == "__main__":
    l = [1, 3, 5, 10, 12]
    target = 10
    print(binary_search(l, target))                 # Output: 3
 

