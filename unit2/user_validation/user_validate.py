import webapp2
import cgi
from  utilities import *

html="""
<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
            %(username_error)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
          %(password_error)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(verify_error)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
            %(email_error)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.write_form()
    
    def post(self):
      #Read the data interms of dictionary
      user_values = { "username" : self.request.get('username'),
                        "password" : self.request.get('password'),
                        "verify" : self.request.get('verify'),
                        "email" : self.request.get('email')
                      }
      #Assume that the values are correct
      valid_data = True
      validations = {}
      if not valid_username(user_values.get('username')):
        validations["username_error"] = "That's not a valid username."
        valid_data = False
      if valid_password(user_values.get('password')):
        #Password is valid, check if it is same
        if not (user_values.get('password') == user_values.get('verify')):
          #Passwords do not match
          valid_data = False
          validations["verify_error"] = "Your passwords didn't match."
      else:
        validations["password_error"] = "That wasn't a valid password."
        valid_data = False
      email = user_values.get('email')
      #If email is entered (optional) check for its validity
      if email and not (valid_email(email)):
        validations["email_error"] = "That's not a valid email."
        valid_data = False
      
      #Extend the user values with the validation errors
      user_values = dict(user_values,**validations)
      user_values =  escape_html_dict(user_values)

      if valid_data:
        #Data is valid
        self.redirect('/welcome?username=' + user_values.get('username'))
      else:
        #If data is in valid
        self.write_form(user_values)

      
    
    def write_form(self,values={}):
        default_values = {  "username" : "",
                            "username_error" : "",
                            "password_error" : "",
                            "verify_error" : "",
                            "email" : "",
                            "email_error" : ""
                            };
        #Extend the default values with the supplied values
        final_values = dict(default_values,**values)
        self.response.out.write(html % final_values)

class WelcomeHandler(webapp2.RequestHandler):

  def get(self):
      html_local = """
        <!DOCTYPE html>
        <html>
          <head>
            <title>Unit 2 Signup</title>
          </head>

          <body>
            <h2>Welcome, %s!</h2>
          </body>
        </html>
      """
      self.response.out.write(html_local % self.request.get('username'))

app = webapp2.WSGIApplication([('/', MainPage),('/welcome', WelcomeHandler)], debug=True)



