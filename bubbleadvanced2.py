# Go through each word, check if the next word has a higher number.
# If it does, don't swap. If it doesn't, swap. If they are the same, go to the next letter.

words = ["Wow", "How", "Zero", "Xylophone"]
swapped = True
preWords = words
swaps = 0

print("The original list is:", words)

# While swapped is true
while swapped:
    # set swapped to false
    swapped = False
    # for i in range of the amount of words there are minus 1
    for i in range(len(words) - 1):
        # if i in index lowercased is less than i plus 1 lowercased
        if (words[i].lower() < words[i + 1].lower()):
            # add the index of i plus 1 of words to temp variable
            temp = words[i + 1]
            # set the index of i plus 1 of words to the index of i
            words[i + 1] = words[i]
            # set the index of i in words to the temp variable
            words[i] = temp
            # set swapped to true
            swapped = True
            # add one to swaps
            swaps += 1



# print the final result and how many swaps it took
print("The finished list is:", words)
print("It took", swaps, "swaps.")
