import string 
def replacer(str,items,repl):
    x = "".join(map(lambda x:repl if x in items else x,str))
    return x
	
def rot13(str, dic={}):
    shift_length = 13
    if (len(dic) == 0):
        alphabet = string.ascii_lowercase
        for i in range(0,len(alphabet)):  
            dic[alphabet[i]]=alphabet[(i+shift_length)%len(alphabet)] 
            
        alphabet = string.ascii_uppercase	
        for i in range(0,len(alphabet)):  
            dic[alphabet[i]]=alphabet[(i+shift_length)%len(alphabet)] 
    x = "".join(map(lambda x:dic.get(x) if x in dic else x,str))
    return x	
    
	
	
	
shift_length = 2


alphabet = string.ascii_lowercase

dic={}  
for i in range(0,len(alphabet)):  
	dic[alphabet[i]]=alphabet[(i+shift_length)%len(alphabet)] 
	
alphabet = string.ascii_uppercase	
for i in range(0,len(alphabet)):  
	dic[alphabet[i]]=alphabet[(i+shift_length)%len(alphabet)] 
	

test = "hello world...!!How are you </a>"
print "Original string : "
print test
test = rot13(test)
print "After rot 13 : "
print test
test = rot13(test)
print "After rot 13 again : "
print test
