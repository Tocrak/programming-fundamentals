import sys
from my_module import occurence

str1 = sys.argv[1]
str2 = sys.argv[2]
print('String ',str1,' occurred ',occurence(str1,str2),' times in string ',str2)