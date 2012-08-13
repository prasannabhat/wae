import webapp2
import cgi
from  utilities import *

def escape_html(s):
    return cgi.escape(s, quote = True)

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>
        Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>
        Year
        <input type="text" name="year" value="%(year)s">
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
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')
        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)
        if (year and month and day):
            self.redirect('/thanks')
        else:
            self.write_form("That doesn't look like a valid day",user_day,user_month,user_year)
  
    def write_form(self, error="",day="",month="",year=""):
        self.response.out.write(form % {"error" : error,
                                    "day" : escape_html(day),
                                    "month" : escape_html(month),
                                    "year" : escape_html(year)})

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks ! that's a totally valid day!")

app = webapp2.WSGIApplication([('/', MainPage),('/thanks', ThanksHandler)], debug=True)



