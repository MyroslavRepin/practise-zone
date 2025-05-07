# FINDING MOST FREQUINLY REPEATED CHAR
def bigger_char(text):
    alphabetDict = dict()

    for char in text:
        if char in alphabetDict:
            alphabetDict[char] += 1
        else:
            alphabetDict[char] = 1
    max_value = max(alphabetDict.values())
    print(max_value)
    print(alphabetDict)

    keys = [key for key, val in alphabetDict.items() if val == max_value]
    print(keys)


bigger_char("abbbbccc")
