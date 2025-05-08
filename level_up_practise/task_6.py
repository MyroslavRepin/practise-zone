# DELETING ALL VOWELS CHARS FROM STRING
def deleting_vowels(text):
    list_text = []
    result = []
    for char in text:
        list_text.append(char)
    vowels = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ё', 'А', 'Е', 'И', 'О',
              'У', 'Ы', 'Э', 'Ю', 'Я', 'Ё', 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'y', 'Y']
    for char in list_text:
        if char not in vowels:
            result.append(char)

    return "".join(result)


print(deleting_vowels('myroslav'))
