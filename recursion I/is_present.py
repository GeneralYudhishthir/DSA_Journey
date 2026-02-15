def is_present(nums,x):
    if len(nums)==0:
        return False

    if nums[0] == x:
        return True
    
    return is_present(nums[1:],x)

print(is_present([1,2,3,4,51],1))