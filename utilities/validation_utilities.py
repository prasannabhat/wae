# User Instructions
# 
# Write a function 'sub1' that, given a 
# string, embeds that string in 
# the string: 
# "I think X is a perfectly normal thing to do in public."
# where X is replaced by the given 
# string.
#

given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
  ret_val = given_string % s
  print ret_val
  return ret_val


sub1("running") 
# => "I think running is a perfectly normal thing to do in public."    
sub1("sleeping") 
# => "I think sleeping is a perfectly normal thing to do in public.

# User Instructions
# 
# Write a function 'sub_m' that takes a 
# name and a nickname, and returns a 
# string of the following format: 
# "I'm NICKNAME. My real name is NAME, but my friends call me NICKNAME."
# 

given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
  str = given_string2 % {"nickname" : nickname , "name" : name}
  print str
  return str
  
    
    

sub_m("Mike", "Goose") 
# => "I'm Goose. My real name is Mike, but my friends call me Goose."