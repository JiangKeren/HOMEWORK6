import webapp2
import os
import cgi
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values)) 
        
class MainHandler(BaseHandler):
    def get(self):
        self.render("changewords1.html")

class ChHandler(BaseHandler):
    def get(self):
        self.render("changewords2.html")
        w1=cgi.escape(self.request.get("a"))
        w2=cgi.escape(self.request.get("b"))
        char1 = list(w1)
        char2 = list(w2)
        i=0 
        output = ""
        if len(char1)==len(char2):
            for i in range(len(char1)):
                output += char1[i]
                output += char2[i]
    
        if len(char1)<len(char2):
            for i in range(len(char1)):
                output += char1[i]
                output += char2[i] 
            index= len(char1)
            while index < len(char2):
                output +=char2[index]
                index+=1
           
        if len(char2)<len(char1):
            for i in range(len(char2)):
                output += char1[i]
                output += char2[i]
            index= len(char2)
            while index < len(char1):
                output +=char1[index]
                index+=1
           
        self.response.out.write(output)





app = webapp2.WSGIApplication([
    ('/',MainHandler),
    ("/change", ChHandler)
],debug=True)      