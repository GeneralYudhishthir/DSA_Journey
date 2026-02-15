def all_indices(nums,x,i=0):
    if len(nums)==i:
        return []
    
    smallans = all_indices(nums,x,i+1)

    if nums[i] == x:
        return [i]+smallans
    
    else:
        return smallans
    
print(all_indices([1,2,3,1],1))