nums = [5, 3, 8, 1, 2]
print("Starting list:", nums)
swapped = True

while swapped:

    # Set swapped to False here
    swapped = False
    for i in range(len(nums) - 1):

    # Compare nums[i] and nums[i + 1]
        if nums[i] > nums[i + 1]:

            # Swap them if needed
            temp = nums[i + 1]
            nums[i + 1] = nums[i]
            nums[i] = temp

            # Don’t forget to mark swapped = True if you do a swap
            swapped = True
            
print("Sorted list:", nums)

# Reflection Questions:

# 1. When there has been no swaps, stated by the "swapped" variable.
# 2. It will go through it and see that there are no swaps and will stop.
# 3. To tell the computer if there was a swap or not.
# 4. To know what you are writing and if there are any bugs, know where they are and how to fix them.
