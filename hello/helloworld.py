import webapp2

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month">
    </label>
    <label>
        Day
        <input type="text" name="day">
    </label>
    <label>
        Year
        <input type="text" name="year">
    </label>
    <div style="color: red">%(error)s</div>
    <br><br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
  def get(self):
		self.write_form()
	
  def post(self):
		user_month = valid_month(self.request.get('month'))
		user_day = valid_day(self.request.get('day'))
		user_year = valid_year(self.request.get('year'))
		if (user_year and user_month and user_day):
			self.response.out.write("Thanks..thats a valida day")
		else:
			self.write_form("That doesn't look like a valid day")
  
  def write_form(self, error=""):
    self.response.out.write(form % {"error" : error})

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)



### Utilities
# -----------
# User Instructions
# 
# Modify the valid_month() function to verify 
# whether the data a user enters is a valid 
# month. If the passed in parameter 'month' 
# is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.
#

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

# print valid_month('jan')        
# print valid_month('january')
# print valid_month('ja')
# print valid_month('janjuyn')
# print valid_month('123')    

# -----------
# User Instructions
# 
# Modify the valid_day() function to verify 
# whether the string a user enters is a valid 
# day. The valid_day() function takes as 
# input a String, and returns either a valid 
# Int or None. If the passed in String is 
# not a valid day, return None. 
# If it is a valid day, then return 
# the day as an Int, not a String. Don't 
# worry about months of different length. 
# Assume a day is valid if it is a number 
# between 1 and 31.
# Be careful, the input can be any string 
# at all, you don't have any guarantees 
# that the user will input a sensible 
# day.
#

def valid_day(day):
  if day and day.isdigit():
    day = int(day)
    if (day > 0 and day <= 31):
      return day



# print valid_day('0') 
# print valid_day('1') 
# print valid_day('33')

# -----------
# User Instructions
# 
# Modify the valid_year() function to verify 
# whether the string a user enters is a valid 
# year. If the passed in parameter 'year' 
# is not a valid year, return None. 
# If 'year' is a valid year, then return 
# the year as a number. Assume a year 
# is valid if it is a number between 1900 and 
# 2020.
#

def valid_year(year):
  if year and year.isdigit():
    year = int(year)
    if (year >= 1900 and year <= 2020):
      return year  


# valid_year('0') => None    
# valid_year('-11') => None
# valid_year('1950') => 1950
# valid_year('2000') => 2000