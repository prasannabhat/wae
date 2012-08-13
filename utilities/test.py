import cgi
from validation_utilities import *
# print valid_username('prasanna ')
# print valid_email('abn@abc.out')
a = {}
a['a'] = 1
a['hi'] = 2

def escape_html(s):
    return cgi.escape(s, quote = True)

def escape_html_dic(dic):
	ret = {}
	for k, v in dic.iteritems():
		dic[k] = escape_html(str(v))
	return dic	

print escape_html_dic(a)