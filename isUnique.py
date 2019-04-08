# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def isUnique(inputStr):
    charSet = set()
    for i in inputStr:
        if i in charSet:
            return False
        else:
            charSet.add(i)
    return True

# Another implementation without different data structure.

def isUniqueInPlace(inputStr):
    checker = 0

    for i in inputStr:
        val = ord(i) - ord('a')
        if (checker & (1 << val)) > 0:
            return False

        checker |= (1 << val)

    return True

if __name__ == '__main__':
    print(isUnique('abcc'))
