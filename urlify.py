# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.

def URLify(inputStr):
    str1 = inputStr.strip().replace(' ', '%20')
    return str1

    

# Without using in built method. Reversing the string to avoid trailing whitespaces.
def URLify2(inputStr):
    result = ''
    start = False
    for i in reversed(inputStr):
        if i != ' ':
            start = True
        if(i == ' ' and start == True):
            result += '02%'
        else: result += i
    return result[::-1]
    
if __name__ == '__main__':
    print(URLify2('Mr John Smith'))