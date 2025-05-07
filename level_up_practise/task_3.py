def bigger_char(text):
    alphabetDict = dict()

    for char in text:
        if char in alphabetDict:
            alphabetDict[char] += 1
        else:
            alphabetDict[char] = 1
    max_value = max(alphabetDict.values())
    print(max_value)


print(bigger_char("abbbbccc"))
