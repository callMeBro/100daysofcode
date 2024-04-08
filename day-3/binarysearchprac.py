def bs(l, target, low, high):
    if low is None or high is None:
        return -1
    
    # Find midpoint 
    midpoint = (low + high) // 2

    if target == l[midpoint]:
        return midpoint

    if target < l[midpoint]:
        return bs(l, target, low, midpoint - 1)
    else:
        return bs(l, target, midpoint + 1, high)


l = [1, 5, 6, 10, 24]
target = 5
low = 0
high = len(l) - 1
print(bs(l, target, low, high)) 
