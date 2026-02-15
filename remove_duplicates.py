def remove_duplicates(nums,x,i=0):
    if len(nums)==i:
        return []
    
    smallans = remove_duplicates(nums,x,i+1)

    if nums[i] == x:
        return smallans
    
    else:
        return [nums[i]]+smallans
    
print(remove_duplicates((1,2,3,1,71,1),1))