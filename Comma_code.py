spam = ['apples', 'bananas', 'tofu', 'cats']
empty = []
def comma_code(list):
    string = ''
    for x in list:
        string += x +', '
        print(string)
    return string

comma_code(spam)