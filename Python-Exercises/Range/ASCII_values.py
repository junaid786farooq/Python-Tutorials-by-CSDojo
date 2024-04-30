# program that prints the ASCII values of lowercase letters from 'a' to 'z' using the range() function.

# ord() function returns the Unicode code point of a given character

for char in range (ord('a'), ord('z') + 1):     
    print(chr(char), ":", char)   
    
    
# chr() function returns the character corresponding to a Unicode code point
