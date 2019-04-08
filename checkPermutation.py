# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
def checkPermutation(str1, str2):
    return set(str1) == set(str2)

if __name__ == '__main__':
    print(checkPermutation('taco', 'cato'))

# Another approach can be to sort the strings and then compare both the strings.