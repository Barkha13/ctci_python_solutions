# Palindrome Permutation: Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: taco cat, atc o eta, etc.)

def permutationPalindrome(inputStr):
    countDict = {}
    oddCount = 0
    for char in inputStr:
        if char != ' ':
            if char not in countDict:
                countDict[char] = 1
            else:
                countDict[char] += 1
    
    for key in countDict:
        if countDict[key] % 2 != 0:
            oddCount += 1
    return oddCount <= 1

if __name__ == '__main__':
    print(permutationPalindrome('taco cat'))