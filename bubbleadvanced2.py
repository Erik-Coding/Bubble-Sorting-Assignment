# Go through each word, check if the next word has a higher number.
# If it does, don't swap. If it doesn't, swap. If they are the same, go to the next letter.

words = ["Wow", "How", "Zero", "Xylophone"]
swapped = True
preWords = words
swaps = 0

print("The original list is:", words)

while swapped:
    swapped = False

    for i in range(len(words) - 1):

        if (words[i].lower() < words[i + 1].lower()):
            temp = words[i + 1]
            words[i + 1] = words[i]
            words[i] = temp

            swapped = True
            swaps += 1




print("The finished list is:", words)
print("It took", swaps, "swaps.")