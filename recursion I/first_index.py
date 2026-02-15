def first_index(nums,x,i=0):
    if len(nums)==i:
        return -1
    
    if nums[i] == x:
        return i
    return first_index(nums, x, i+1)

    
    
    
print(first_index([1,2,3,1,2,1],1,0))