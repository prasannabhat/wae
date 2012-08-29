import hashlib
import hmac

import random
import string

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

# Implement the function valid_pw() that returns True if a user's password 
# matches its hash. You will need to modify make_pw_hash.

def make_pw_hash(name, pw):
    salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)    

def hash_str_prev(s):
    return hashlib.md5(s).hexdigest()

# Implement the hash_str function to use HMAC and our SECRET instead of md5
SECRET = 'imsosecret'
def hash_str(s):
	return hmac.new(SECRET,s).hexdigest()
    ###Your code here    

# -----------------
# User Instructions
# 
# Implement the function make_secure_val, which takes a string and returns a 
# string of the format: 
# s,HASH

def make_secure_val(s):
	return "%s|%s" % (s,hash_str(s))

# -----------------
# User Instructions
# 
# Implement the function check_secure_val, which takes a string of the format 
# s,HASH
# and returns s if hash_str(s) == HASH, otherwise None 

def check_secure_val(h):
	val = h.split('|')[0]
	if h == make_secure_val(val):
	    return val

print hash_str("hello")