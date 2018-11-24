def divide_two_numbers(nr1,nr2):
    return nr1/nr2

def occurence(str1,str2):
    return str2.count(str1)

def extract_letter(str1,str2):
    if str2 in str1:
        return str1.replace(str2,'')
    else:
        return str1