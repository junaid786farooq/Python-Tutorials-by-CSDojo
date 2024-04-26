# Given a string, return a string where for every char in the original, there are two chars.
'''
double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
'''

def double_char(str):
    to_return = ""
    for x in str:
        to_return += x*2
    print(to_return)

double_char("ABC")