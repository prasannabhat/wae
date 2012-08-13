import string 

  
def rot13(str, dic={}):
    shift_length = 13
    #Create a dictionary for substitution, if nothing is given
    if (len(dic) == 0):
        alphabet = string.ascii_lowercase
        for i in range(0,len(alphabet)):  
            dic[alphabet[i]]=alphabet[(i+shift_length)%len(alphabet)] 
            
        alphabet = string.ascii_uppercase 
        for i in range(0,len(alphabet)):  
            dic[alphabet[i]]=alphabet[(i+shift_length)%len(alphabet)] 
    x = "".join(map(lambda x:dic.get(x) if x in dic else x,str))
    return x  
   
