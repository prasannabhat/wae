# import string_test
from string_test import replacer

test = "hello world"
test = replacer(test,['e','l','o'],'?')

import string 
alphabet = string.ascii_uppercase
alphabet = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
print alphabet