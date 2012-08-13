import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

def valid_month(month):
    month_abbvs = dict((m[:3].lower(),m) for m in months)          
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)



def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if (day > 0 and day <= 31):
            return day


def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if (year >= 1900 and year <= 2020):
            return year  

import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PWD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
  if USER_RE.match(username):
    return True
  else:
    return False

def valid_password(pwd):
  if PWD_RE.match(pwd):
    return True
  else:
    return False

def valid_email(email):
  if EMAIL_RE.match(email):
    return True
  else:
    return False            

#HTML escape all the values in the given dictionary
def escape_html_dict(values):
    for k, v in values.iteritems():
        values[k] = escape_html(v)
    return values


