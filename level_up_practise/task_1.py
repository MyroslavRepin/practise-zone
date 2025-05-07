# CHECKING IF WORL IS POLINDROM
def is_polindrom(word):
    if word[::-1] == word:
        return True
    else:
        return False


print(is_polindrom("шалаш"))
