import webapp2
import cgi
from  utilities import *

def escape_html(s):
    return cgi.escape(s, quote = True)

form="""
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(text)s</textarea>
      <br>
      <input type="submit">
    </form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.write_form()
    
    def post(self):
        #Get the input text from the form
        text = self.request.get("text")
        #Apply rot13 conversion
        text = rot13(text)
        text = escape_html(text)
        self.write_form(text)
    
    def write_form(self,text=""):
        self.response.out.write(form % {"text" : text})

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)



